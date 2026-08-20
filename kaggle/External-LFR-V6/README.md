# Dış Kümelerde Akciğer-Odak Oranı

`external-lfr-analysis.ipynb` — **eğitim yok, ~12 dakika.**

## Neden

LFR şimdiye kadar yalnızca **iç** test kümesinde ölçüldü (A 0,005 · B 0,111 · C 0,909).
Makalenin ana iddiası bu farka dayandığı için, örüntünün eğitim dağıtımına özgü
olmadığını göstermek zorunlu. Ayrıca C kolunun yüksek oranı kısmen tasarım gereği —
yetişkin görüntülerde segmentasyon zorlanırsa bu garanti zayıflar.

## Girdiler

| # | Sekme | Kimlik |
|---|---|---|
| 1 | **Notebooks** | `segmentation-ablation-lung-focused-vit` |
| 2 | Competitions | `rsna-pneumonia-detection-challenge` |
| 3 | Datasets | `nih-chest-xrays/data` |

1. girdi hem kontrol noktalarını hem de iç LFR değerlerini birlikte getirir.
Eğitim veri kümesine gerek yok. GPU + Internet açık.

## Ölçülenler

1. Kol × küme LFR dağılımları (iç test değerleriyle yan yana)
2. **Eşleştirilmiş Wilcoxon** — aynı görüntü üç koldan geçtiği için doğru test bu
3. Toplu dikkat haritaları (kol × küme ızgarası, akciğer konturu bindirilmiş)
4. LFR ↔ doğruluk ilişkisi
5. **Maske alanı denetimi** — ianpan yetişkinde makul maske üretiyor mu

## Yorum anahtarı

A kolunun LFR'si, aynı kümedeki **ortalama maske alanıyla** karşılaştırılmalı:

- LFR ≈ maske alanı → dikkat esasen rastgele dağılmış
- LFR ≪ maske alanı → dikkat akciğerden **aktif olarak kaçıyor** (iç testteki bulgu)

Yetişkin göğüs kafesinde akciğer karenin daha büyük bir kısmını kapladığından, A kolunda
sayısal bir yükseliş beklenebilir; önemli olan orandır, mutlak değer değil.

## Çıktılar

`extlfr_per_image.csv` · `extlfr_summary.csv` · `extlfr_wilcoxon.csv` ·
`extlfr_vs_correctness.csv` · `extlfr_mask_area.csv` · `extlfr_aggregate_maps.npz` ·
`extlfr_fig_01_distributions.png` · `extlfr_fig_02_aggregate.png`
