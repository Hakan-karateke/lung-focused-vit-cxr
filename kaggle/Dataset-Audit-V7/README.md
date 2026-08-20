# Veri Kümesi Bütünlük Denetimi

`dataset-integrity-audit.ipynb` — **GPU gerekmez, ~6 dakika.**

## Bu neden isteğe bağlı değil

Kullanılan `chest-xray-pneumonia-balanced-dataset` sürümünde:

| Sınıf | Kermany özgün | Kullanılan | Oran |
|---|---|---|---|
| PNEUMONIA | 4.273 | 4.265 | **1,00×** |
| NORMAL | 1.583 | 4.265 | **2,69×** |

PNEUMONIA neredeyse birebir aynı, **NORMAL'e 2.682 görüntü eklenmiş**. İki olasılık var
ve ikisi de makaleyi doğrudan etkiler:

**(i) Çoğaltma/artırma kopyaları** → aynı hasta hem eğitimde hem testte olabilir.
Bizim sızıntı denetimimiz *dosya adı + boyut* imzasına dayanıyordu; bu, yeniden kodlanmış
veya döndürülmüş kopyaları **yakalayamaz**. İç test AUC'si (0,998) şişkin olabilir.

**(ii) Başka bir kaynaktan eklenmiş** → "NORMAL vs PNEUMONIA" kısmen "kaynak A vs
kaynak B" demektir. Bu, A kolunun akciğere hiç bakmadan (LFR 0,005) %99,8 AUC üretmesini
de açıklar — model patolojiyi değil, çekim kaynağını okuyor olur.

Hakem bu soruyu soracaktır. Yanıtı yayından **önce** bilinmeli.

## Denetlenenler

| # | Denetim | Ortaya çıkardığı |
|---|---|---|
| 1 | Dosya adı şeması | Kermany kalıbına uymayan adlar → yabancı kaynak |
| 2 | Hasta kimliği | `person123_*`, `IM-####-*` kalıplarından |
| 3 | **Hasta düzeyi sızıntı** | Aynı hasta birden çok bölmede mi |
| 4 | Birebir kopya | İçerik MD5 |
| 5 | Yakın kopya | dHash Hamming ≤ 3 → çoğaltma izi |
| 6 | Çözünürlük dağılımı | Sınıfa göre kümelenme → kaynak farkı |

Bölme, ablasyondaki kodun birebir aynısıyla yeniden üretilir ve imzalar denetlenir.

## Girdi

Yalnızca `yusufmurtaza01/chest-xray-pneumonia-balanced-dataset`.
Accelerator **None** seçilebilir.

## Çıktılar

`audit_summary.json` · `audit_files.csv` · `audit_near_duplicates.csv` ·
`audit_fig_01_geometry.png`

Notebook sonunda bulguları listeleyip makalenin **Kısıtlar** bölümünde ne yazılması
gerektiğini söyler. Sorun çıkmazsa da değerli: *"Bölmeler hasta düzeyinde ve algısal
karma ile sızıntı açısından denetlenmiştir"* cümlesi metodolojiyi güçlendirir.
