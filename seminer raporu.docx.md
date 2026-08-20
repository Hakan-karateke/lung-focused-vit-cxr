**T.C.**  
**FIRAT ÜNİVERSİTESİ**  
**FEN BİLİMLERİ ENSTİTÜSÜ**  
**YAZILIM MÜHENDİSLİĞİ ANABİLİM DALI**

**GÖĞÜS RADYOGRAFİSİNDE PNÖMONİ SINIFLANDIRMASI İÇİN AKCİĞER-ODAKLI VISION TRANSFORMER: ANATOMİK MASKELEME, KONTROLLÜ ABLASYON VE DIŞ DOĞRULAMA**

**Yüksek Lisans Semineri**

**Hakan KARATEKE**

**ELAZIĞ \- 2026**

**T.C.**  
**FIRAT ÜNİVERSİTESİ**  
**FEN BİLİMLERİ ENSTİTÜSÜ**  
**YAZILIM MÜHENDİSLİĞİ ANABİLİM DALI**

**GÖĞÜS RADYOGRAFİSİNDE PNÖMONİ SINIFLANDIRMASI İÇİN AKCİĞER-ODAKLI VISION TRANSFORMER: ANATOMİK MASKELEME, KONTROLLÜ ABLASYON VE DIŞ DOĞRULAMA**

**Yüksek Lisans Semineri**

**Hakan KARATEKE**

**Danışman: Prof. Dr. Gülşah KARADUMAN**

**ELAZIĞ \- 2026**  
**ÖNSÖZ**

Bu çalışma, derin öğrenme tabanlı tıbbi görüntü sınıflandırıcılarının yüksek doğruluk değerlerinin ardındaki güvenilirlik sorununu konu almakta; özelinde göğüs radyografisinden pnömoni tespitinde modellerin anatomik kısayollara değil, gerçek hastalık bulgularına dayanmasını sağlamayı amaçlamaktadır. Çalışma boyunca, bir modelin yüksek test başarımı göstermesinin tek başına klinik güvenilirlik için yeterli olmadığı; modelin bağımsız veri kümelerinde de tutarlı davranması ve kararını anatomik olarak anlamlı bölgelere dayandırması gerektiği temel ilke olarak benimsenmiştir.

Çalışmanın seyri sırasında, başlangıçta beklenen sonucun aksine, anatomik maskelemenin sınıflandırma başarımını ölçülebilir biçimde artırmadığı; buna karşılık modelin karar dayanağını kökten değiştirdiği saptanmıştır. Bu bulgu, hipotezin bir bölümünü desteklememekle birlikte çalışmanın asıl katkısını oluşturmuş ve raporun çerçevesini belirlemiştir. Negatif sonuçların da dürüstçe raporlanması bilimsel yöntemin gereği sayılmış; bu doğrultuda tüm doğrulama adımları, sonucu destekleyip desteklemediğine bakılmaksızın aktarılmıştır.

Çalışmanın her aşamasında bilgi, deneyim ve yönlendirmeleriyle bana destek olan, akademik bakış açısı kazandıran değerli danışmanım Prof. Dr. Gülşah Karaduman'a en içten teşekkürlerimi sunarım. Ayrıca eğitim sürecim boyunca beni destekleyen aileme ve arkadaşlarıma minnettarım.

**Elazığ, 2026                                                                                     Hakan KARATEKE**  
**ÖZET**

**Yüksek Lisans Semineri**

**GÖĞÜS RADYOGRAFİSİNDE PNÖMONİ SINIFLANDIRMASI İÇİN AKCİĞER-ODAKLI VISION TRANSFORMER: ANATOMİK MASKELEME, KONTROLLÜ ABLASYON VE DIŞ DOĞRULAMA**

Hakan KARATEKE

Göğüs radyografisinde pnömoni sınıflandırması yapan derin öğrenme modelleri yüksek test doğrulukları bildirse de, bu modellerin kararlarını çoğu zaman hastalıkla nedensel ilişkisi olmayan, veri kümesine özgü kısayollara dayandırdığı bilinmektedir. Bu seminer, söz konusu kısayolu cezalandırarak değil, onu besleyen bilgiyi girdi düzeyinde ortadan kaldırarak engelleyen bir sınıflandırma hattı önermekte ve bu hattın katkısını kontrollü bir ablasyonla ölçmektedir. Her radyograf, çok merkezli verilerle eğitilmiş bir segmentasyon modeliyle işlenip yalnızca sağ ve sol akciğer alanları korunarak, ilgi alanına kırpılarak Vision Transformer (ViT-B/16) modeline verilmiştir. Katkıyı ayrıştırmak için üç kol aynı bölme, aynı tohum ve aynı hiperparametrelerle eğitilmiştir: segmentasyonsuz taban çizgi (A), yalnızca ilgi alanı kırpma (B) ve maskeleme ile kırpmanın birlikte uygulandığı önerilen hat (C).

Bulgular üç eksende toplanmaktadır. Birincisi, **anatomik maskeleme ayrıştırma başarımını değiştirmemektedir**: üç kolun ROC-AUC değerleri iç test kümesinde (0,998), RSNA'da (0,914-0,924) ve NIH ChestX-ray14'te (0,695-0,705) istatistiksel olarak ayırt edilemez düzeydedir; tek tohumda gözlenen +0,010'luk fark, üç bağımsız eğitim tohumuyla tekrarlandığında topluluk düzeyinde +0,001'e gerilemiş ve eğitim gürültüsünün içinde kalmıştır. İkincisi, **maskeleme modelin karar dayanağını kökten değiştirmektedir**: segmentasyonsuz modelin dikkatinin akciğer maskesiyle örtüşme oranı bağımsız yetişkin kümelerde 0,011 iken (ortalama akciğer alanı 0,236, yani rastgele dikkatin beklenen değerinin yaklaşık yirmi ikide biri), maskelenmiş modelde 0,951'dir; 1.000 görüntünün tamamında maskelenmiş model daha yüksek örtüşme göstermiştir. Üçüncüsü, bu fark bir dikkat gözleminden ibaret olmayıp **nedenseldir**: her iki akciğer alanı tamamen silindiğinde segmentasyonsuz modelin iç test AUC değeri 0,998'den yalnızca 0,990'a düşmekte, buna karşılık akciğer dışındaki her şey silindiğinde 0,780'e gerilemektedir. Aynı büyüklükte rastgele bir bölgenin silinmesiyle karşılaştırıldığında akciğerin silinmesi ek bir kayıp üretmemektedir.

Ayrıca kullanılan kamuya açık dengelenmiş veri kümesinin bütünlük denetimi yapılmış; NORMAL sınıfının 1.575 kaynak görüntüden augmentasyonla 4.265 dosyaya çıkarıldığı ve test bölmesindeki NORMAL görüntülerin %86,6'sının eğitimdeki bir görüntünün kopyası olduğu saptanmıştır. Hasta düzeyinde ayrık bir alt kümede yapılan yeniden değerlendirme, bu sızıntının başarıma katkısının 0,005 AUC düzeyinde kaldığını göstermiştir. Sonuç olarak, başarım ölçütlerinin modelin klinik olarak anlamlı bölgeyi kullanıp kullanmadığına kör olduğu; güvenilirliğin ayrı bir eksende, dikkat hizalaması ve nedensel bölge analiziyle ölçülmesi gerektiği ortaya konmaktadır.

**Anahtar Kelimeler:** Göğüs radyografisi, pnömoni, Vision Transformer, kısayol öğrenmesi, anatomik segmentasyon, kontrollü ablasyon, dış doğrulama, oklüzyon analizi, veri sızıntısı, model kalibrasyonu  
**İÇİNDEKİLER**

**ÖNSÖZ	i**  
**ÖZET	ii**  
**ÇİZELGELER LİSTESİ	iv**  
**ŞEKİLLER LİSTESİ	v**  
**KISALTMALAR LİSTESİ	vi**  
**1\. GİRİŞ	1**  
1.1. Problem Durumu	1  
1.2. Araştırmanın Amacı	1  
1.3. Araştırmanın Önemi	2  
1.4. Sayıltılar	2  
1.5. Sınırlılıklar	2  
1.6. Tanımlar	3  
**2\. KURAMSAL ÇERÇEVE VE İLGİLİ ARAŞTIRMALAR	4**  
2.1. Göğüs Radyografisinde Derin Öğrenme	4  
2.2. Vision Transformer Mimarisi	4  
2.3. Kısayol Öğrenmesi ve Açıklanabilirlik	4  
2.4. Anatomik Segmentasyon	5  
2.5. Veri Sızıntısı ve Yeniden Üretilebilirlik	5  
2.6. İlgili Araştırmalar	5  
**3\. YÖNTEM	6**  
3.1. Veri Kümesi ve Bütünlük Denetimi	6  
3.2. Anatomik Maskeleme ve İlgi Alanı Çıkarımı	7  
3.3. Akciğer-Odaklı Vision Transformer Mimarisi	8  
3.4. Eğitim Ayrıntıları	9  
3.5. Kontrollü Ablasyon Tasarımı	9  
3.6. Dış Doğrulama Tasarımı	10  
3.7. Eşik Yeniden Kalibrasyonu	10  
3.8. Açıklanabilirlik ve Akciğer-Odak Oranı	11  
3.9. Nedensel Bölge Analizi: Oklüzyon Testi	11  
3.10. İstatistiksel Analiz	12  
**4\. BULGULAR	13**  
4.1. Veri Kümesi Bütünlük Denetimi	13  
4.2. İç Test Başarımı ve Sızıntısız Değerlendirme	14  
4.3. Segmentasyonun Katkısı: Kontrollü Ablasyon	15  
4.4. Örneklem Gücü ve Eğitim Tohumu Değişkenliği	16  
4.5. Dış Doğrulama Sonuçları	17  
4.6. Kalibrasyon Sonrası Başarım	18  
4.7. Akciğer-Odak Oranı	19  
4.8. Nedensel Bölge Analizi Sonuçları	20  
**5\. TARTIŞMA	22**  
**6\. SONUÇ VE ÖNERİLER	24**  
**KAYNAKLAR	25**  
**EKLER	27**  
**ÖZGEÇMİŞ	29**  
**ÇİZELGELER LİSTESİ**

Çizelge 3.1. Kontrollü ablasyonda karşılaştırılan üç kolun tanımı ve izole ettiği etki	9  
Çizelge 3.2. Oklüzyon testinde kullanılan bölgeler ve alan eşleşmeli kontrolleri	12  
Çizelge 4.1. Veri kümesi bütünlük denetimi özeti	13  
Çizelge 4.2. İç test başarımı: sızıntılı ve sızıntısız alt kümelerde ROC-AUC	14  
Çizelge 4.3. Kontrollü ablasyon: kol ve küme bazında ROC-AUC (tek tohum, sınıf başına 400 görüntü)	15  
Çizelge 4.4. Kollar arası eşleştirilmiş karşılaştırmalar (DeLong testi)	16  
Çizelge 4.5. Üç eğitim tohumunda kol içi değişkenlik ve topluluk sonuçları	17  
Çizelge 4.6. Dış doğrulama setlerinde özet başarım ölçütleri (karar eşiği 0,50)	17  
Çizelge 4.7. Eşik yeniden kalibrasyonu öncesi ve sonrası başarım (görülmemiş %50 test yarısı)	18  
Çizelge 4.8. Akciğer-odak oranının kol ve küme bazında dağılımı	19  
Çizelge 4.9. Oklüzyon testi: bölge kapatmanın ROC-AUC üzerindeki etkisi	20  
**ŞEKİLLER LİSTESİ**

Şekil 3.1. Önerilen akciğer-odaklı Vision Transformer çerçevesinin uçtan uca görünümü	6  
Şekil 3.2. Anatomik maskeleme ve ilgi alanı çıkarım algoritmasının adımları	7  
Şekil 3.3. Akciğer-odaklı maskeleme hattının üç aşaması	8  
Şekil 3.4. Aynı radyograftan üretilen üç ablasyon kolunun girdileri	9  
Şekil 3.5. Oklüzyon testinde kullanılan bölge kapatma koşulları	12  
Şekil 4.1. Sızıntılı ve sızıntısız alt kümelerde iç test başarımı	14  
Şekil 4.2. Kontrollü ablasyon: kol başına ROC-AUC ve bootstrap güven aralıkları	15  
Şekil 4.3. Kollar arası AUC farkının etki büyüklüğü	16  
Şekil 4.4. Üç eğitim tohumunda kolların ROC-AUC dağılımı	17  
Şekil 4.5. Dış doğrulama setleri arasında ROC-AUC ile duyarlılık ve özgüllük karşılaştırması	18  
Şekil 4.6. Eşik yeniden kalibrasyonu öncesi ve sonrası güvenilirlik eğrileri	19  
Şekil 4.7. Akciğer-odak oranının kümeler ve kollar arasında dağılımı	19  
Şekil 4.8. Bağımsız kümelerde toplu dikkat haritaları	20  
Şekil 4.9. Bölge kapatmanın nedensel etkisi	21  
**KISALTMALAR LİSTESİ**

**AP**	: Ortalama Kesinlik (Average Precision)

**AUC**	: Eğri Altındaki Alan (Area Under the Curve)

**CNN**	: Evrişimli Sinir Ağı (Convolutional Neural Network)

**ECE**	: Beklenen Kalibrasyon Hatası (Expected Calibration Error)

**F1**	: Kesinlik ve Duyarlılığın Harmonik Ortalaması

**GA**	: Güven Aralığı

**LFR**	: Akciğer-Odak Oranı (Lung-Focus Ratio)

**NIH**	: Amerikan Ulusal Sağlık Enstitüleri

**RoI**	: İlgi Alanı (Region of Interest)

**ROC**	: Alıcı İşletim Karakteristiği

**RRR**	: Doğru Nedenlerle Doğru (Right for the Right Reasons)

**RSNA**	: Kuzey Amerika Radyoloji Derneği

**ViT**	: Görü Dönüştürücüsü (Vision Transformer)

**1\. GİRİŞ**

Bu bölümde araştırmanın problem durumu, amacı, önemi, sayıltıları, sınırlılıkları ve temel tanımları sunulmaktadır. Bölüm, çalışmanın hangi soruna yanıt aradığını ve bu yanıtın neden önemli olduğunu çerçevelemeyi amaçlamaktadır.

**1.1. Problem Durumu**

Göğüs radyografisi, düşük maliyeti ve yaygın erişilebilirliği nedeniyle pnömoni tanısında ilk başvurulan görüntüleme yöntemidir. Pnömoni, akciğer parankiminde konsolidasyon ve infiltrasyon olarak görülür; ancak bu bulguların radyografide saptanması deneyim gerektirir ve gözlemciler arası değişkenlik gösterir. Son yıllarda derin öğrenme tabanlı sınıflandırıcılar bu görevde radyolog düzeyine yakın test başarımları bildirmiştir (Rajpurkar ve diğerleri, 2017).

Ancak yüksek bir test doğruluğu, modelin klinik olarak güvenilir olduğunu tek başına göstermez. Derin ağlar, etiketle nedensel ilişkisi olmayan ancak veri kümesine özgü istatistiksel ipuçlarını öğrenerek doğru sonuca ulaşabilir; bu olgu kısayol öğrenmesi olarak adlandırılır (Geirhos ve diğerleri, 2020). Tıbbi görüntülemede bunun çarpıcı bir örneği, COVID-19 saptadığı düşünülen modellerin aslında görüntü kaynağına ve pozisyonel artefaktlara baktığının gösterilmesidir (DeGrave, Janizek ve Lee, 2021).

Önceki bir denemede, modele akciğer dışına bakmayı yumuşak bir ceza terimiyle yasaklayan yaklaşım (Ross, Hughes ve Doshi-Velez, 2017) kullanılmış; ancak modelin bu cezayı sayısal olarak küçültürken kararını hâlâ akciğerler arası omurga/mediasten ekseninden vermeyi sürdürdüğü gözlenmiştir. Problem iki katmanlıdır. Birinci katman, güçlü bir kısayolun yumuşak bir ceza ile caydırılamamasıdır. İkinci ve daha temel katman ise şudur: **kısayol kullanan bir modelle kullanmayan bir modeli, başarım ölçütleriyle birbirinden ayırmak mümkün değildir.** Bir çalışmanın yalnızca doğruluk, F1 veya AUC raporlaması, modelin kararını nereye dayandırdığı hakkında hiçbir bilgi vermez. Bu rapor, bu ikinci katmanı deneysel olarak göstermeyi amaçlamaktadır.

**1.2. Araştırmanın Amacı**

Bu araştırmanın amacı, kısayol öğrenmesini cezalandırarak değil, onu besleyen bilgiyi girdi düzeyinde ortadan kaldırarak engelleyen bir sınıflandırma hattı tasarlamak; bu hattın katkısını kontrollü bir ablasyonla ölçmek ve gerçek genelleme yeteneğini bağımsız veri kümelerinde sınamaktır. Bu doğrultuda aranan yanıtlar şunlardır:

(i) Akciğer dışı bölgeyi maskeleyerek yalnızca akciğer dokusunu modele vermek sınıflandırma başarımını **artırır mı, korur mu, yoksa düşürür mü**?

(ii) Olası bir başarım farkı, maskelemeden mi yoksa yalnızca ilgi alanına kırpmanın (kadrajlama) etkisinden mi kaynaklanmaktadır?

(iii) Gözlenen fark, eğitim rastgeleliğinden ve örneklem gürültüsünden ayırt edilebilir mi?

(iv) Model, kararını gerçekte hangi görüntü bölgesine dayandırmaktadır; bu bağımlılık nedensel olarak gösterilebilir mi?

(v) Bu hat, eğitiminden bağımsız bir veri kümesinde genelleşir mi ve dağıtım kayması altında ortaya çıkan kalibrasyon bozulması yeniden kalibrasyonla giderilebilir mi?

**1.3. Araştırmanın Önemi**

Çalışma, tıbbi yapay zekâda giderek önem kazanan güvenilirlik ve genellenebilirlik tartışmasına dört yönlü katkı sunmaktadır. Birincisi, kısayoldan arındırmayı bir ceza terimine değil doğrudan veri hattının yapısına gömmesi yönüyle özgündür. İkincisi, bu müdahalenin katkısını üç kollu kontrollü bir ablasyonla, çoklu tohum ve örneklem gücü analizleriyle birlikte ölçerek tek koşumluk iyileşme iddialarının ötesine geçmektedir. Üçüncüsü, dikkat temelli korelasyonel gözlemi oklüzyon temelli nedensel bir teste bağlamaktadır. Dördüncüsü, yaygın kullanılan kamuya açık bir veri kümesindeki sistematik sızıntıyı belgeleyip etkisini niceliksel olarak ölçmekte; böylece aynı kümeyi kullanan çalışmalara doğrudan katkı sağlamaktadır.

**1.4. Sayıltılar**

Araştırmada şu sayıltılar kabul edilmiştir: kullanılan segmentasyon modeli akciğer alanlarını klinik olarak yeterli doğrulukta sınırlandırmaktadır (bu sayıltı §4.7'de maske alanı denetimiyle ampirik olarak sınanmıştır); dış doğrulama kümelerindeki sınıf etiketleri, etiket gürültüsü payı dikkate alınmak kaydıyla başarım ölçümü için yeterince güvenilirdir; pediatrik veride eğitilen modelin yetişkin verisinde sınanması geçerli bir dağıtım kayması senaryosu oluşturmaktadır; ve dosya adlarından çıkarılan hasta anahtarları, gerçek hasta kimlikleri yayımlanmadığından, hasta düzeyi ayrıklık için bir üst sınır tahmini vermektedir.

**1.5. Sınırlılıklar**

Çalışma, retrospektif ve vekil (proxy) etiketli bir dış doğrulamayla sınırlıdır; prospektif veri ve uzman radyolog mutabakat etiketleri kapsam dışındadır. Eğitim verisi pediatrik, dış doğrulama verisi yetişkindir. Akciğer dışı bağlam (kardiyotorasik oran, mediastinal genişlik) kasıtlı olarak atıldığından yöntem tam bir radyolojik okuma değildir.

Kullanılan eğitim kümesi, özgün Kermany kümesinin NORMAL sınıfı augmentasyonla çoğaltılarak dengelenmiş bir türevidir; bu nedenle NORMAL sınıfının efektif özgün büyüklüğü raporlanan dosya sayısından belirgin biçimde küçüktür (§4.1). Hasta düzeyinde ayrık iç test alt kümesi sınıf başına yaklaşık 40 görüntüyle sınırlı kalmış, güven aralıkları geniş çıkmıştır. Ablasyon kolları üç eğitim tohumuyla tekrarlanmış olup daha fazla tohum kestirimi iyileştirecektir. Oklüzyon testinde bölge kapatma dağıtım dışı girdi ürettiğinden alan eşleşmeli rastgele kontroller kullanılmış, ancak bu etki tamamen giderilememiştir. Son olarak yalnızca tek bir mimari (ViT-B/16) ile çalışılmıştır.

**1.6. Tanımlar**

Pnömoni: Akciğer parankiminde konsolidasyon ve infiltrasyonla seyreden enfeksiyöz akciğer iltihabı.  
Kısayol öğrenmesi: Modelin amaçlanan özelliği değil, eğitim dağıtımında onunla bağıntılı kolay bir vekil özelliği öğrenmesi.  
Vision Transformer (ViT): Görüntüyü sabit boyutlu yamalara bölerek öz-dikkat mekanizmasıyla işleyen derin öğrenme mimarisi.  
Anatomik segmentasyon: Bir görüntüdeki anatomik yapıların (akciğer, kalp) piksel düzeyinde sınırlandırılması.  
Kontrollü ablasyon: Bir yöntemin bileşenlerinin tek tek çıkarılarak, diğer tüm koşullar sabit tutulmak suretiyle her bileşenin katkısının ayrı ayrı ölçülmesi.  
Dış doğrulama: Modelin, eğitildiği veri dağıtımından bağımsız bir kaynaktan gelen veriyle sınanması.  
Dağıtım kayması: Eğitim ve uygulama verilerinin istatistiksel dağılımları arasındaki farklılık.  
Veri sızıntısı: Test kümesindeki bilginin eğitim kümesinde de bulunması; başarım kestirimini iyimser yönde yanlı hale getirir.  
Oklüzyon analizi: Girdinin belirli bir bölgesinin kapatılarak modelin o bölgeye nedensel bağımlılığının ölçülmesi.  
ROC-AUC: Karar eşiğinden bağımsız olarak modelin pozitif ve negatif sınıfları ayırt etme yeteneğini ölçen alan.  
Kalibrasyon: Modelin ürettiği olasılıkların gerçek olabilirliklerle uyumu.

**2\. KURAMSAL ÇERÇEVE VE İLGİLİ ARAŞTIRMALAR**

Bu bölümde, çalışmanın dayandığı kuramsal temeller ve ilgili araştırmalar sistematik alt başlıklar halinde sunulmaktadır.

**2.1. Göğüs Radyografisinde Derin Öğrenme**

Göğüs radyografisi sınıflandırmasında dönüm noktalarından biri, NIH ChestX-ray14 veri kümesi üzerinde eğitilen ve 14 toraks patolojisini saptayan CheXNet modelidir (Rajpurkar ve diğerleri, 2017). Bu ve benzeri çalışmalar yüksek başarım bildirse de, kullanılan etiketlerin radyoloji raporlarından doğal dil işleme ile çıkarılması ve veri kümelerinin çoğunlukla tek merkezli olması, modellerin genellenebilirliği konusunda kuşku doğurmuştur (Wang ve diğerleri, 2017). Özellikle pnömoni gibi belirsiz sınırları olan bir patolojinin etiketlenmesindeki gürültü, bu kümelerde ulaşılabilecek başarıma bir tavan koymaktadır.

**2.2. Vision Transformer Mimarisi**

Vision Transformer, görüntüyü sabit boyutlu yamalara bölerek bir dizi olarak ele alan ve öz-dikkat mekanizmasıyla işleyen bir mimaridir (Dosovitskiy ve diğerleri, 2021). Yeterli ölçekte ön-eğitimle, evrişimli ağlarla yarışan ve birçok görevde onları geçen başarımlara ulaşır. Bu çalışmada ImageNet üzerinde ön-eğitilmiş ViT-B/16 modeli temel alınmıştır. ViT'in dikkat yapısı, modelin karar verirken görüntünün hangi bölgelerine ağırlık verdiğinin incelenmesine de olanak tanır.

**2.3. Kısayol Öğrenmesi ve Açıklanabilirlik**

Kısayol öğrenmesi, modelin eğitim dağıtımında hedefle bağıntılı kolay bir vekil özelliği öğrenmesidir (Geirhos ve diğerleri, 2020). Bu davranış, modelin eğitim ve test kümesinde yüksek başarım göstermesine karşın dağıtım dışı veride çökmesine yol açar. Teşhisinde açıklanabilirlik yöntemleri kullanılır. Transformer modellerinde dikkat akışını katmanlar boyunca bütünleştiren Attention Rollout yöntemi (Abnar ve Zuidema, 2020), sınıf belirteci üzerinden yamalar arasındaki dikkat akışını izleyerek bir ısı haritası üretir.

Ancak dikkat haritaları **korelasyoneldir**: modelin bir bölgeye ağırlık vermesi, kararını oraya dayandırdığını kanıtlamaz. Nedensel bir iddia için girdi düzeyinde müdahale gerekir. Oklüzyon temelli yaklaşımlar, bir bölgeyi kapatarak başarım değişimini ölçer ve böylece bağımlılığı nedensel olarak sınar (Zeiler ve Fergus, 2014). Bu çalışmada her iki yaklaşım birlikte kullanılmıştır.

**2.4. Anatomik Segmentasyon**

Akciğer alanlarının çıkarımı için, CheXmask veri kümesi üzerinde eğitilmiş çok merkezli ve yüksek başarımlı bir segmentasyon modeli kullanılmıştır (Gaggion ve diğerleri, 2024). Model, raporlanan doğrulukta sağ akciğer için yaklaşık 0,957 ve sol akciğer için yaklaşık 0,948 Dice katsayısına ulaşmaktadır. Bu çalışmada modelin yalnızca sağ ve sol akciğer çıktıları kullanılmış; kalp ve mediasten kasıtlı olarak dışlanmıştır.

**2.5. Veri Sızıntısı ve Yeniden Üretilebilirlik**

Tıbbi görüntülemede veri sızıntısının en sık görülen biçimi, aynı hastaya ait farklı görüntülerin eğitim ve test bölmelerine dağılmasıdır. Kamuya açık kümelerin türev sürümlerinde ise sınıf dengesi sağlamak amacıyla uygulanan augmentasyon, aynı kaynak görüntünün dönüştürülmüş kopyalarının farklı bölmelere düşmesine yol açabilir. Bu tür sızıntı, dosya adı veya boyut karşılaştırmasına dayanan basit denetimlerle saptanamaz. Bu çalışmada kullanılan türev kümenin veri kartı da bu riske açıkça dikkat çekmektedir. Sızıntının varlığı ve etkisi §4.1 ve §4.2'de ayrıca ölçülmüştür.

**2.6. İlgili Araştırmalar**

Tıbbi görüntülemede kısayol öğrenmesini teşhis eden çalışmaların yanı sıra (DeGrave ve diğerleri, 2021), modelleri doğru bölgelere yönlendirmeyi amaçlayan açıklama-kısıtlama yöntemleri de önerilmiştir (Ross ve diğerleri, 2017). Bu yöntemler, modelin açıklamasını bir kayıp terimiyle istenen bölgeye çekmeye çalışır. Akciğer segmentasyonunu bir ön-işleme adımı olarak kullanan çalışmalar da mevcuttur; ancak bu çalışmaların çoğu segmentasyonun katkısını kontrollü bir ablasyonla ölçmemekte, maskelemenin başarımı artırdığını varsaymaktadır. Bu seminer, söz konusu varsayımı doğrudan sınamakta ve maskeleme ile kadrajlamanın etkilerini birbirinden ayırmaktadır.

**3\. YÖNTEM**

Bu bölümde veri kümesi ve bütünlük denetimi, önerilen akciğer-odaklı ön-işleme hattı, model mimarisi, eğitim ayrıntıları, kontrollü ablasyon tasarımı, dış doğrulama, eşik kalibrasyonu, açıklanabilirlik ve nedensel bölge analizi ile istatistiksel yöntemler açıklanmaktadır. Önerilen çerçevenin uçtan uca görünümü Şekil 3.1'de verilmiştir.

![Onerilen cerceve](/figures/sekil_01_onerilen_cerceve.png)

Şekil 3.1. Önerilen akciğer-odaklı Vision Transformer çerçevesinin uçtan uca görünümü

**3.1. Veri Kümesi ve Bütünlük Denetimi**

Model, 1-5 yaş arası pediatrik hastalardan tek bir merkezde toplanan göğüs radyografisi kümesinin (Kermany ve diğerleri, 2018) kamuya açık dengelenmiş bir türevi üzerinde eğitilmiştir. Türev küme 8.530 görüntü içermekte olup her sınıftan 4.265 görüntüye sahiptir. Veri kartında belirtildiği üzere denge, **kontrollü alt örnekleme ve augmentasyon** ile sağlanmıştır.

Bu tür bir dengeleme sızıntı riski taşıdığından, eğitime geçilmeden önce sistematik bir bütünlük denetimi uygulanmıştır. Denetim altı bileşenden oluşur: (i) dosya adı şemalarının özgün kümenin adlandırma kalıplarıyla karşılaştırılması, (ii) dosya adlarından hasta anahtarı çıkarımı, (iii) bölmeler arası hasta düzeyi çakışma denetimi, (iv) içerik özetine (MD5) dayalı birebir kopya taraması, (v) algısal karma (dHash) ile yakın kopya taraması ve (vi) sınıfa göre çözünürlük dağılımının incelenmesi. Denetim sonuçları §4.1'de sunulmaktadır.

Bölmeleme şu biçimde yapılmıştır: özgün doğrulama kümesi F1 kestirimi için fazla küçük olduğundan (yaklaşık 30 örnek), doğrulama ve test havuzları birleştirilip her sınıftan eşit sayıda örnek içeren iki ayrık alt kümeye bölünmüştür. Bölme, sabit tohumla (42) deterministik biçimde üretilmiş ve her bölmenin içerik imzası (MD5) hesaplanarak sonraki tüm çalışmalarda aynı bölmenin kullanıldığı otomatik olarak doğrulanmıştır. Elde edilen bölmeler: eğitim 6.800, doğrulama 864, test 864 görüntü; her biri sınıf bakımından dengeli.

**3.2. Anatomik Maskeleme ve İlgi Alanı Çıkarımı**

Önerilen hattın çekirdeğini, her radyografı sınıflandırıcıya ulaşmadan önce dönüştüren çok aşamalı bir işlem oluşturur (Şekil 3.2). İlk aşamada segmentasyon modeliyle sağ ve sol akciğer maskesi çıkarılır; kalp ve mediasten bölgesi maskenin dışında bırakılır. Bu seçim kritiktir; çünkü önceki sürümde keşfedilen omurga/mediasten kısayolu tam da bu santral bölgede yaşamaktaydı.

İkinci aşama, segmentasyonun kusurlu olabileceği gerçeğini telafi eden bir tolerans katmanıdır. Maske, kısa kenarın yaklaşık %2,5'i kadar genişletilerek akciğer kenarındaki periferik patolojinin dışarıda kalması önlenir. Maske kenarına Gauss bulanıklığı uygulanarak akciğer ile arka plan arasındaki ani yoğunluk sıçraması yumuşatılır; böylece modelin bu yapay keskin kenarı yeni bir özellik olarak öğrenmesinin önüne geçilir. Akciğer dışı bölge, saf siyah yerine veri kümesi ortalama gri değeriyle doldurularak normalizasyon sonrası nötr bir zemin elde edilir.

Üçüncü aşamada maskenin sınır kutusu bulunur, %5 güvenlik payıyla genişletilir, en-boy oranı korunacak biçimde kareye tamamlanır ve 224 × 224 boyutuna ölçeklenir. Segmentasyonun boş maske döndürdüğü durumlarda görüntü doğrudan ölçeklenir ve geri çekilme olarak işaretlenir; bu çalışmada işlenen 10.128 görüntünün hiçbirinde geri çekilme tetiklenmemiştir. Tüm işlem çevrimdışı uygulanıp önbelleğe alınmıştır.

![Maskeleme algoritmasi](/figures/sekil_02_maskeleme_algoritmasi.png)

Şekil 3.2. Anatomik maskeleme ve ilgi alanı çıkarım algoritmasının adımları

![Masking Preview](/kaggle/Vision%20transformer%20pneumonia%20lung%20focused-V2/output/fig_01_masking_preview.png)

Şekil 3.3. Akciğer-odaklı maskeleme hattının üç aşaması: orijinal radyograf ve akciğer konturu, maske uygulanmış görüntü ve ilgi alanına kırpılmış nihai ViT girdisi

**3.3. Akciğer-Odaklı Vision Transformer Mimarisi**

Sınıflandırıcı olarak ImageNet üzerinde ön-eğitilmiş ViT-B/16 modeli kullanılmıştır. Modelin büyük bölümü dondurulmuş, yalnızca son iki kodlayıcı bloğu, katman normalizasyonu ve sınıflandırma başlığı ince ayarlanmıştır; bu, toplam 85,80 milyon parametrenin 14,18 milyonuna (%16,5) karşılık gelir. Kayıp fonksiyonu yalnızca standart çapraz entropidir; önceki sürümdeki ceza terimi tamamen kaldırılmıştır, çünkü akciğer dışına bakmama kısıtı artık bir ceza ile değil girdinin yapısıyla sağlanmaktadır.

**3.4. Eğitim Ayrıntıları**

Model, AdamW optimize edici (öğrenme oranı 1e-4, ağırlık çürümesi 1e-2) ve kosinüs öğrenme oranı çizelgesiyle 15 dönem boyunca, 16 örneklik yığınlarla eğitilmiştir. Girdiler 224 × 224 boyutunda, üç kanala kopyalanmış gri tonlamalı görüntülerdir ve veri kümesi ortalaması (0,4769) ile standart sapmasına (0,2414) göre normalize edilmiştir. Veri artırma hafif tutulmuş; akciğeri kadrajdan kaçırma riski taşıyan agresif rastgele kırpma kullanılmamıştır. En iyi doğrulama F1 değerini veren ağırlıklar saklanmış ve sonraki tüm değerlendirmelerde bu ağırlıklar kullanılmıştır.

**3.5. Kontrollü Ablasyon Tasarımı**

Anatomik maskelemenin katkısını ölçebilmek için üç kol, **aynı veri bölmesi, aynı rastgelelik tohumu, aynı mimari, aynı artırma ve aynı optimizasyon çizelgesiyle** sıfırdan eğitilmiştir. Kollar arasındaki tek fark, sınıflandırıcıya ulaşan görüntünün nasıl hazırlandığıdır (Çizelge 3.1, Şekil 3.4).

Çizelge 3.1. Kontrollü ablasyonda karşılaştırılan üç kolun tanımı ve izole ettiği etki

| Kol | Ön-işleme | İzole ettiği etki |
| :---- | :---- | :---- |
| **A (raw)** | Görüntü doğrudan 224 × 224 boyutuna ölçeklenir | Segmentasyon yok — taban çizgi |
| **B (roi)** | Segmentasyon **yalnızca** ilgi alanı kutusunu bulmak için kullanılır; hiçbir piksel silinmez | Kadrajlama (yakınlaştırma) etkisi |
| **C (lung)** | Akciğer dışı pikseller silinir ve aynı ilgi alanına kırpılır | Önerilen hattın tamamı |

Tasarımın kilit noktası, **B ve C kollarının birebir aynı kırpma kutusunu paylaşmasıdır.** Böylece B → C farkı yalnızca maskelemeyi, A → B farkı ise yalnızca kadrajlamayı yansıtır. Bu ayrıştırma olmadan, gözlenen bir başarım farkının maskelemeden mi yoksa akciğerin çerçeveyi doldurmasından (etkin çözünürlük artışından) mı kaynaklandığı belirlenemez. Her kolun eğitimi öncesinde tüm tohumlar sıfırlanmış ve veri yükleyicinin karıştırma üreteci sabit tohumla kurulmuştur; böylece kollar aynı ağırlık başlangıcını, aynı yığın sırasını ve aynı artırma rastgeleliğini paylaşmıştır.

![Uc kolun girdisi](/kaggle/Ablation-Segmentation-V3/output/abl_fig_01_arms_preview.png)

Şekil 3.4. Aynı radyograftan üretilen üç ablasyon kolunun girdileri

**3.6. Dış Doğrulama Tasarımı**

Aynı dağıtımdan ayrılan bir test kümesindeki yüksek başarım, modelin başka bir merkezin cihazında da çalışacağını göstermez. Bu nedenle model, eğitim verisinden tamamen bağımsız iki yetişkin veri kümesinde sınanmıştır. Birincisi, radyolog gözden geçirmeli ikili etiketlere sahip RSNA Pneumonia Detection Challenge kümesidir; belirsiz "akciğer opasitesi yok / normal değil" sınıfı dışlanmıştır. İkincisi, etiketleri raporlardan doğal dil işleme ile çıkarılmış olan NIH ChestX-ray14 kümesidir (Wang ve diğerleri, 2017). Her iki kümeden de sabit tohumla dengeli örneklem alınmış ve eğitimle birebir aynı hattan geçirilmiştir. COVID-19 Radiography kümesi, içerdiği görüntülerin bu çalışmanın eğitim kaynağıyla örtüşmesi nedeniyle kasıtlı olarak dışlanmıştır.

Örneklem büyüklüğünün yeterliliğini sınamak amacıyla dış doğrulama, sınıf başına 400 görüntüyle yapılan birincil analizin ardından, aynı tohumla genişletilmiş bir üst kümede (RSNA'da sınıf başına 1.000, NIH'de havuzun izin verdiği 1.431) yinelenmiştir. Genişletilmiş örneklemin ilk 400 görüntüsü birincil örneklemle birebir aynı olduğundan, önceki sonuçlar iç tutarlılık denetimi olarak yeniden üretilebilmiştir.

**3.7. Eşik Yeniden Kalibrasyonu**

Dağıtım kayması altında modelin olasılık çıktıları yanlı hale gelebilir. Bunu incelemek için her dış küme, sabit tohumla %50 kalibrasyon ve %50 test olarak katmanlı biçimde bölünmüştür. Platt ölçekleme ve isotonik regresyon kalibratörleri yalnızca kalibrasyon yarısında öğrenilmiş; tüm ölçütler görülmemiş test yarısında raporlanmıştır. Bu yaklaşım, gerçek dağıtımda küçük bir etiketli yetişkin örneklemiyle kalibrasyon yapmaya karşılık gelir. Her iki dönüşüm de monoton olduğundan AUC değerini değiştirmez; yalnızca olasılıkların güvenilirliğini ve karar eşiğinin anlamlılığını etkiler.

**3.8. Açıklanabilirlik ve Akciğer-Odak Oranı**

Modelin dikkatinin nereye yöneldiğini niceliklendirmek için Attention Rollout (Abnar ve Zuidema, 2020) ile elde edilen ısı haritası, akciğer maskesiyle karşılaştırılmıştır. $S(u) \in [0,1]$ normalize edilmiş dikkat değeri, $L(u) \in \{0,1\}$ akciğer maskesi ve $\tau = 0{,}20$ gürültü eşiği olmak üzere yüksek-enerjili piksel kümesi $\Omega = \{u : S(u) > \tau\}$ üzerinde Akciğer-Odak Oranı şöyle tanımlanır:

$$\mathrm{LFR} = \frac{\sum_{u \in \Omega} S(u)\,L(u)}{\sum_{u \in \Omega} S(u)}$$

Ölçüm, her kolun kendi koordinat uzayındaki maskesiyle yapılmıştır. Değerin yorumlanmasında kritik referans, aynı kümedeki **ortalama akciğer maske alanıdır**: rastgele dağılmış bir dikkat haritası, beklenen değer olarak maske alanına eşit bir LFR üretir. Dolayısıyla LFR'nin maske alanına oranı, dikkatin akciğere yönelme veya akciğerden kaçınma derecesini verir.

**3.9. Nedensel Bölge Analizi: Oklüzyon Testi**

Dikkat haritaları korelasyoneldir. Nedensel bir iddia için, girdinin belirli bölgeleri kapatılarak başarım değişimi ölçülmüştür. Kapatılan bölge, maskeleme hattındaki dolgu değeriyle aynı olan veri kümesi ortalama grisiyle doldurulmuştur.

Tasarımın kilit noktası şudur: **herhangi bir bölgeyi kapatmak girdi dağılımını bozar ve zaten bir miktar başarım kaybı üretir.** Bu nedenle her hedefli oklüzyona, aynı alanı kaplayan rastgele konumlu bir dikdörtgen kontrolü eşlik ettirilmiştir (Çizelge 3.2). Bir bölgenin nedensel katkısı, kendi düşüşü ile alan eşleşmeli kontrolün düşüşü arasındaki farktır:

$$\text{net etki} = \Delta\mathrm{AUC}_{\text{bölge}} - \Delta\mathrm{AUC}_{\text{rastgele, aynı alan}}$$

Çizelge 3.2. Oklüzyon testinde kullanılan bölgeler ve alan eşleşmeli kontrolleri

| Bölge | Kapladığı alan | Alan eşleşmeli kontrolü |
| :---- | :---: | :---- |
| Akciğerler | ≈ %25 (maskeye göre) | Görüntü başına eşleşen rastgele dikdörtgen |
| Akciğer dışı (tümleyen) | ≈ %75 | — (alan eşleşmeli kontrolü yoktur) |
| Köşeler | %19,1 | %20 rastgele dikdörtgen |
| Çevre şeridi | %29,6 | %30 rastgele dikdörtgen |
| Diyafram altı bant | %28,1 | %30 rastgele dikdörtgen |
| Üst bant | %20,1 | %20 rastgele dikdörtgen |
| Merkezî sütun | %19,6 | %20 rastgele dikdörtgen |

Hattın doğruluğu iki otomatik tutarlılık denetimiyle sınanmıştır: C kolunda akciğer dışı bölgenin kapatılması etkisiz olmalıdır (o bölge zaten gri doludur) ve akciğerlerin kapatılması yıkıcı olmalıdır (tüm bilgi silinir).

![Okluzyon kosullari](/kaggle/Occlusion-V9/output/occ_fig_00_conditions.png)

Şekil 3.5. Oklüzyon testinde kullanılan bölge kapatma koşulları

**3.10. İstatistiksel Analiz**

Birincil başarım ölçütü, eşikten bağımsız olduğu için kümeler arası karşılaştırmada en adil ölçüt olan ROC-AUC'dir. Ek olarak ortalama kesinlik, doğruluk, F1, duyarlılık ve özgüllük raporlanmıştır. Olasılık kalitesi için Brier skoru ve beklenen kalibrasyon hatası kullanılmıştır. Karar tabanlı ölçütler 0,50 eşiğinde hesaplanmıştır.

İki kolun aynı örneklem üzerindeki AUC değerleri ilişkili olduğundan, farkın anlamlılığı **DeLong testiyle** sınanmıştır. Güven aralıkları, sınıf-katmanlı yeniden örneklemeye dayalı eşleştirilmiş bootstrap ile (2.000 tekrar) hesaplanmıştır; aynı yeniden örnekleme indeksleri tüm kollara uygulanarak fark dağılımının eşleştirilmiş olması sağlanmıştır. Eşik 0,50'deki ikili kararların karşılaştırılmasında McNemar testi kullanılmıştır. Akciğer-odak oranı dağılımları sınırlı ve çarpık olduğundan, aynı görüntünün üç kolun hattından geçmesi nedeniyle eşleştirilmiş olan bu ölçüm Wilcoxon işaretli sıra testiyle karşılaştırılmıştır.

Eğitim rastgeleliğinin etkisini ayrıştırmak için tüm ablasyon kolları **üç bağımsız eğitim tohumuyla** yeniden eğitilmiştir. Veri bölmesi ve dış örneklem seçimi sabit tohumla (42) korunmuş, yalnızca ağırlık başlangıcı, yığın sırası ve artırma rastgeleliği değiştirilmiştir. Kol içi standart sapma gürültü tabanı olarak raporlanmış ve kollar arası farkla aynı ölçekte karşılaştırılmıştır. Ayrıca her kol için tohumların olasılık ortalaması alınarak bir topluluk oluşturulmuş; topluluklar arası karşılaştırma, eğitim gürültüsünden büyük ölçüde arındırılmış bir kestirim sağlamıştır.

**4\. BULGULAR**

Bu bölümde veri kümesi bütünlük denetimi, iç test başarımı, kontrollü ablasyon, örneklem gücü ve tohum değişkenliği, dış doğrulama, kalibrasyon, akciğer-odak oranı ve nedensel bölge analizi sonuçları sunulmaktadır.

**4.1. Veri Kümesi Bütünlük Denetimi**

Denetim, kullanılan dengelenmiş türev kümede sınıfa göre asimetrik ve sistematik bir yapı ortaya koymuştur (Çizelge 4.1). NORMAL sınıfı 1.575 kaynak görüntüden augmentasyonla 4.265 dosyaya çıkarılmış olup kaynak başına ortalama 2,71 kopya bulunmaktadır; yalnızca 279 kaynak görüntünün hiç kopyası yoktur. Buna karşılık PNEUMONIA sınıfındaki 4.265 dosyanın tamamı benzersizdir ve hiçbir augmentasyon kopyası içermez. Dosya adı şeması analizi bunu doğrulamaktadır: NORMAL sınıfındaki 2.690 dosya `_aug_` ekiyle işaretlenmiş augmentasyon türevi olup dört farklı adlandırma kalıbına dağılmıştır; PNEUMONIA sınıfında bu ekin bulunduğu tek bir dosya dahi yoktur.

Bunun doğrudan sonucu, bölmeler arasında **sınıfa göre asimetrik bir sızıntıdır.** Kümenin paketlenmiş bölmesinde doğrulama kümesindeki NORMAL görüntülerin %87,3'ü, bu çalışmada kullanılan test bölmesindeki NORMAL görüntülerin ise %86,6'sı, eğitim kümesindeki bir görüntünün augmentasyon kopyasıdır. PNEUMONIA sınıfında bu oran her iki bölmede de %0,0'dır. Ayrıca 62 dosya birebir içerik kopyası olarak saptanmış, bunların 11 grubu birden fazla bölmeye yayılmıştır.

Çizelge 4.1. Veri kümesi bütünlük denetimi özeti

| Ölçüt | NORMAL | PNEUMONIA |
| :---- | :---: | :---: |
| Toplam dosya | 4.265 | 4.265 |
| Benzersiz kaynak görüntü | **1.575** | 4.265 |
| Augmentasyon kopyası | 2.690 | 0 |
| Kaynak başına ortalama kopya | 2,71 | 1,00 |
| Test bölmesinde eğitimle aynı kaynağı paylaşan | **%86,6** | %0,0 |
| Doğrulama bölmesinde aynı oran | %87,3 | %0,0 |

Bu bulgu, kümenin veri kartındaki "kontrollü alt örnekleme ve augmentasyon ile dengelenmiştir" ifadesiyle ve aynı kartın "augmente varyantları bölmeler arasında karıştırmayın" uyarısıyla tutarlıdır. Bulgunun başarım üzerindeki etkisi bir sonraki alt bölümde ayrıca ölçülmüştür.

**4.2. İç Test Başarımı ve Sızıntısız Değerlendirme**

Üç kol da eğitim verisiyle aynı dağıtımdan gelen iç test kümesinde çok yüksek başarım sergilemiştir (ROC-AUC 0,998). Sızıntının bu değere katkısını ölçmek için, eğitim kümesiyle hiçbir kaynak görüntüyü paylaşmayan alt kümeler tanımlanmış ve aynı modeller yeniden değerlendirilmiştir. En katı ölçüt olan hasta düzeyi ayrıklıkta 40 NORMAL ve 138 PNEUMONIA görüntü kalmıştır (Çizelge 4.2).

Çizelge 4.2. İç test başarımı: sızıntılı ve sızıntısız alt kümelerde ROC-AUC

| Alt küme | N | A (raw) | B (roi) | C (lung) |
| :---- | :---: | :---: | :---: | :---: |
| Orijinal test (sızıntılı) | 864 | 0,9981 | 0,9976 | 0,9982 |
| Kaynak düzeyi temiz | 949 | 0,9937 | 0,9925 | 0,9958 |
| **Hasta düzeyi temiz** | **178** | **0,9893** | **0,9873** | **0,9951** |

Sızıntının katkısı, pozitif küme sabit tutulup negatif kümenin sızıntılı ve temiz olarak değiştirilmesiyle doğrudan ölçülmüştür: A kolunda +0,005, B kolunda +0,007, C kolunda +0,002 AUC. NORMAL görüntülerdeki tahmin olasılığı dağılımları sızıntılı ve temiz gruplarda ayırt edilemez düzeydedir; her iki grup da sıfıra yakın olasılıklarda yığılmaktadır.

Bu sonuç iki bakımdan önemlidir. Birincisi, saptanan sızıntı gerçek olmakla birlikte **iç test başarımını sürüklememektedir**; model hiç görmediği hastalarda da yaklaşık 0,99 AUC üretmektedir. İkincisi ve daha kritik olarak, bu durum çalışmanın merkezi paradoksunu keskinleştirmektedir: model ezberlemiyor, gerçekten genelleşen bir sinyal öğreniyor — ancak §4.7 ve §4.8'de gösterileceği üzere bu sinyal akciğerlerde bulunmamaktadır.

![Temiz ic test](/kaggle/Clean-Internal-V8/output/clean_fig_01_auc.png)

Şekil 4.1. Sızıntılı ve sızıntısız alt kümelerde iç test başarımı

**4.3. Segmentasyonun Katkısı: Kontrollü Ablasyon**

Üç kolun karşılaştırması Çizelge 4.3 ve Şekil 4.2'de verilmiştir. Hiçbir kümede kollar arasında anlamlı bir ayrıştırma farkı bulunmamıştır: dokuz eşleştirilmiş karşılaştırmanın tamamında bootstrap güven aralıkları sıfırı içermekte ve DeLong p değerleri 0,19'un üzerinde kalmaktadır (Çizelge 4.4). ROC eğrileri üç kümede de üst üste binmektedir.

Çizelge 4.3. Kontrollü ablasyon: kol ve küme bazında ROC-AUC (tek tohum, sınıf başına 400 görüntü)

| Küme | N | A (raw) | B (roi) | C (lung) |
| :---- | :---: | :---: | :---: | :---: |
| İç test | 864 | 0,9981 | 0,9976 | 0,9982 |
| RSNA | 800 | 0,9163 | 0,9182 | 0,9264 |
| NIH ChestX-ray14 | 800 | 0,6787 | 0,6785 | 0,6887 |

Çizelge 4.4. Kollar arası eşleştirilmiş karşılaştırmalar (DeLong testi)

| Küme | Karşılaştırma | ΔAUC | %95 GA | DeLong p |
| :---- | :---- | :---: | :---: | :---: |
| İç test | C − A | +0,000 | [−0,002; +0,002] | 0,978 |
| İç test | C − B | +0,001 | [−0,001; +0,002] | 0,491 |
| RSNA | C − A | +0,010 | [−0,005; +0,025] | 0,192 |
| RSNA | C − B | +0,008 | [−0,007; +0,023] | 0,296 |
| NIH | C − A | +0,010 | [−0,014; +0,035] | 0,421 |
| NIH | C − B | +0,010 | [−0,013; +0,034] | 0,395 |

Eşik 0,50'deki doğruluk karşılaştırmalarında (McNemar) bazı farklar anlamlı çıkmıştır; ancak bu farklar ayrıştırma yeteneğine değil çalışma noktasına ilişkindir. Örneğin RSNA'da B kolu A koluna göre 0,50 eşiğinde belirgin biçimde daha yüksek doğruluk üretmektedir (McNemar p < 10⁻⁶) ancak AUC farkı yalnızca +0,002 ve anlamsızdır. Olasılıkların %88-98'i 0,05'in altında veya 0,95'in üstünde toplandığından, eşik tabanlı ölçütler doygun kütlenin konumuna duyarlıdır ve ayrıştırma farkı olarak yorumlanmamalıdır.

![Ablasyon AUC](/kaggle/Ablation-Segmentation-V3/output/abl_fig_03_auc_by_arm.png)

Şekil 4.2. Kontrollü ablasyon: kol başına ROC-AUC ve bootstrap güven aralıkları

Farkların etki büyüklüğü Şekil 4.3'te ayrıca gösterilmiştir. Dokuz karşılaştırmanın tamamında güven aralığı sıfır çizgisini kesmektedir; C kolu lehine olan farklar her iki dış kümede de aynı yönde olmakla birlikte hiçbiri istatistiksel anlamlılığa ulaşmamaktadır.

![Etki buyuklugu](/kaggle/Ablation-Segmentation-V3/output/abl_fig_05_effect.png)

Şekil 4.3. Kollar arası AUC farkının etki büyüklüğü

**4.4. Örneklem Gücü ve Eğitim Tohumu Değişkenliği**

Gözlenen +0,010'luk farkın örneklem gücü yetersizliğinden mi yoksa gerçek bir etkinin yokluğundan mı kaynaklandığını ayırmak için iki tamamlayıcı analiz yürütülmüştür.

Birincisi, dış doğrulama örnekleminin genişletilmesidir. RSNA'da sınıf başına 400'den 1.000'e, NIH'de 1.431'e çıkarıldığında etki büyüklüğü neredeyse değişmemiştir (RSNA'da C − A = +0,0099; NIH'de +0,0098) ve güven aralıkları beklendiği gibi daralmıştır. RSNA'da DeLong p değeri 0,056'ya inmiş ancak anlamlılık sınırının altına düşmemiştir. Genişletilmiş örneklemin ilk 400 görüntüsünde hesaplanan AUC değerleri, birincil analizle ±0,0000 farkla eşleşerek hattın doğruluğunu doğrulamıştır.

İkincisi ve belirleyici olanı, üç bağımsız eğitim tohumuyla yapılan tekrardır (Çizelge 4.5). RSNA'da C kolunun üç tohumdaki AUC değerleri 0,9264, 0,9191 ve 0,9084'tür; yani tek tohumlu analizde kullanılan koşum, o kolun üç koşumundan en iyisiydi. Kol içi standart sapma (0,0091), aranan etkiyle (0,010) aynı mertebededir. Tohum ortalaması alındığında C − A farkı +0,0026'ya, tohum topluluğu düzeyinde ise +0,0006'ya (p = 0,94) gerilemektedir.

Çizelge 4.5. Üç eğitim tohumunda kol içi değişkenlik ve topluluk sonuçları

| Küme | Kol | Tohum ort. ± ss | Topluluk AUC | Topluluk C − A (p) |
| :---- | :---- | :---: | :---: | :---: |
| İç test | A | 0,99804 ± 0,00062 | 0,9987 | — |
| İç test | C | 0,99762 ± 0,00094 | 0,9982 | −0,0005 (0,51) |
| RSNA | A | 0,9154 ± 0,0052 | 0,9227 | — |
| RSNA | C | 0,9180 ± 0,0091 | 0,9232 | +0,0006 (0,94) |
| NIH | A | 0,6758 ± 0,0174 | 0,6753 | — |
| NIH | C | 0,6874 ± 0,0040 | 0,6901 | +0,0148 (0,25) |

Bu iki analiz birlikte değerlendirildiğinde sonuç açıktır: **tek tohumda gözlenen küçük fark, eğitim rastgeleliğinden ayırt edilemez.** Anatomik maskeleme, ayrıştırma başarımını ölçülebilir biçimde değiştirmemektedir.

![Tohum dagilimi](/kaggle/MultiSeed-V5/output/seed_fig_01_scatter.png)

Şekil 4.4. Üç eğitim tohumunda kolların ROC-AUC dağılımı

**4.5. Dış Doğrulama Sonuçları**

Önerilen hattın (C kolu) dış doğrulama sonuçları Çizelge 4.6 ve Şekil 4.5'te özetlenmiştir. RSNA kümesinde model, eğitiminde hiç görmediği yetişkin radyografilerinde AUC 0,930 değerine ulaşmıştır. NIH kümesinde ise AUC 0,702 ile daha düşük kalmıştır; bu değer bağlam içinde değerlendirilmelidir, çünkü doğrudan NIH üzerinde eğitilmiş modeller bile bu kümenin gürültülü pnömoni etiketinde yaklaşık 0,77 AUC alabilmektedir (Rajpurkar ve diğerleri, 2017). Her iki kümede de yüksek duyarlılık ve düşük özgüllük gözlenmiştir.

Çizelge 4.6. Dış doğrulama setlerinde özet başarım ölçütleri (karar eşiği 0,50)

| Veri Kümesi | N | AUC | AP | Doğruluk | F1 | Duyarlılık | Özgüllük | Brier | ECE |
| :---- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| RSNA | 800 | 0,930 | 0,927 | 0,802 | 0,830 | 0,965 | 0,640 | 0,190 | 0,193 |
| NIH | 800 | 0,702 | 0,677 | 0,641 | 0,703 | 0,850 | 0,432 | 0,350 | 0,350 |

Burada önemli bir düzeltme gerekmektedir. Dış kümedeki başarım düşüşü, tek başına kısayol öğrenmesinin bir sınavı olarak yorumlanamaz. Ablasyon sonuçları, **üç kolun da neredeyse aynı oranda gerilediğini** göstermektedir (iç test 0,998 → RSNA 0,92 → NIH 0,68). Akciğer dışı bilgiyi tamamen silen kol da, hiç silmeyen kol da benzer biçimde düşmektedir. Dolayısıyla düşüşün kaynağı kenar veya çevre artefaktları değil; pediatrik popülasyondan yetişkin popülasyona geçiş ve dış kümelerdeki etiket tanımı farklılıklarıdır.

![Ext Summary](/kaggle/Lung%20Focused%20VIT%20External%20Validation-V2/output/ext_summary.png)

Şekil 4.5. Dış doğrulama setleri arasında ROC-AUC ile duyarlılık ve özgüllük karşılaştırması

**4.6. Kalibrasyon Sonrası Başarım**

Eşik yeniden kalibrasyonunun sonuçları Çizelge 4.7 ve Şekil 4.6'da verilmiştir. Her iki kümede de olasılık güvenilirliği belirgin biçimde iyileşmiş; beklenen kalibrasyon hatası RSNA'da 0,191'den 0,015'e, NIH'de 0,347'den 0,017'ye gerilemiştir. RSNA kümesinde isotonik kalibrasyon gerçek bir çalışma noktası kazancı sağlamış, özgüllük 0,645'ten 0,820'ye yükselmiştir. Buna karşılık NIH kümesinde özgüllük kalibrasyona rağmen büyük ölçüde değişmemiştir; bu, NIH'deki sınırın bir eşik problemi değil, etiket gürültüsünden kaynaklanan bir ayrıştırma tavanı olduğunu doğrular. Beklendiği gibi kalibrasyon her iki kümede de AUC değerini değiştirmemiştir.

Çizelge 4.7. Eşik yeniden kalibrasyonu öncesi ve sonrası başarım (görülmemiş %50 test yarısı, eşik 0,50)

| Veri Kümesi | Yöntem | Doğruluk | F1 | Duyarlılık | Özgüllük | Brier | ECE |
| :---- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| RSNA | Ham (0,50) | 0,808 | 0,834 | 0,970 | 0,645 | 0,188 | 0,191 |
| RSNA | Platt | 0,815 | 0,840 | 0,970 | 0,660 | 0,141 | 0,015 |
| RSNA | Isotonic | 0,852 | 0,857 | 0,885 | 0,820 | 0,109 | 0,047 |
| NIH | Ham (0,50) | 0,652 | 0,706 | 0,835 | 0,470 | 0,342 | 0,347 |
| NIH | Platt | 0,645 | 0,698 | 0,820 | 0,470 | 0,224 | 0,017 |
| NIH | Isotonic | 0,632 | 0,667 | 0,735 | 0,530 | 0,220 | 0,061 |

![Ext Calibration](/kaggle/Lung%20Focused%20VIT%20External%20Validation-V2/output/ext_calibration.png)

Şekil 4.6. Eşik yeniden kalibrasyonu öncesi ve sonrası güvenilirlik eğrileri ile özgüllük ve duyarlılık değişimi

**4.7. Akciğer-Odak Oranı**

Başarım bakımından ayırt edilemeyen üç kol, dikkat hizalaması bakımından birbirinden kökten ayrılmaktadır (Çizelge 4.8). Ölçüm, iç test kümesinin yanı sıra bağımsız yetişkin kümelerde de yinelenmiş; böylece örüntünün eğitim dağıtımına özgü olmadığı doğrulanmıştır.

Çizelge 4.8. Akciğer-odak oranının kol ve küme bazında dağılımı

| Küme | n | A (raw) | B (roi) | C (lung) | Ortalama maske alanı |
| :---- | :---: | :---: | :---: | :---: | :---: |
| İç test | 120 | 0,005 | 0,111 | 0,909 | — |
| RSNA | 500 | **0,011** | 0,043 | **0,952** | 0,236 |
| NIH | 500 | **0,017** | 0,048 | **0,951** | 0,237 |

Yorumun anahtarı son sütundur. Ortalama akciğer maske alanı 0,236 olduğuna göre, **rastgele dağılmış bir dikkat haritası bile beklenen değer olarak 0,236 civarında bir LFR üretirdi.** Segmentasyonsuz modelin 0,011 değeri, bu şans düzeyinin yaklaşık yirmi ikide biridir. Model akciğerden yalnızca pasif biçimde uzak durmamakta, dikkatini akciğer dışına aktif olarak yöneltmektedir.

Eşleştirilmiş Wilcoxon testinde C − A medyan farkı RSNA'da +0,955, NIH'de +0,957 bulunmuş (p < 10⁻⁵⁰) ve **500 görüntünün 500'ünde** C kolu daha yüksek örtüşme göstermiştir; iki dağılım arasında hiçbir örtüşme yoktur. Toplu dikkat haritaları bunu görsel olarak da doğrulamaktadır (Şekil 4.8): segmentasyonsuz modelde enerji köşelerde, çevre şeridinde ve diyafram altı bölgede toplanırken akciğer alanları neredeyse boş kalmakta; maskelenmiş modelde ise dikkat doğrudan parankim içindedir.

Segmentasyonun yetişkin görüntülerdeki davranışı da denetlenmiştir: maske alanının makul aralık dışında kaldığı görüntü oranı RSNA'da %5,6, NIH'de %4,4 olup çok küçük maske üretilen görüntü bulunmamaktadır. Dolayısıyla §1.4'teki segmentasyon sayıltısı yetişkin veride de karşılanmaktadır. Ayrıca akciğer-odak oranı ile tahmin doğruluğu arasında hiçbir kümede anlamlı ilişki bulunmamıştır (tüm p > 0,08).

![LFR dagilimlari](/kaggle/External-LFR-V6/output/extlfr_fig_01_distributions.png)

Şekil 4.7. Akciğer-odak oranının kümeler ve kollar arasında dağılımı

![Toplu dikkat](/kaggle/External-LFR-V6/output/extlfr_fig_02_aggregate.png)

Şekil 4.8. Bağımsız kümelerde toplu dikkat haritaları

**4.8. Nedensel Bölge Analizi Sonuçları**

Oklüzyon testi, dikkat temelli gözlemi nedensel bir bulguya dönüştürmüştür (Çizelge 4.9). Otomatik tutarlılık denetimleri beklendiği gibi sonuçlanmıştır: C kolunda akciğer dışı bölgenin kapatılması iç testte yalnızca +0,001 AUC kaybı üretmiş, akciğerlerin kapatılması ise +0,259 kayba yol açmıştır.

Çizelge 4.9. Oklüzyon testi: bölge kapatmanın ROC-AUC üzerindeki etkisi

| Küme | Kol | Bozulmamış | Akciğerler kapalı | Akciğer dışı kapalı | Alan eşleşmeli rastgele |
| :---- | :---- | :---: | :---: | :---: | :---: |
| İç test | A (raw) | 0,9981 | **0,9896** | **0,7799** | 0,9936 |
| İç test | C (lung) | 0,9982 | **0,7395** | 0,9968 | 0,9665 |
| RSNA | A (raw) | 0,9238 | 0,8950 | 0,8046 | 0,8818 |
| RSNA | C (lung) | 0,9364 | 0,6822 | 0,9231 | 0,8315 |
| NIH | A (raw) | 0,6912 | 0,6610 | 0,6318 | 0,6839 |
| NIH | C (lung) | 0,7051 | 0,6022 | 0,6933 | 0,6334 |

Segmentasyonsuz model, **her iki akciğer alanı tamamen silindiğinde iç test AUC değerinin %99'unu korumaktadır** (0,9981 → 0,9896). Aynı büyüklükte rastgele bir bölge silindiğinde ortaya çıkan kayıpla karşılaştırıldığında net etki iç testte +0,004, RSNA'da −0,013, NIH'de +0,023'tür; yani akciğerin silinmesi, aynı alanda rastgele bir bölgenin silinmesinden daha fazla zarar vermemektedir. Buna karşılık aynı karşılaştırma C kolunda +0,227 (iç test) ve +0,149 (RSNA) net etki üretmektedir. İki kol arasında tam bir ayna simetrisi gözlenmektedir.

Akciğer dışındaki her şey silindiğinde segmentasyonsuz modelin başarımı 0,7799'a gerilemektedir; bu, akciğerlerin silinmesiyle oluşan kaybın iç testte 25,6 katıdır. Ancak bu karşılaştırmanın alan eşleşmeli olmadığı (yaklaşık %75'e karşı %25 alan) belirtilmelidir; nedensel iddianın metodolojik dayanağı, alan eşleşmeli olan akciğer-rastgele karşılaştırmasıdır.

Tek tek geometrik bölgelerin (köşeler, çevre şeridi, diyafram altı bant, üst bant, merkezî sütun) hiçbirinin net etkisi anlamlı bulunmamıştır; çoğu negatiftir. Dolayısıyla kısayol tek bir alt bölgede yoğunlaşmamış, akciğer dışı bölgeye **yayılmış ve fazlalıklı** biçimde kodlanmıştır. Bu, B kolunun (yalnızca kırpma) neden ne başarımı ne de dikkat hizalamasını düzeltemediğini açıklamaktadır: tek bir çevresel bölgeyi kırpmak yeterli değildir.

![Okluzyon net etki](/kaggle/Occlusion-V9/output/occ_fig_01_net_effect.png)

Şekil 4.9. Bölge kapatmanın nedensel etkisi

**5\. TARTIŞMA**

Bulgular bir bütün olarak değerlendirildiğinde, çalışmanın çıkış hipotezinin bir bölümü desteklenmemiş, buna karşılık daha güçlü ve daha genel bir sonuç ortaya çıkmıştır.

Desteklenmeyen bölüm şudur: anatomik maskeleme sınıflandırma başarımını artırmamaktadır. Üç kol, üç farklı kümede, üç eğitim tohumunda ve iki farklı örneklem büyüklüğünde istatistiksel olarak ayırt edilemez düzeyde kalmıştır. Bu sonuç, segmentasyon tabanlı ön-işlemenin başarımı artırdığını varsayan yaygın uygulamayı sorgulamaktadır. Tek tohumla çalışan bir araştırmacının bu veriden +0,010'luk bir iyileşme raporlaması mümkündü; çoklu tohum analizi bunun bir koşum şansı olduğunu göstermiştir. Bu, yöntemsel açıdan ayrıca kayda değer bir uyarıdır.

Buna karşılık maskeleme, modelin karar dayanağını kökten değiştirmektedir. Segmentasyonsuz modelin dikkatinin akciğerle örtüşmesi, bağımsız yetişkin kümelerde şans düzeyinin yaklaşık yirmi ikide biridir ve bu örüntü 1.000 görüntünün tamamında tutarlıdır. Oklüzyon testi bunun bir gözlem artefaktı olmadığını doğrulamaktadır: her iki akciğer tamamen silindiğinde model başarımının %99'unu korumakta, akciğer dışı silindiğinde ise çökmektedir. Maskelenmiş modelde tam tersi geçerlidir.

Buradan çıkan temel sonuç şudur: **başarım ölçütleri, modelin klinik olarak anlamlı bölgeyi kullanıp kullanmadığına kördür.** İki model aynı AUC değerini üretirken tamamen farklı bilgi kaynaklarına dayanabilmektedir. Bir çalışmanın yalnızca doğruluk, F1 veya AUC raporlaması, modelin güvenilirliği hakkında hiçbir güvence sağlamamaktadır. Güvenilirlik, ayrı bir eksende ve ayrı araçlarla — dikkat hizalaması ve nedensel bölge analiziyle — ölçülmelidir.

Segmentasyonsuz modelin kullandığı sinyalin ne olduğu açık bir sorudur. Sızıntısız iç test, modelin hiç görmediği hastalarda da yaklaşık 0,99 AUC ürettiğini göstermektedir; dolayısıyla ezberleme söz konusu değildir. Model, o dağıtım içinde gerçekten genelleşen ancak akciğer dışında bulunan bir örüntü öğrenmektedir. Oklüzyon sonuçları bu örüntünün tek bir bölgede yoğunlaşmadığını, çevresel anatomi ve çekim bağlamına yayıldığını göstermektedir. Çekim/pozlama karakteristiği, hasta pozisyonu ve gövde dokusu olası adaylar arasındadır; ancak bu çalışma hangisinin belirleyici olduğunu saptayacak tasarıma sahip değildir.

Dış kümelerdeki başarım düşüşünün yorumu da düzeltilmelidir. Üç kolun da benzer oranda gerilemesi, düşüşün akciğer dışı kısayollardan değil, popülasyon kayması ve etiket tanımı farklılıklarından kaynaklandığını göstermektedir. Bu nedenle dış doğrulamadaki AUC düşüşü, tek başına bir kısayol sınavı olarak kullanılmamalıdır. Ham modelin yetişkin verisinde düşük özgüllük göstermesi bir ayrıştırma sorunu değil kalibrasyon sorunudur ve küçük bir etiketli örneklemle büyük ölçüde giderilebilmektedir.

Kullanılan veri kümesindeki sızıntının belgelenmesi ayrı bir katkıdır. NORMAL sınıfının augmentasyonla çoğaltılması, test bölmesindeki negatif örneklerin %86,6'sının eğitimdeki bir görüntünün kopyası olması sonucunu doğurmuştur. Sızıntının başarıma katkısının küçük çıkması (0,005 AUC) bu bulgunun önemini azaltmaz; aynı kümeyi kullanan çalışmaların bölmeleri kaynak görüntü düzeyinde ayırması gerekmektedir.

**6\. SONUÇ VE ÖNERİLER**

Bu seminerde, göğüs radyografisinde pnömoni sınıflandırması için akciğer dışı bilgiyi girdi düzeyinde maskeleyen bir Vision Transformer hattı sunulmuş; katkısı üç kollu kontrollü bir ablasyonla ölçülmüş ve model, eğitiminden bağımsız iki yetişkin veri kümesinde dış doğrulamadan geçirilmiştir. Sonuçlar dört ana mesaj vermektedir.

Birincisi, anatomik maskeleme ayrıştırma başarımını değiştirmemektedir; gözlenen küçük farklar eğitim rastgeleliğinin içinde kalmaktadır. İkincisi, maskeleme modelin karar dayanağını kökten değiştirmekte; dikkat hizalamasını şans düzeyinin yirmi ikide birinden 0,95'e taşımaktadır. Üçüncüsü, bu fark nedenseldir: segmentasyonsuz model, akciğerleri tamamen silindiğinde başarımının %99'unu korumaktadır. Dördüncüsü, güvenilir olasılıklar için kalibrasyon gerekli ve etkilidir; ancak etiket kaynaklı her sınır kalibrasyonla çözülememektedir.

Bu bulguların pratik karşılığı şudur: bir modelin klinik kullanıma uygunluğu, başarım ölçütleriyle değerlendirilemez. Değerlendirme protokolü, dikkat hizalaması ve nedensel bölge analizi gibi araçları içermelidir. Anatomik maskeleme, başarım kaybı olmaksızın modeli denetlenebilir kıldığı için — başarımı artırmasa bile — savunulabilir bir tasarım tercihidir.

Gelecek çalışmalar için öneriler şunlardır: segmentasyonsuz modelin kullandığı sinyalin niteliğini belirlemek amacıyla çekim meta-verisi (poz, cihaz, pozlama) ile kontrollü analizler yapılması; hasta düzeyinde ayrık ve augmentasyon içermeyen bir bölmeyle tüm kolların yeniden eğitilmesi; tohum sayısının artırılarak etki kestiriminin daraltılması; maske payı parametrelerinin duyarlılık analizi; ve modelin prospektif, uzman radyolog mutabakat etiketli veriyle alt gruplara ayrıştırılmış biçimde değerlendirilmesi. Bu çalışma bir karar-destek prototipi niteliğindedir; klinik kullanım, uzman denetimi ve düzenleyici onay gerektirir.

**KAYNAKLAR**

Samira Abnar and Willem Zuidema. 2020. Quantifying Attention Flow in Transformers. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics,* pages 4190–4197, Online. Association for Computational Linguistics.

DeGrave, A.J., Janizek, J.D. & Lee, SI. AI for radiographic COVID-19 detection selects shortcuts over signal. *Nat Mach Intell* **3**, 610–619 (2021). [https://doi.org/10.1038/s42256-021-00338-7](https://doi.org/10.1038/s42256-021-00338-7)

DeLong, E. R., DeLong, D. M. ve Clarke-Pearson, D. L. (1988). Comparing the areas under two or more correlated receiver operating characteristic curves: A nonparametric approach. *Biometrics*, 44(3), 837-845.

Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., … Houlsby, N. (2021). An image is worth 16x16 words: Transformers for image recognition at scale. *International Conference on Learning Representations (ICLR).*

Gaggion, N., Mosquera, C., Mansilla, L. et al. CheXmask: a large-scale dataset of anatomical segmentation masks for multi-center chest x-ray images. *Sci Data* 11, 511 (2024). [https://doi.org/10.1038/s41597-024-03358-1](https://doi.org/10.1038/s41597-024-03358-1)

Geirhos, Robert & Jacobsen, Jörn-Henrik & Michaelis, Claudio & Zemel, Richard & Brendel, Wieland & Bethge, Matthias & Wichmann, Felix. (2020). Shortcut learning in deep neural networks. *Nature Machine Intelligence*. 2. 665-673. 10.1038/s42256-020-00257-z.

Kermany DS, Goldbaum M, Cai W, Valentim CCS, Liang H, Baxter SL, McKeown A, Yang G, Wu X, Yan F, Dong J, Prasadha MK, Pei J, Ting MYL, Zhu J, Li C, Hewett S, Dong J, Ziyar I, Shi A, Zhang R, Zheng L, Hou R, Shi W, Fu X, Duan Y, Huu VAN, Wen C, Zhang ED, Zhang CL, Li O, Wang X, Singer MA, Sun X, Xu J, Tafreshi A, Lewis MA, Xia H, Zhang K. Identifying Medical Diagnoses and Treatable Diseases by Image-Based Deep Learning. *Cell*. 2018 Feb 22;172(5):1122-1131.e9. doi: 10.1016/j.cell.2018.02.010. PMID: 29474911.

Rajpurkar, Pranav & Irvin, Jeremy & Zhu, Kaylie & Yang, Brandon & Mehta, Hershel & Duan, Tony & Ding, Daisy & Bagul, Aarti & Langlotz, Curtis & Shpanskaya, Katie & Lungren, Matthew & Ng, Andrew. (2017). CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning. 10.48550/arXiv.1711.05225.

Ross, A. S., Hughes, M. C. ve Doshi-Velez, F. (2017). Right for the right reasons: Training differentiable models by constraining their explanations. *Proceedings of the 26th International Joint Conference on Artificial Intelligence* (IJCAI), 2662-2670.

Wang, X., Peng, Y., Lu, L., Lu, Z., Bagheri, M. ve Summers, R. M. (2017). ChestX-ray8: Hospital-scale chest X-ray database and benchmarks on weakly-supervised classification and localization of common thorax diseases. *IEEE Conference on Computer Vision and Pattern Recognition* (CVPR), 2097-2106.

Zeiler, M. D. ve Fergus, R. (2014). Visualizing and understanding convolutional networks. *European Conference on Computer Vision* (ECCV), 818-833.

**EKLER**

**EK-1. Model ve Eğitim Hiperparametreleri**

| Temel mimari | ViT-B/16 (ImageNet ön-eğitimli) |
| :---- | :---- |
| **İnce ayar** | Son 2 kodlayıcı bloğu + katman normalizasyonu + sınıflandırma başlığı |
| **Eğitilebilir parametre** | 14.178.818 / 85.800.194 (%16,5) |
| **Girdi boyutu** | 224 × 224 (3 kanal) |
| **Normalizasyon** | Ortalama 0,4769 / standart sapma 0,2414 |
| **Kayıp fonksiyonu** | Çapraz entropi (ceza terimi yok) |
| **Optimize edici** | AdamW (lr 1e-4, wd 1e-2), kosinüs çizelge → 1e-6 |
| **Dönem / yığın** | 15 / 16 |
| **Veri artırma** | Yatay çevirme 0,5; döndürme 8°; öteleme 0,04; ölçek 0,95-1,05; parlaklık-kontrast 0,15 |
| **Maske genişletme / RoI payı** | %2,5 / %5 |
| **Kenar yumuşatma / dolgu** | Gauss (k=9) / ortalama gri (122) |
| **Segmentasyon modeli** | CheXmask tabanlı U-Net (kalp hariç) |
| **Model seçimi** | En iyi doğrulama F1 |

**EK-2. Veri Kümeleri ve Bölme Bilgileri**

Eğitim verisi, Kermany ve diğerleri (2018) pediatrik göğüs radyografisi kümesinin kamuya açık dengelenmiş bir türevidir (8.530 görüntü; NORMAL 4.265, PNEUMONIA 4.265). Türev kümenin NORMAL sınıfı 1.575 kaynak görüntüden augmentasyonla çoğaltılmıştır (§4.1). Bölmeler: eğitim 6.800, doğrulama 864, test 864. Bölmelerin içerik imzaları (MD5) sırasıyla `ccf23597ec992137`, `779ac7f6455a7ac8` ve `3a25cbb40ab471d7` olup tüm çalışmalarda otomatik olarak doğrulanmıştır. Dış doğrulamada RSNA Pneumonia Detection Challenge ve NIH ChestX-ray14 kümeleri kullanılmıştır.

**EK-3. Yeniden Üretilebilirlik**

Tüm deneyler ayrı ayrı yürütülebilen betikler halinde düzenlenmiştir. Eğitilen model ve tüm ön-işleme parametreleri tek bir kontrol noktasında saklanmış; sonraki tüm çalışmalar bu kontrol noktasından hattı birebir yeniden kurmuştur. Veri bölmesi her çalışmada aynı kodla yeniden üretilmiş ve içerik imzalarıyla doğrulanmıştır.

| Çalışma | İçerik | Süre |
| :---- | :---- | :---- |
| Akciğer-odaklı eğitim | Önerilen hattın eğitimi ve iç değerlendirmesi | ≈ 80 dk |
| Dış doğrulama | RSNA ve NIH üzerinde çıkarım, kalibrasyon | ≈ 6 dk |
| Kontrollü ablasyon | Üç kolun özdeş koşullarda eğitimi | ≈ 3,8 sa |
| Örneklem gücü | Genişletilmiş dış örneklemde yeniden değerlendirme | ≈ 15 dk |
| Çoklu tohum | Üç eğitim tohumuyla tekrar, gürültü tabanı | ≈ 7 sa |
| Dış akciğer-odak analizi | Bağımsız kümelerde LFR ve toplu dikkat | ≈ 12 dk |
| Veri bütünlük denetimi | Sızıntı, kopya ve köken analizi | ≈ 6 dk |
| Sızıntısız iç test | Kaynak/hasta düzeyi ayrık alt kümede değerlendirme | ≈ 8 dk |
| Oklüzyon testi | Nedensel bölge analizi | ≈ 15 dk |

**ÖZGEÇMİŞ**
