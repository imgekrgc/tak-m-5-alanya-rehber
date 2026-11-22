# Pull request adımları (GitHub web arayüzü, Hüseyin Özen)

Repo: `takim-5-alanya-rehber`. Dosya yolu `uygulama/` klasörüne göredir (kılavuz: Adım 10.5).

## 1) veri.json
1. Repoda `uygulama/src/data/` klasörüne gidin (yoksa **Add file > Create new file** ile `uygulama/src/data/veri.json` yazarak oluşturun).
2. Dosyayı açıp `pr-hazir/uygulama/src/data/veri.json` içeriğini yapıştırın (ya da **Add file > Upload files**).
3. Altta **Create a new branch for this commit and start a pull request** seçin. Dal adı: `veri/ilk-10-mekan`. Commit mesajı: `İlk 10 mekan kartı eklendi`.
4. **Propose changes** > **Create pull request**.

## 2) README problem bölümü
1. Repo kökünde `README.md` > kalem simgesi.
2. "Problem ve hedef kullanıcı" bölümüne `1_adim-10.7_problem-tanimi.md` içeriğini yapıştırın (5 cümle + 3 kullanıcı görevi).
3. Dal adı: `readme/problem-tanimi`. **Propose changes** > **Create pull request**.

## PR açıklaması (her iki PR'a yapıştırın, ilgili satırı bırakın)
**Başlık:** İlk 10 mekan kartı (Adım 10.7) / README problem tanımı (Adım 10.7)

- Ne değişti: `uygulama/src/data/veri.json` 10 mekan kartı (id, ad, tur, metin, kaynak) / README'ye 5 cümlelik problem ve 3 kullanıcı görevi
- Mekan kartları kaynak gösterilerek yazıldı; kişisel veri içermez. `yorumlar` listesi şimdilik boş, sentetik yorumlar sonra eklenecek
- Gözden geçiren: @İmge Karaağaç (teknik lider)
