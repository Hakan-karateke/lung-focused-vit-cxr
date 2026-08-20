# Segmentasyon Ablasyonu — Kurulum ve Çalıştırma

`segmentation-ablation-lung-focused-vit.ipynb`

Danışman sorusu: **“Segmentasyon başarıyı artırıyor mu?”**
Bu notebook, aynı bölme / aynı tohum / aynı hiperparametrelerle **üç kolu sıfırdan
eğitip** iç test + RSNA + NIH üçlüsünde karşılaştırarak yanıtlar.

---

## Üç kol

| Kol | Ön-işleme | Neyi izole eder |
|-----|-----------|-----------------|
| **A · `raw`** | Görüntü doğrudan 224² | Segmentasyon yok — taban çizgi |
| **B · `roi`** | Segmentasyon **yalnızca** kırpma kutusu için; piksel silinmez | Kadrajlama etkisi |
| **C · `lung`** | Akciğer dışı silinir + aynı kutuya kırpılır | Önerilen yöntem |

**B ve C birebir aynı kırpma kutusunu kullanır.** Dolayısıyla:

- `B − A` = kadrajlamanın (yakınlaştırmanın) katkısı
- `C − B` = **maskelemenin** katkısı ← asıl sorulan bu
- `C − A` = yöntemin toplam katkısı

Üçüncü kol olmadan “segmentasyon işe yarıyor” iddiası, kazancın sadece
yakınlaştırmadan gelme olasılığını dışlayamaz. Hakemin ilk soracağı budur.

---

## Kaggle kurulumu

**Add Input** ile eklenecekler:

1. **Chest X-Ray Pneumonia (Balanced)** — eğitim kümesi (`train/`, `val/`, `test/` ve
   içlerinde `NORMAL/`, `PNEUMONIA/`)
2. **RSNA Pneumonia Detection Challenge** — *Competitions* sekmesinden
3. **NIH Chest X-rays** — *Datasets* sekmesinden (`nih-chest-xrays/data`)

**Ayarlar**

- Accelerator: **GPU T4 ×2** veya **P100**
- Internet: **On** (segmentasyon modeli HuggingFace’ten iner)
- Persistence: kapalı kalabilir

Yollar elle girilmez; notebook `/kaggle/input` altını tarayarak üç girdiyi de kendisi bulur.

---

## Çalıştırma süresi

| Aşama | Süre (T4) |
|---|---|
| Çevrimdışı ön-işleme (8.528 görüntü × 3 kol) | ~15 dk |
| Eğitim (3 kol × 15 epoch) | ~3–3,5 sa |
| Dış doğrulama (1.600 görüntü × 3 kol) | ~12 dk |
| İstatistik + figürler | ~2 dk |
| **Toplam** | **≈ 4 sa** |

Tek bir Kaggle oturumuna sığar (sınır 12 sa).

### Önce hattı doğrula

İlk hücrede `QUICK_TEST = True` yapın:

- bölmeler 240 görüntüye indirgenir, 2 epoch, sınıf başına 60 dış görüntü
- tüm akış uçtan uca **~8–10 dakikada** çalışır
- ayrı bir önbellek kökü kullanılır, tam koşumun önbelleğine karışmaz

Akış temiz çalıştıktan sonra `False` yapıp tam koşumu başlatın.

---

## Ayarlar (ilk kod hücresi)

| Değişken | Varsayılan | Açıklama |
|---|---|---|
| `QUICK_TEST` | `False` | Hat doğrulama koşusu |
| `EPOCHS` | `15` | Kol başına epoch |
| `MAX_PER_CLASS_EXT` | `400` | Dış setlerden sınıf başına görüntü |
| `ARMS` | `["raw","roi","lung"]` | Süre darsa `roi` çıkarılabilir (bu durumda B/C ayrımı kaybolur) |
| `SAVE_CHECKPOINTS` | `True` | 3 × 343 MB çıktı |
| `CONFIG["raw_mode"]` | `"resize"` | Taban çizgi tam görüş alanı. `"centercrop"` = 256→224 merkez kırpım |

---

## Üretilen çıktılar

| Dosya | İçerik |
|---|---|
| `ablation_metrics.csv` | Küme × kol × tüm metrikler |
| `ablation_pairwise_tests.csv` | ΔAUC, bootstrap GA, DeLong z/p, McNemar |
| `ablation_auc_ci.csv` | Kol başına AUC %95 güven aralığı |
| `ablation_predictions.npz` | Ham olasılıklar — figürler yeniden üretilebilir |
| `ablation_summary.json` | Bölme imzaları, config, en iyi Val F1, LFR |
| `ablation_vit_{raw,roi,lung}.pth` | Üç kontrol noktası |
| `abl_fig_01…06.png` | Önizleme, eğitim, AUC, ROC, etki büyüklüğü, LFR |

---

## Doğrulanmış noktalar

- **Bölme birebir yeniden üretilir.** Önceki çalışmadaki `random` çağrı sırası korunur;
  her bölmenin MD5 imzası yazdırılır — koşumlar arasında aynı çıkmalıdır.
- **DeLong uygulaması test edildi.** Sentetik veride AUC değerleri `sklearn` ile birebir;
  DeLong standart hatası 3.000 tekrarlı eşleştirilmiş bootstrap standart sapmasıyla
  dört basamak eşleşiyor (oran 1.000).
- **Kollar özdeş başlar.** Her kolun eğitimi öncesi tüm tohumlar sıfırlanır; veri
  yükleyicinin karıştırma üreteci sabit tohumla kurulur. Kollar aynı ağırlık başlangıcını,
  aynı yığın sırasını ve aynı artırma rastgeleliğini paylaşır.
- **Palet CVD-güvenli.** Üç kol rengi doğrulayıcıdan geçirildi; tüm çubuklar ayrıca
  doğrudan değer etiketi taşır, kimlik renge bağlı değildir.
- **Önbellek `/kaggle/temp`** altına yazılır — çıktı anlığına 25.000 dosya girmez.

## Bilinen kısıtlar

- **Tek tohum.** Her kol bir kez eğitilir. Eğitim rastgeleliğini ayrıştırmak için ideal
  olan 3–5 tohumla tekrardır; süre tohum sayısıyla çarpılır.
- **Çoklu karşılaştırma.** Küme başına üç eşleştirilmiş test yapılır. Makalede birincil
  hipotez (`C − A`, dış doğrulamada) önceden belirtilmeli, diğerleri keşifsel sunulmalı
  ya da Holm düzeltmesi uygulanmalıdır.
- **GPU determinizmi.** `cudnn.benchmark` kapalı ve tohumlar sabit; yine de bit düzeyinde
  aynılık garanti değildir. Kalan değişkenlik bootstrap aralıklarının içindedir.
