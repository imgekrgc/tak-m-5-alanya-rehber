#!/usr/bin/env python3
"""docs/ai-log.md içindeki eksik ya da doldurulmamış hücreleri bulur.

Kullanım (repo kökünden):
    python scripts/ai_log_kontrol.py
    python scripts/ai_log_kontrol.py docs/ai-log.md

Altı sütun beklenir: Tarih | Kim | Araç ve model | Ne istendi | Sonuç | Ne değiştirildi
Boş hücre, "...", "…", "DOLDURULACAK", "Ad Soyad" ve YYYY-MM-DD dışındaki tarihler eksik sayılır.
Eksik varsa çıkış kodu 1 olur.
"""
import re
import sys

BASLIKLAR = ["Tarih", "Kim", "Araç ve model", "Ne istendi", "Sonuç", "Ne değiştirildi"]
YER_TUTUCU = ("...", "…", "doldurulacak", "ad soyad")


def hucreler(satir):
    return [h.strip() for h in satir.strip().strip("|").split("|")]


def main():
    yol = sys.argv[1] if len(sys.argv) > 1 else "docs/ai-log.md"
    with open(yol, encoding="utf-8") as f:
        satirlar = [s for s in f.read().splitlines() if s.strip().startswith("|")]

    veri = [s for s in satirlar[2:]]  # başlık ve ayırıcı satırı atla
    sorunlar = []
    for n, satir in enumerate(veri, start=1):
        h = hucreler(satir)
        if len(h) != len(BASLIKLAR):
            sorunlar.append(f"Satır {n}: {len(h)} sütun var, {len(BASLIKLAR)} olmalı")
            continue
        for ad, deger in zip(BASLIKLAR, h):
            kucuk = deger.lower()
            if not deger or any(y in kucuk for y in YER_TUTUCU):
                sorunlar.append(f"Satır {n}: '{ad}' eksik ({deger or 'boş'})")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", h[0]):
            sorunlar.append(f"Satır {n}: tarih YYYY-AA-GG biçiminde olmalı ({h[0]})")

    print(f"{len(veri)} satır kontrol edildi.")
    if sorunlar:
        print(f"{len(sorunlar)} sorun bulundu:")
        for s in sorunlar:
            print(" -", s)
        sys.exit(1)
    print("Eksik yok.")


if __name__ == "__main__":
    main()
