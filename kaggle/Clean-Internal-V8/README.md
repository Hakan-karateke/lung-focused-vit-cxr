# Sızıntısız İç Test

`clean-internal-test.ipynb` — **eğitim yok, ~8 dakika.**

## Neden

Bütünlük denetimi, kullanılan "dengelenmiş" kümede NORMAL sınıfının **1.575 kaynak
görüntüden augmentasyonla 4.265 dosyaya** çıkarıldığını gösterdi. Sonuç: test
bölmesindeki NORMAL görüntülerin **%86,6'sı eğitimdeki bir görüntünün kopyası**;
PNEUMONIA'da tek kopya yok — sızıntı **sınıfa göre asimetrik**.

Bu koşulda "NORMAL'i ezberle, tanımadığına PNEUMONIA de" stratejisi yüksek iç başarım
üretir. Nitekim dış kümelerde duyarlılık 0,97 iken özgüllük 0,58'e düşüyor.

Bu notebook, aynı kontrol noktalarını **eğitimle hiçbir kaynak görüntüyü paylaşmayan**
alt kümede yeniden değerlendirir.

## Girdiler

| # | Sekme | Kimlik |
|---|---|---|
| 1 | Datasets | `yusufmurtaza01/chest-xray-pneumonia-balanced-dataset` |
| 2 | **Notebooks** | `segmentation-ablation-lung-focused-vit` |

GPU + Internet açık.

## Alt kümeler

| Alt küme | Tanım | N |
|---|---|---|
| Orijinal test | Ablasyondaki test bölmesi (sızıntılı) | 864 (432/432) |
| Yalnızca sızıntılı NORMAL | Negatifler eğitim kopyası | 1.615 |
| Kaynak düzeyi temiz | `_aug_` eki soyulmuş kök eğitimde yok | 949 (85/864) |
| **Hasta düzeyi temiz** | Hasta anahtarı eğitimde yok — **birincil** | 178 (40/138) |

Aynı kökten birden çok dosya varsa yalnızca biri tutulur (augmente edilmemiş tercih
edilir) — yerel doğrulama: temiz NORMAL'lerin **0'ı** augmente.

## Yöntem notları

- **Birincil ölçüt ROC-AUC**, sınıf oranından bağımsız olduğu için dengesiz alt kümede
  doğrudan hesaplanır.
- **Eşiğe bağlı ölçütler** (doğruluk, F1, özgüllük) denge gerektirir; çok olan sınıftan
  200 tekrarlı çekilişle dengelenip ortalama ± ss verilir — tek çekilişin şansına
  bağlı kalınmaz.
- **Sızıntının katkısı doğrudan ölçülür:** pozitif küme (PNEUMONIA) sabit tutulup
  negatif küme sızıntılı ↔ temiz olarak değiştirilir. Aradaki AUC farkı, sızıntının
  başarıma katkısıdır.
- **Ezberleme izi:** NORMAL görüntülerde P(pnömoni) dağılımı sızıntılı ve temiz gruplar
  için ayrı çizilir. Sızıntılılar 0'a yapışık, temizler sağa yayılmışsa model o
  görüntüleri tanıyor demektir.

Bölme, ablasyondaki kodun birebir aynısıyla yeniden üretilir ve MD5 imzaları
`assert` ile denetlenir (yerel olarak doğrulandı: üçü de eşleşiyor).

## Çıktılar

`clean_internal_metrics.csv` · `clean_leakage_effect.csv` · `clean_per_image.csv` ·
`clean_internal_summary.json` · `clean_fig_01_auc.png` · `clean_fig_02_prob_dist.png`

## Kısıtlar (makalede belirtilecek)

1. **Örneklem küçük** — hasta düzeyinde sınıf başına ~40; güven aralıkları geniş.
   Veri kümesinin yapısından kaynaklanıyor, tasarım tercihi değil.
2. **Modeller yine sızıntılı veriyle eğitildi.** Bu, temiz bir *test* sağlar, temiz bir
   *eğitim* değil. NORMAL'in efektif eğitim büyüklüğü 3.400 değil ~1.244 özgün görüntü.
3. **Hasta anahtarı dosya adından çıkarıldı.** Gerçek hasta kimlikleri yayımlanmadığı
   için bu bir üst sınır tahminidir.

> Bu kısıtlar sonucu geçersiz kılmaz; iç test sayısının neden **birincil kanıt olarak
> kullanılmaması** gerektiğini gösterir. Çalışmanın tüm ana iddiaları bağımsız dış
> kümelerde ölçülmüştür ve sızıntıdan etkilenmez.
