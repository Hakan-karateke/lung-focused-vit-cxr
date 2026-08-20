# Oklüzyon (Bölge Kapatma) Testi

`occlusion-causal-test.ipynb` — **eğitim yok, ~15 dakika.**

## Neden

Dikkat analizi, segmentasyonsuz modelin akciğerle örtüşmesinin **şans düzeyinin
22 katı altında** olduğunu gösterdi (LFR 0,011 · ortalama maske alanı 0,236). Ama
dikkat haritaları **korelasyoneldir** — modelin bir bölgeye bakması, kararını oraya
dayandırdığını kanıtlamaz.

Bu notebook nedensel testi yapar: bir bölge kapatılır, başarım düşüşü ölçülür.

## Tasarımın kilit noktası: alan eşleşmeli kontrol

Herhangi bir bölgeyi kapatmak girdi dağılımını bozar ve zaten bir miktar düşüş yaratır.
Bu yüzden her hedefli oklüzyona **aynı alanı kaplayan rastgele bir dikdörtgen kontrolü**
eşlik eder:

```
net etki = ΔAUC(hedef bölge) − ΔAUC(alan eşleşmeli rastgele)
```

Net etki ≈ 0 ise o bölge, rastgele bir bölgeden fazla rol oynamıyor demektir.

## 11 koşul

| Koşul | Alan | Kontrolü |
|---|---|---|
| `baseline` | — | — |
| **`lungs`** | maskeye göre (~%25) | `rand_lungs` (görüntü başına eşleşir) |
| `non_lungs` | tümleyen | — |
| `corners` | %19,1 | `rand_20` |
| `border` | %29,6 | `rand_30` |
| `subdiaphragm` | %28,1 | `rand_30` |
| `upper` | %20,1 | `rand_20` |
| `center` | %19,6 | `rand_20` |

Kapatılan bölge veri kümesi ortalama grisiyle (122) doldurulur — maskeleme hattındaki
dolgu değeriyle aynı.

## Otomatik tutarlılık denetimi

Notebook iki beklentiyi kendisi sınar:

- **C kolunda `non_lungs` etkisiz olmalı** (o bölge zaten gri dolu)
- **C kolunda `lungs` yıkıcı olmalı** (tüm bilgi silinir)

İkisi tutmuyorsa uyarı verir; sonuçları yorumlamadan önce bakılmalıdır.

## Girdiler

| # | Sekme | Kimlik |
|---|---|---|
| 1 | Datasets | `yusufmurtaza01/chest-xray-pneumonia-balanced-dataset` |
| 2 | **Notebooks** | `segmentation-ablation-lung-focused-vit` |
| 3 | Competitions | `rsna-pneumonia-detection-challenge` |
| 4 | Datasets | `nih-chest-xrays/data` |

GPU + Internet açık. Kümeler: iç test (864) + RSNA (500) + NIH (500) = 1.864 görüntü
× 11 koşul × 3 kol ≈ 61.500 ileri geçiş.

## Beklenen bulgu

**A kolu:** `lungs` net etkisi ≈ 0 (akciğeri silmek zarar vermiyor),
`corners` / `border` / `subdiaphragm` net etkisi > 0.

**C kolu:** tam tersi.

Bu, korelasyonel gözlemi nedensel iddiaya çevirir:
*"Model akciğere bakmıyor"* → *"Akciğeri tamamen silmek başarımı düşürmüyor."*

**Net etki her yerde ≈ 0 çıkarsa** model bilgiyi geniş biçimde dağıtmış demektir;
o durumda oklüzyon ayrım üretmez ve makalede yalnızca LFR kanıtı kullanılır —
negatif sonuç da dürüstçe raporlanır.

## Çıktılar

`occlusion_results.csv` · `occlusion_predictions.npz` · `occlusion_summary.json` ·
`occ_fig_00_conditions.png` (koşulların görseli) · `occ_fig_01_net_effect.png`

## Kısıtlar

1. **Oklüzyon dağıtım dışı girdi üretir.** Gri dolgu modelin eğitimde gördüğü bir örüntü
   değildir (C kolu hariç). Alan eşleşmeli kontroller bunu büyük ölçüde giderir, tamamen
   değil.
2. **Bölgeler geometriktir**, anatomik değil — `subdiaphragm` bandı gerçek diyafram
   düzeyiyle birebir örtüşmeyebilir. Akciğer maskesi ise anatomiktir.
3. **Tek eğitim tohumu.** Etki büyüklükleri tohuma göre oynayabilir; beklenen örüntü
   (net etki ≈ 0 ↔ > 0) niteliksel bir ayrımdır.
