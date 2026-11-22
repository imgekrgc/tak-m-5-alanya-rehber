#!/usr/bin/env python3
"""docs/karsilastirma.csv dosyasından docs/karsilastirma.md özetini üretir.

Kullanım (repo kökünden):
    python scripts/olcum_ozeti.py
    python scripts/olcum_ozeti.py --csv docs/karsilastirma.csv --out docs/karsilastirma.md

CSV sütunları:
    no,tur,gemini_v1_puan,gemini_v1_sure_sn,gemini_v2_puan,claude_model,claude_puan,claude_sure_sn,not
Boş hücreler ortalamaya girmez. Betik "Tek değişiklik" ve "Karar" satırlarını
DOLDURULACAK olarak bırakır; onları siz yazarsınız.
"""
import argparse
import csv
from collections import Counter


def sayi(deger):
    deger = (deger or "").strip().replace(",", ".")
    if not deger:
        return None
    try:
        return float(deger)
    except ValueError:
        return None


def ortalama(degerler):
    degerler = [d for d in degerler if d is not None]
    if not degerler:
        return None
    return sum(degerler) / len(degerler)


def bicim(x, basamak=2):
    return "—" if x is None else f"{x:.{basamak}f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="docs/karsilastirma.csv")
    ap.add_argument("--out", default="docs/karsilastirma.md")
    args = ap.parse_args()

    with open(args.csv, encoding="utf-8", newline="") as f:
        satirlar = list(csv.DictReader(f))

    def sutun(ad, sadece_kenar=False):
        return [
            sayi(r.get(ad))
            for r in satirlar
            if not sadece_kenar or (r.get("tur") or "").strip() == "kenar"
        ]

    modeller = Counter(
        (r.get("claude_model") or "").strip() for r in satirlar if (r.get("claude_model") or "").strip()
    )
    claude_adi = modeller.most_common(1)[0][0] if modeller else "Sonnet veya Haiku"

    v1, v2, cl = "gemini_v1_puan", "gemini_v2_puan", "claude_puan"
    iyilesen, kotulesen = [], []
    for r in satirlar:
        a, b = sayi(r.get(v1)), sayi(r.get(v2))
        if a is None or b is None:
            continue
        if b > a:
            iyilesen.append((r["no"], a, b))
        elif b < a:
            kotulesen.append((r["no"], a, b))

    def vaka_listesi(liste):
        if not liste:
            return "yok"
        return ", ".join(f"{no} ({a:g}→{b:g})" for no, a, b in liste)

    uyarilar = []
    if not kotulesen:
        uyarilar.append("Skoru düşen vaka yok; vakaları ve v2 puanlarını bir kez daha kontrol edin.")
    bos = [r["no"] for r in satirlar if sayi(r.get(v1)) is None]
    if bos:
        uyarilar.append("gemini_v1_puan boş vakalar: " + ", ".join(bos))

    md = f"""# Model karşılaştırması

| | Gemini (Skill v1) | Gemini (Skill v2) | Claude ({claude_adi}) |
| --- | --- | --- | --- |
| Ortalama puan (0–2) | {bicim(ortalama(sutun(v1)))} | {bicim(ortalama(sutun(v2)))} | {bicim(ortalama(sutun(cl)))} |
| Kenar durumlarda ortalama | {bicim(ortalama(sutun(v1, True)))} | {bicim(ortalama(sutun(v2, True)))} | {bicim(ortalama(sutun(cl, True)))} |
| Ortalama süre (sn) | {bicim(ortalama(sutun("gemini_v1_sure_sn")), 1)} | — | {bicim(ortalama(sutun("claude_sure_sn")), 1)} |

Tek değişiklik: DOLDURULACAK
İyileşen vakalar: {vaka_listesi(iyilesen)}
Kötüleşen vakalar: {vaka_listesi(kotulesen)}
Karar: Uygulamada DOLDURULACAK kalıyor, çünkü DOLDURULACAK

Not: Gemini v2 için süre ölçülmedi. Claude ölçümü Skill v1 ile yapıldı. Süreler internet hızına ve servis yoğunluğuna bağlıdır; yaklaşık karşılaştırma içindir.
"""
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"{args.out} yazıldı ({len(satirlar)} vaka).")
    for u in uyarilar:
        print("UYARI:", u)


if __name__ == "__main__":
    main()
