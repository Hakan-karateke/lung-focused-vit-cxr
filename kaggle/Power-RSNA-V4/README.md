# (a) Dış Doğrulama Örnekleminin Büyütülmesi

`external-power-boost.ipynb` — **eğitim yok, yalnızca çıkarım. ~15 dakika.**

## Neden

Ablasyonda RSNA'da C − A = **+0,0102** bulundu (SE 0,0077, DeLong p = 0,19).
Bu etki gerçekse p < 0,05'e ulaşmak için gereken örneklem ≈ **1.770** görüntü.
Mevcut 800 yetersizdi — yani "fark yok" değil, "bilmiyoruz" durumundaydık.

Bu notebook örneklemi sınıf başına 400 → **1000**'e çıkarır (NIH'de havuz ne kadar
izin veriyorsa). AUC'nin beklenen değeri değişmez, yalnızca **standart hatası küçülür**.

## Eklenecek girdiler

| # | Sekme | Kimlik |
|---|---|---|
| 1 | Datasets | *(kendi yükleyeceğin)* ablasyon kontrol noktaları |
| 2 | Competitions | `rsna-pneumonia-detection-challenge` |
| 3 | Datasets | `nih-chest-xrays/data` |

**Kontrol noktalarını yüklemek için:** ablasyon koşumunun Output sekmesinden
`ablation_vit_raw.pth`, `ablation_vit_roi.pth`, `ablation_vit_lung.pth` dosyalarını
indir → *New Dataset* → ad: `ablation-vit-checkpoints`.

Eğitim veri kümesine **gerek yok** — hiçbir şey eğitilmiyor.
Ayarlar: GPU açık, Internet açık.

## Tasarımdaki kilit nokta: üst küme

Örneklem eskisinin **üst kümesidir**. Aynı tohumla karıştırılıp dilim `[:400]` yerine
`[:1000]` alındığı için yeni örneklemin ilk 400 görüntüsü eskisiyle birebir aynıdır.
Bu iki şeyi sağlar:

1. **İç tutarlılık denetimi** — notebook ilk 400 alt kümesinde AUC'yi yeniden hesaplar
   ve önceki koşumun değerleriyle karşılaştırır (RSNA 0,9163 / 0,9182 / 0,9264).
   Fark |0,002|'yi aşarsa hat bozuk demektir ve uyarı verir.
2. Büyütme örneklem *değiştirmez*, yalnızca **ekler** — farkın yönü seçimden gelemez.

## Çıktılar

`power_metrics.csv` · `power_pairwise_tests.csv` · `power_auc_ci.csv` ·
`power_predictions.npz` · `power_fig_01_nested.png` (örneklem büyüdükçe AUC eğrisi) ·
`power_fig_02_effect.png` (400 vs büyütülmüş, aralık daralması)

## Sonucu okuma

- **İç tutarlılık denetimi sapma gösteriyorsa** başka hiçbir sayıya bakma.
- **C − A anlamlı çıkarsa:** küçük ama gerçek bir ayrıştırma katkısı var; etki
  büyüklüğüyle (≈ +0,01 AUC) birlikte raporla, "büyük kazanç" deme.
- **Anlamsız kalırsa:** artık *dar* aralıkla "fark yok" denebilir — bu, önceki
  "bilmiyoruz"dan çok daha güçlü bir ifadedir.

> Bu notebook yalnızca **örneklem** belirsizliğini ölçer. Eğitim rastgeleliğinden gelen
> belirsizlik için çoklu tohum notebook'una bak — ikisi birbirinin yerine geçmez.
