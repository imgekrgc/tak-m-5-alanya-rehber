# <Uygulama adı>

Alanya turizm rehberi ve otel yorum panosu. Turiste rota önerir, otel işletmecisine misafir yorumlarını özetler. Bu bir ders projesidir; tüm veriler sentetiktir.

## Takım ve roller

| Rol | Kim | Sorumlu olduğu çıktılar |
| --- | --- | --- |
| Ürün sahibi | Hüseyin Özen (İşletme) | Problem ve kullanıcı, uygulama içeriği, 25 vakalık test seti ve alan doğruluğu puanı, kullanıcı testi |
| İçerik ve yayın sorumlusu | Asrın Sezen (Animasyon) | YouTube videoları, tanıtım sayfasının metinleri, benimseme planı, final sunumu |
| Teknik lider | İmge Karaağaç (BP) | Mimari, repo düzeni, pull request onayı, web ve APK yayını |
| Uygulama geliştiricisi | Yunus Emre Unğan (BP) | Ekranlar, API route, Gemini bağlantısı, onay pencereleri |
| AI ve ölçüm sorumlusu | Oktay Kılıç (BP) | SKILL.md, EmbeddingGemma 2, model karşılaştırması, AI kullanım günlüğü |

Web sayfası işini teknik lider ile içerik ve yayın sorumlusu paylaşır.

## Problem ve hedef kullanıcı

**Hedef kullanıcılar:** Alanya'ya gelen turist (rehber tarafı) ve küçük bir otelin işletmecisi (yorum panosu tarafı).

Alanya'ya gelen turist bugün tarihî mekanları, plajları ve doğa rotalarını birçok blog, harita ve forum arasında tek tek arayıp günlük planını elle çıkarıyor; hangi mekanın hangisine yakın olduğunu ve ilgi alanına uyup uymadığını anlamak zor. Küçük otel işletmecisi ise farklı sitelerdeki misafir yorumlarını tek tek okuyor ve hangi konuda (temizlik, personel, konum, fiyat, yemek) şikâyet aldığını görmek için zaman harcıyor. Uygulama, takımın kaynak göstererek yazdığı mekan kartlarından ilgi alanına ve süreye göre rota önererek turistin; yorumları olumlu/olumsuz ve konuya göre özetleyerek de işletmecinin işini kolaylaştıracak.

**Kullanıcı görevleri**

1. Bir günlük tarih rotası oluşturun.
2. Bir mekandan benzerlerine geçin.
3. Yorum panosunda olumsuz yorumların özetini görün.

## Canlı linkler

| Çıktı | Link |
| --- | --- |
| Web uygulaması (EAS Hosting) | <https://EAS-ADRESINIZ/> |
| Android APK (EAS Build) | <https://APK-LINKINIZ> |
| iPhone | Web adresini Safari'de açıp Paylaş > Ana Ekrana Ekle ile PWA olarak kullanın |
| Tanıtım sayfası (GitHub Pages) | <https://KULLANICI.github.io/takim-5-site/> |
| YouTube kanalı | <KANAL-LINKI> |
| Short 1 · Alanya'da bir günü nasıl planlarsınız? | <LINK> |
| Short 2 · Maskotla uygulama turu | <LINK> |
| Tanıtım videosu | <LINK> |

## Kurulum

Gereksinimler: Git, Node.js (LTS).

```bash
git clone https://github.com/<kullanici>/takim-5-alanya-rehber.git
cd takim-5-alanya-rehber/uygulama
npm install
```

Gemini API anahtarını `.env` dosyasına yazın (örnek: `.env.example`). `.env` repoya girmez:

```
GEMINI_API_KEY=buraya-anahtar
```

Çalıştırma:

```bash
npx expo start
```

Terminalde `w` tuşuna basınca uygulama tarayıcıda açılır. SDK 58 projeleri Expo Go'da açılmayabilir; geliştirmede tarayıcıyı, telefonda APK'yı kullanın.

Web yayını:

```bash
npx expo export -p web
eas deploy --prod
```

## Mimari

- **Arayüz:** Expo (SDK 58) ve Expo Router; ekranlar `src/app/` altında: Ana sayfa, Mekanlar, Mekan detayı, Rotam, Yorum panosu, Sor.
- **Sunucu tarafı:** `src/app/api/sor+api.ts` ve `src/app/api/yorum+api.ts` API route'ları; Gemini'ye yalnızca bu route'lar bağlanır, anahtar istemciye inmez.
- **Veri:** `src/data/veri.json` (mekan kartları ve sentetik yorumlar), `src/data/benzerler.json` (EmbeddingGemma 2 ile hesaplanan benzer mekanlar).
- **Talimat:** `skills/alanya-rehber-asistani/SKILL.md`; gövdesi `src/ai/skill.ts` ile aynıdır.
- **Yayın:** Web için EAS Hosting, Android için EAS Build (APK), tanıtım sayfası için GitHub Pages.
- **Akış:** Kullanıcı soruyu yazar → API route soruyu talimat ve uygulama verisiyle Gemini'ye gönderir → yanıt ekranda gösterilir. Hata veya limit varsa kullanıcıya hata mesajı gösterilir. Ayrıntı: `docs/ai-akisi.md`.

## AI bileşenleri

| Bileşen | Ne yapıyor | Kaynak |
| --- | --- | --- |
| Gemini | Mekan kartlarından rota önerir; yorumları olumlu/olumsuz/karışık ve konuya göre (temizlik, personel, konum, fiyat, yemek) JSON olarak sınıflandırır | [Gemini API fiyatlandırma ve ücretsiz katman](https://aistudio.google.com/docs/pricing) |
| Agent Skill | Yanıt kurallarını belirler: kartta olmayan bilgiyi uydurmama, soru dilinde yanıt, en fazla 5 durak ve 6 cümle, yorumlarda yalnızca JSON | [Agent Skills belirtimi](https://agentskills.io/specification) |
| EmbeddingGemma 2 | "Benzer öneriler" alanı için her mekanın en benzer 3 mekanını hesaplar (`notebooks/embeddinggemma.ipynb`) | [EmbeddingGemma 2 model kartı](https://huggingface.co/google/embeddinggemma-2) |
| Claude (Sonnet veya Haiku) | Model karşılaştırması için aynı 25 vaka üzerinde ölçüldü | [Claude planları ve fiyatları](https://claude.com/pricing) |

Her AI kullanımı `docs/ai-log.md` dosyasına yazılmıştır.

## Ölçüm ve model karşılaştırması

25 vakalık test seti: `docs/test-seti.csv` (15 normal: 10 rota ve mekan sorusu, 5 yorum sınıflandırması; 10 kenar durum). Puanlama: 2 = doğru ve kurallara uygun, 1 = kısmen, 0 = yanlış veya kural dışı. Ham sonuçlar: `docs/karsilastirma.csv`; özet: `docs/karsilastirma.md`.

| | Gemini (Skill v1) | Gemini (Skill v2) | Claude (Sonnet veya Haiku) |
| --- | --- | --- | --- |
| Ortalama puan (0–2) | | | |
| Kenar durumlarda ortalama | | | |
| Ortalama süre (sn) | | | |

**Skill'deki tek değişiklik:** …

**Uygulamada kalan model ve gerekçe:** …

Kullanıcı testi (sınıf dışından 3 kişi, 3 görev): `docs/kullanici-testi.md`. İnce ayar kararı: `docs/karar-tablosu.md`.

## Sınırlılıklar

> Teslimden önce gerçek durumla güncelleyin. Aşağıdakiler kılavuzdan ve tasarımdan bilinen sınırlılıklardır.

- Tüm veriler sentetiktir: 30 mekan kartı ve 50 sentetik yorum; gerçek bir otelin veya kişinin verisi değildir.
- Fiyat, giriş ücreti ve açılış saati kartlarda yoktur; uygulama bu sorulara "Bu bilgi uygulamada yok" diye yanıt verir. Güncel bilgi için resmi kaynaklara bakın.
- Uygulama yalnızca mekan kartlarındaki bilgiye dayanır; kartta olmayan mekanlar için öneri veya rota üretmez.
- Ücretsiz Gemini katmanının dakika ve günlük limitleri vardır; limit dolunca uygulama hata mesajı gösterir.
- iOS derlemesi yoktur (ücretli Apple geliştirici hesabı gerektirir); iPhone'da web adresi PWA olarak kullanılır.
- Üç dilde (Türkçe, İngilizce, Almanca) yanıt hedeflenir; başka dillerde kalite ölçülmemiştir.
- Yorum sınıflandırması ironik veya karışık yorumlarda hata yapabilir; ayrıştırılamayan yanıtlar ölçüm tablosunda sayılmıştır.
- Çalışmayanlar / yarım kalanlar: *(teslimden önce buraya dürüstçe yazın)*

## Katkı beyanı

Her üye kendi katkısını yazar; tüm üyeler onaylar.

| Üye | Rol | Katkım | Onay |
| --- | --- | --- | --- |
| Hüseyin Özen | Ürün sahibi | Problem tanımı ve hedef kullanıcı, mekan kartları ve kaynakları, 25 vakalık test seti ve alan doğruluğu kontrolü, karar tablosu, kullanıcı testi, README | ☐ |
| Asrın Sezen | İçerik ve yayın sorumlusu | | ☐ |
| İmge Karaağaç | Teknik lider | | ☐ |
| Yunus Emre Unğan | Uygulama geliştiricisi | | ☐ |
| Oktay Kılıç | AI ve ölçüm sorumlusu | | ☐ |

## Lisans

Başkasının kodu lisansına uygun ve kaynak gösterilerek kullanılmıştır. Lisans dosyası: `LICENSE`.
