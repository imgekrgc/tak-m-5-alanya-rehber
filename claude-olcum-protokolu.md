# Adım 13.3 · Claude ile model karşılaştırması

Sorumlu: Oktay Kılıç (AI ve ölçüm sorumlusu)
Ön koşul: docs/test-seti.csv 25 vakaya tamamlanmış (Adım 13.1) ve Gemini v1 ölçümü başlamış (Adım 13.2).

## Adil karşılaştırma ilkeleri

- Aynı 25 vaka, aynı kabul edilebilir cevaplar, aynı 0/1/2 puanlama ölçeği.
- Claude'a Gemini'ye giden şeyin aynısını verin: SKILL.md (ya da yüklü Skill) ve veri.json.
- Tek bir Claude modeli seçin (Sonnet ya da Haiku) ve 25 vakanın hepsinde aynısını kullanın. Model adını CSV'ye yazın.
- Mümkünse puanı, hangi modelin yanıtı olduğunu bilmeyen biri versin; alan doğruluğunu Hüseyin Özen kontrol eder.
- Claude ölçümü Skill v1 ile yapılır; v2 yalnızca Gemini tarafında denenir. Bunu docs/karsilastirma.md'de belirtin.

## Adımlar

1. claude.ai'de yeni sohbet açın; model olarak seçtiğiniz Sonnet ya da Haiku'yu seçin.
2. Skill'i Customize > Skills'ten yüklediyseniz etkin olsun; yüklemediyseniz SKILL.md dosyasını sohbete ekleyin.
3. src/data/veri.json dosyasını sohbete ekleyin.
4. İlk mesaj olarak aşağıdaki metni gönderin.
5. Her vakayı ayrı bir mesajla sorun. Yanıtın bittiği ana kadar geçen süreyi kronometreyle saniye olarak not edin (Enter'a bastığınız andan son kelimeye kadar).
6. Her yanıtı puanlayın: 2 = doğru ve kurallara uygun, 1 = kısmen, 0 = yanlış veya kural dışı.
7. Sonuçları claude_olcum.csv dosyasına yazın; bittiğinde claude_model, claude_puan, claude_sure_sn ve not sütunlarını docs/karsilastirma.csv'deki aynı "no" satırlarına taşıyın.
8. Claude'un limitine takılırsanız vakaları takım içinde paylaştırın; kimin hangi vakayı ölçtüğünü not sütununa yazın.

## İlk mesaj (olduğu gibi yapıştırın)

```
Bu sohbette Alanya turizm rehberi ve otel yorum panosu asistanısın. Yanıt kuralların ekteki SKILL.md dosyasında, bilgi kaynağın ekteki veri.json dosyasıdır. Yalnızca bu dosyalara dayan. Her mesajımı önceki mesajlardan bağımsız, yeni bir soru olarak yanıtla ve önceki sorulara atıfta bulunma. İlk soruyu bekle.
```

## Dikkat

- Tek sohbette 25 vaka sorarsanız önceki mesajlar sonrakini etkileyebilir. Bu bir sınırlılıktır; ölçüm özetine yazın. Daha temiz sonuç için vakaları birkaç ayrı sohbete bölün ve her sohbette ilk mesajı tekrarlayın.
- Süre, internet hızı ve claude.ai'nin o anki yoğunluğuna bağlıdır; Gemini süreleriyle yaklaşık karşılaştırma yapıldığını yazın.
- Gerçek kişi ya da müşteri verisi kullanmayın; tüm veri sentetiktir.
