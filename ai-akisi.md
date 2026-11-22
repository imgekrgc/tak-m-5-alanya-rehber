# AI akışı

## Akış 1 · Sor ekranı (rota ve mekan soruları)

Tetikleyici: Kullanıcı Sor ekranında soru yazıp Gönder'e basar
AI işlemi: /api/sor route'u soruyu talimat (SKILL) ve uygulamanın verisiyle (veri.json) tek bir istekte Gemini'ye gönderir
Koşul: Soru boş ya da 2000 karakterden uzunsa 400; Gemini hata verir ya da limit dolarsa 503 ve "AI şu an yanıt veremiyor" mesajı
Çıktı: Yanıt ekranda gösterilir (en fazla 5 duraklı rota ya da kısa cevap)
İnsan onayı: AI yalnızca öneri metni üretir, uygulama bu yanıtla hiçbir işlem yapmaz; rotayı kabul edip etmemek kullanıcıya aittir
Kayıt: AI kullanım günlüğü (docs/ai-log.md) ve ölçüm dosyaları docs/ altında

## Akış 2 · Yorum sınıflandırma (yorum panosu)

Tetikleyici: Otel işletmecisi yorum panosunu açar ya da bir yorumu sınıflandırır
AI işlemi: /api/yorum route'u yorumu SKILL ile Gemini'ye gönderir ve yalnızca JSON ister ({"duygu": ..., "konular": [...]})
Koşul: JSON ayrıştırılamazsa duygu "bilinmiyor" olur, ayrıştırılamayan yanıt sayısı ölçüm tablosuna girer; Gemini hata verirse hata mesajı gösterilir
Çıktı: Her yorum için duygu ve konu etiketi; panoda olumsuz yorumların özeti
İnsan onayı: Sınıflandırma yalnızca gösterilir. Yorum silme ya da misafire yanıt gönderme gibi bir işlem varsa onayIste penceresi olmadan çalışmaz (Adım 12.4)
Kayıt: Ayrıştırılamayan yanıt sayısı ve vaka puanları docs/karsilastirma.csv dosyasında

## Akış 3 · Benzer mekanlar (AI çağrısı çalışma anında yok)

Tetikleyici: Kullanıcı Mekan detayı ekranını açar
AI işlemi: EmbeddingGemma 2, Colab'da bir kez çalıştırılır; her mekanın en benzer 3 mekanı hesaplanıp src/data/benzerler.json dosyasına yazılır. Uygulama çalışırken model çağrılmaz, hazır dosya okunur
Koşul: Mekanın benzerler.json'da kaydı yoksa "Benzer öneriler" alanı boş kalır
Çıktı: Detay ekranında "Benzer öneriler" listesi
İnsan onayı: Gerekmez; yalnızca öneri listesidir. Mekan verisi değişirse not defteri takım tarafından yeniden çalıştırılır
Kayıt: notebooks/embeddinggemma.ipynb ve src/data/benzerler.json repoda

## Karar: İş akışı mı, ajan mı?

| Soru | Yanıt |
| --- | --- |
| Adımlar önceden bilinir mi? | Evet: soru al, talimat ve veriyi ekle, Gemini'ye gönder, yanıtı göster |
| Adım sayısı sabit mi? | Evet: her istekte tek bir Gemini çağrısı |
| Hata olunca kod mu karar verir? | Evet: try/catch ve JSON ayrıştırma koduna bağlı, model karar vermez |
| Her adım ayrı test edilebilir mi? | Evet: route, ekran, JSON ayrıştırma ve 25 vakalık set ayrı ayrı denenir |
| Maliyet öngörülebilir mi? | Evet: istek başına tek çağrı, ücretsiz katman limiti içinde |
| Hata ayıklama kolay mı? | Evet: girdi, talimat ve çıktı tek noktada görülür |

Karar: İş akışı. Gerekçe: Altı sorunun hepsi "evet"; adımlar kodda sabit, modelin hangi aracı ya da kaç adım çalıştıracağına karar verdiği bir döngü yok.
