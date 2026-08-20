# (b) Çoklu Tohumla Gürültü Tabanının Ölçülmesi

`multi-seed-ablation.ipynb` — **~7 saat** (2 yeni tohum × 3 kol).

## Neden

Ablasyonda C − A = +0,010 bulundu. Aynı yapılandırmanın iki bağımsız koşumu arasındaki
fark ise **0,0036** ölçüldü (V2 tek-kollu koşum: RSNA 0,9300; ablasyon `lung` kolu: 0,9264).
Yani gürültü, aranan etkinin **~%35'i**. Tek tohumla bu soru kapanmaz.

Bu notebook, **kol-içi değişkenliği** (aynı kol, farklı tohum) ile **kollar arası farkı**
aynı ölçekte karşılaştırır.

## Tasarımdaki kilit nokta: hangi tohum sabit

| | Tohum | Neden |
|---|---|---|
| Veri bölmesi | **42, sabit** | Değişirse her koşum farklı train/val/test görür — karşılaştırma çöker |
| Dış örneklem | **42, sabit** | Aynı RSNA/NIH görüntüleri değerlendirilmeli |
| Eğitim (ağırlık başlangıcı, yığın sırası, artırma) | **değişken** | Ölçmek istediğimiz belirsizlik bu |

Bölme, ablasyon koşumunun yazdırdığı **MD5 imzalarıyla otomatik denetlenir**
(`train ccf23597ec992137`, `val 779ac7f6455a7ac8`, `test 3a25cbb40ab471d7`).
İmza tutmazsa notebook `assert` ile durur.

## Eklenecek girdiler

| # | Sekme | Kimlik | Zorunlu |
|---|---|---|---|
| 1 | Datasets | `yusufmurtaza01/chest-xray-pneumonia-balanced-dataset` | evet |
| 2 | Competitions | `rsna-pneumonia-detection-challenge` | evet |
| 3 | Datasets | `nih-chest-xrays/data` | evet |
| 4 | Datasets | *(kendi yükleyeceğin)* `ablation_predictions.npz` | opsiyonel |

**4. girdi**: ablasyon çıktısındaki `ablation_predictions.zip`/`.npz` dosyasını dataset
olarak eklersen tohum 42 sonuçları birleştirilir ve analiz **3 tohumla** yapılır.
Eklemezsen 2 tohumla devam eder (gürültü tahmini zayıflar). Eklemen önerilir.

## Ayarlar

| Değişken | Varsayılan | Not |
|---|---|---|
| `SPLIT_SEED` | `42` | **Değiştirme** |
| `TRAIN_SEEDS` | `[1337, 2024]` | Yeni eğitim tohumları |
| `ARMS` | `["raw","roi","lung"]` | Süre riskliyse `["raw","lung"]` → ~4,5 sa |
| `SAVE_CHECKPOINTS` | `False` | Açarsan 6 × 343 MB |

Süre darsa önce `QUICK_TEST = True` ile hattı doğrula (~10 dk; imza denetimi atlanır).

## Ne raporlanacak

1. **Gürültü tabanı** — kol başına tohumlar arası AUC standart sapması
2. **Tohum-eşleştirilmiş fark** — her tohumda C − A, sonra ortalama ± ss
3. **etki/gürültü oranı** — 1'in altındaysa fark eğitim rastgeleliğinden ayırt edilemez
4. **Tohum topluluğu** — olasılık ortalaması; eğitim gürültüsünü giderir, topluluklar
   arası DeLong testi ön-işleme etkisini en temiz haliyle verir

## Çıktılar

`seed_auc_by_seed.csv` · `seed_noise_floor.csv` · `seed_effect_vs_noise.csv` ·
`seed_ensemble_metrics.csv` · `seed_ensemble_tests.csv` · `seed_predictions.npz` ·
`seed_summary.json` · `seed_fig_01_scatter.png` · `seed_fig_02_effect_vs_noise.png`

## Makale için

Yöntem bölümünde tek cümle yeter:
*"Her kol N bağımsız eğitim tohumuyla eğitilmiş, sonuçlar ortalama ± standart sapma
olarak verilmiş, kollar arası farklar tohum-eşleştirilmiş olarak hesaplanmıştır."*
Bu, hakemin "tek koşum mu?" itirazını baştan kapatır.
