# Karar tablosu

> **TASLAK:** Aşağıdaki 5 satır, Skill v1 yazılmadan önce Gemini'de en sık beklenen sorunlara göre hazırlanmış bir başlangıçtır. Adım 12.1 uygulamayı 15 dakika kullanarak memnun olmadığınız **gerçek** 5 yanıtı seçmenizi ister. Uygulamayı kullanınca "Memnun olunmayan yanıt" ve "Sonuç" sütunlarını gerçek yanıtlarla değiştirin; teşhis ve çözüm sütunlarını gözleminize göre düzeltin.

| # | Memnun olunmayan yanıt | Teşhis (bilgi / biçim / davranış / maliyet) | Çözüm (veri / Skill / kod) | Sonuç |
| --- | --- | --- | --- | --- |
| 1 | "Alanya Kalesi'nin giriş ücreti ne kadar?" sorusuna kartta olmayan bir fiyat söylüyor | Davranış (kartta olmayan bilgiyi uyduruyor) | Skill: "Kartta olmayan mekan, fiyat veya açılış saati uydurma; 'Bu bilgi uygulamada yok' de" kuralı | 13. haftada vaka 13 ile ölçülecek |
| 2 | Kısa bir mekan sorusuna uzun, çok paragraflı yanıt veriyor | Biçim (çok uzun) | Skill: "En fazla 6 cümle yaz" kuralı | 13. haftada tüm normal vakalarda ölçülecek |
| 3 | İngilizce veya Almanca soruya Türkçe yanıt veriyor | Davranış (dil kuralına uymuyor) | Skill: "Soru hangi dilde geldiyse o dilde yanıt ver" kuralı ve bir örnek | 13. haftada vaka 14 ve 15 ile ölçülecek |
| 4 | Rotada 5'ten fazla durak sıralıyor veya kartta olmayan mekan ekliyor | Davranış (kural dışı) ve bilgi (veride olmayan mekan) | Skill: "Rota en fazla 5 duraktır; her durakta kartın adını yaz" kuralı; kart sayısı 30'a tamamlanır | 13. haftada vaka 1, 3, 16 ve 22 ile ölçülecek |
| 5 | Yorum sınıflandırmasında JSON'un yanına açıklama cümlesi ekliyor veya ironik yorumu olumlu sayıyor | Biçim (JSON dışı metin) ve davranış (ironiyi kaçırıyor) | Skill: "yalnızca JSON döndür" kuralı ve ironik bir örnek; ayrıştırılamayan yanıtlar ölçüm tablosuna sayılır | 13. haftada vaka 9–12, 18 ve 23 ile ölçülecek |

**İnce ayar gerekli mi?** Hayır.

**Gerekçe:** Beş sorunun hiçbiri modelin temel yeteneğinden gelmiyor: ikisi bilgi eksikliği (kartlarda olmayan veri), üçü davranış ve biçim kuralı (uzunluk, dil, JSON). Bunlar Skill kuralı, örnek ve veri ekleyerek çözülür. İnce ayar, ücretsiz katmanda ek maliyet ve zaman getirir; ölçülebilir bir kazanç göstermeden gerekçesi olmaz. Karar, 13. haftadaki 25 vakalık ölçümle doğrulanacak; ölçüm Skill ile giderilemeyen bir sorun gösterirse bu karar yeniden değerlendirilir.
