import streamlit as st
import pandas as pd
import json

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Matematik, Hikmet ve Kâinat Ölçüsü | Math, Wisdom & Universal Measure",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Özel CSS İle Şık Tasarım ve Metin Kopyalama Koruması
st.markdown("""
<style>
    .main-title {
        color: #1e3d59;
        font-family: 'Georgia', serif;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        color: #17b978;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .quote-card {
        background-color: #f8f9fa;
        border-left: 5px solid #1e3d59;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .badge-ayet { background-color: #d4edda; color: #155724; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
    .badge-hadis { background-color: #cce5ff; color: #004085; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
    .badge-alim { background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
    .badge-bediuzzaman { background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
    .source-text {
        color: #6c757d;
        font-size: 0.9rem;
        font-style: italic;
        margin-top: 10px;
    }
    /* Metinlerin kopyalanmasını ve seçilmesini engelleyen güvenlik katmanı */
    body, .stApp {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Dil Tercihi Yan Menüden Alınır
st.sidebar.title("🌐 Dil / Language")
dil = st.sidebar.selectbox("Arayüz Dili / Interface Language", ["Türkçe", "English"])

# Çeviri Sözlükleri
texts = {
    "tr": {
        "title": "📐 Matematik, Hikmet ve Kâinat Ölçüsü",
        "subtitle": "Kur'an (Diyanet Meali), Hadis, İslam Alimleri ve Bediüzzaman'ın Perspektifinden Kâinatın Matematiksel Nizamı",
        "search_header": "🔍 Filtreleme ve Arama",
        "select_cat": "Kategori Seçin:",
        "search_placeholder": "Örn: kader, mizan, cebir, sayı...",
        "total_records": "Toplam Kayıt",
        "ayets": "Ayetler",
        "hadiths": "Hadisler",
        "scholars": "Alimler & Veliler",
        "said_nursi": "Bediüzzaman",
        "no_result": "Aramanıza uygun kayıt bulunamadı.",
        "sleep_info": "💡 *Not:* Bu web uygulaması ücretsiz sunucularda barındırılmaktadır. Uzun süre işlem yapılmadığında uygulama uyku moduna geçebilir (ekranda 'Zzzz' simgesi çıkabilir).\n\n💤 Eğer böyle bir ekranla karşılaşırsanız, ekranda beliren mavi renkli *'Yes, get this app back up!'* butonuna tıklayın ve uygulamanın yeniden uyanması için 15-30 saniye bekleyin.",
        "footer": "Matematik ve Hikmet Külliyatı Arşivi © 2026. Her hakkı saklıdır. Ticari olarak kullanılamaz. Ayetler Diyanet İşleri Başkanlığı mealinden alınmıştır."
    },
    "en": {
        "title": "📐 Mathematics, Wisdom & Universal Measure",
        "subtitle": "The Mathematical Order of the Universe from the Perspective of Quran (Diyanet Translation), Hadith, Islamic Scholars, and Bediuzzaman",
        "search_header": "🔍 Filtering & Search",
        "select_cat": "Select Category:",
        "search_placeholder": "E.g., destiny, measure, algebra...",
        "total_records": "Total Records",
        "ayets": "Verses",
        "hadiths": "Hadiths",
        "scholars": "Scholars & Saints",
        "said_nursi": "Bediuzzaman",
        "no_result": "No matching records found.",
        "sleep_info": "💡 *Note:* This web application is hosted on free servers. When left inactive for a long time, the app may go to sleep mode (a 'Zzzz' icon may appear on the screen).\n\n💤 If you encounter such a screen, click the blue button that says *'Yes, get this app back up!'* on the screen and wait 15-30 seconds for the app to wake up.",
        "footer": "Mathematics and Wisdom Archive © 2026. All rights reserved. Non-commercial use only. Verses are taken from Diyanet Affairs translation."
    }
}

t = texts["tr"] if dil == "Türkçe" else texts["en"]

# Kenar Çubuğuna Bilgi Notu ve Uyku Modu Yönlendirmesi Ekleme
st.sidebar.markdown("---")
st.sidebar.info(t['sleep_info'])

# --- MASTER VERİ SETİ (1-80 Liste) ---
if 'master_data' not in st.session_state:
    st.session_state.master_data = [
        # Ayetler (1-20)
        {
            "id": 1, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Kâinattaki Ölçü ve Kader", "baslik_en": "Universal Measure and Destiny",
            "icerik_tr": "Şüphesiz biz her şeyi bir ölçüye göre yarattık.",
            "icerik_en": "Indeed, all things We created with a determined measure.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Kamer Sûresi, 54:49",
            "kaynak_en": "Diyanet Affairs Translation - Quran 54:49",
            "hikmet_tr": "Kâinatın temelinde tesadüf değil, hassas bir matematiksel ölçü vardır.",
            "hikmet_en": "At the core of the universe lies a precise mathematical measure, not coincidence."
        },
        {
            "id": 2, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Varlıkların Sayısal Hesabı", "baslik_en": "Numerical Calculation of Entities",
            "icerik_tr": "Çünkü Allah onların nezdinde bulunanları ilmiyle kuşatmış ve her şeyi bir bir saymıştır.",
            "icerik_en": "And He has encompassed what is with them and has enumerated all things in number.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Cin Sûresi, 72:28",
            "kaynak_en": "Diyanet Affairs Translation - Quran 72:28",
            "hikmet_tr": "İlahî ilim, varlıklar âlemindeki her şeyi nicelik ve sayılarıyla kuşatmıştır.",
            "hikmet_en": "Divine knowledge encompasses every entity in the realm of existence along with its quantities."
        },
        {
            "id": 3, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Hassas Mizan ve Ölçü", "baslik_en": "Precise Balance and Quantity",
            "icerik_tr": "Hiçbir şey yoktur ki hazineleri bizim katımızda olmasın. Biz onu ancak belli bir ölçüye göre indiririz.",
            "icerik_en": "And there is not a thing but that with Us are its depositories, and We do not send it down except according to a known measure.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Hicr Sûresi, 15:21",
            "kaynak_en": "Diyanet Affairs Translation - Quran 15:21",
            "hikmet_tr": "Maddenin miktar ve ölçüleri ilahî takdirin bir matematiğidir.",
            "hikmet_en": "The quantities and measures of matter constitute the mathematics of divine decree."
        },
        {
            "id": 4, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Güneş ve Ay'ın Matematiksel Hesabı", "baslik_en": "Mathematical Calculation of Sun and Moon",
            "icerik_tr": "Güneş ve ay bir hesaba göre hareket etmektedir.",
            "icerik_en": "The sun and the moon move by precise calculation.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Rahmân Sûresi, 55:5",
            "kaynak_en": "Diyanet Affairs Translation - Quran 55:5",
            "hikmet_tr": "Gök cisimlerinin hareketi hassas astronomik hesaplara bağlıdır.",
            "hikmet_en": "The movement of celestial bodies depends on precise astronomical calculations."
        },
        {
            "id": 5, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Bütün Varlıkların Teker Teker Sayılması", "baslik_en": "Counting of All Beings Individually",
            "icerik_tr": "Andolsun ki Allah onları kuşatmış ve teker teker saymıştır.",
            "icerik_en": "Verily, He has enumerated them and counted them a full counting.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Meryem Sûresi, 19:94",
            "kaynak_en": "Diyanet Affairs Translation - Quran 19:94",
            "hikmet_tr": "Cüz'î ve küllî her bir varlık ilahî adalet istatistiğinde kayıtlıdır.",
            "hikmet_en": "Every particular and universal entity is recorded in the statistics of divine justice."
        },
        {
            "id": 6, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Yılların Sayısı ve Hesap", "baslik_en": "Number of Years and Calculation",
            "icerik_tr": "Biz geceyi ve gündüzü iki alamet kıldık... ki yılların sayısını ve hesabı bilesiniz.",
            "icerik_en": "We made the night and the day two signs... that you may know the number of years and the calculation of time.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - İsrâ Sûresi, 17:12",
            "kaynak_en": "Diyanet Affairs Translation - Quran 17:12",
            "hikmet_tr": "Zamanın ölçülmesi ve takvim matematiği insanlığa sunulmuş bir lütuftur.",
            "hikmet_en": "The measurement of time and calendar mathematics is a blessing offered to humanity."
        },
        {
            "id": 7, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Yedi Kat Göklerin Orantısı", "baslik_en": "Proportion of Seven Heavens",
            "icerik_tr": "O, birbiriyle uyumlu yedi gök yaratmıştır. Rahman'ın yaratmasında hiçbir uyumsuzluk göremezsin.",
            "icerik_en": "He who created seven heavens in layers. You do not see in the creation of the Most Merciful any inconsistency.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Mülk Sûresi, 67:3",
            "kaynak_en": "Diyanet Affairs Translation - Quran 67:3",
            "hikmet_tr": "Kâinattaki kozmik mimari kusursuz bir simetri ve orantı üzerinedir.",
            "hikmet_en": "The cosmic architecture in the universe is built on flawless symmetry and proportion."
        },
        {
            "id": 8, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Yeryüzünün Sabit Ölçüleri", "baslik_en": "Fixed Measurements of the Earth",
            "icerik_tr": "Yeryüzünü döşedik, orada ölçülü ve dengeli her şeyden bitirdik.",
            "icerik_en": "And the earth We have spread out and caused to grow therein every well-balanced thing.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Hicr Sûresi, 15:19",
            "kaynak_en": "Diyanet Affairs Translation - Quran 15:19",
            "hikmet_tr": "Jeolojik yapılar ve ağırlık merkezleri matematiksel birer dengedir.",
            "hikmet_en": "Geological structures and centers of gravity represent mathematical balances."
        },
        {
            "id": 9, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Her Şeyin Çiftler Halinde Yaratılması", "baslik_en": "Creation of Everything in Pairs",
            "icerik_tr": "Düşünesiniz diye her şeyden ikişer çift yarattık.",
            "icerik_en": "And of all things We created two mates; perhaps you will remember.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Zâriyât Sûresi, 51:49",
            "kaynak_en": "Diyanet Affairs Translation - Quran 51:49",
            "hikmet_tr": "Kâinattaki simetri, ikili kodlar ve zıtlıklar matematiğin temel yasasıdır.",
            "hikmet_en": "Symmetry, binary codes, and dualities in the universe are foundational laws of mathematics."
        },
        {
            "id": 10, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Göklerin ve Yerin Adalet Terazisi", "baslik_en": "Balance of Heavens and Earth",
            "icerik_tr": "Göğü yükseltti ve mizanı koydu. Sakın tartıda taşkınlık etmeyin.",
            "icerik_en": "And the heaven He raised and imposed the balance that you not transgress within the balance.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Rahmân Sûresi, 55:7-8",
            "kaynak_en": "Diyanet Affairs Translation - Quran 55:7-8",
            "hikmet_tr": "Evrenin her köşesinde mutlak bir matematiksel denge ve adalet kanunu hükder.",
            "hikmet_en": "An absolute law of mathematical balance and justice reigns in every corner of the universe."
        },
        {
            "id": 11, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Gece ve Gündüzün Matematiksel Takibi", "baslik_en": "Mathematical Tracking of Night and Day",
            "icerik_tr": "Şüphesiz göklerin ve yerin yaratılışında, gece ile gündüzün birbiri ardınca gelmesinde akıl sahipleri için deliller vardır.",
            "icerik_en": "Indeed, in the creation of the heavens and the earth and the alternation of the night and the day are signs for those of understanding.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Âl-i İmrân Sûresi, 3:190",
            "kaynak_en": "Diyanet Affairs Translation - Quran 3:190",
            "hikmet_tr": "Zamanın periyodik döngüleri akıl ve hesap sahipleri için ilahî tablolardır.",
            "hikmet_en": "Periodic cycles of time are divine tables for those endowed with reason and calculation."
        },
        {
            "id": 12, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Maddelerin Ağırlık ve Hacim Ölçüsü", "baslik_en": "Weight and Volume Measure of Matter",
            "icerik_tr": "Biz yerde her şeyi belli bir ölçüye göre bitirdik.",
            "icerik_en": "And We caused to grow therein things of every kind in a balanced manner.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Hicr Sûresi, 15:19",
            "kaynak_en": "Diyanet Affairs Translation - Quran 15:19",
            "hikmet_tr": "Biyolojik ve kimyasal bileşimler kesin oran kanunlarına tabidir.",
            "hikmet_en": "Biological and chemical compositions are subject to strict laws of proportion."
        },
        {
            "id": 13, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Yağmurun Ölçülü ve Hesaplı İndirilmesi", "baslik_en": "Measured and Calculated Descent of Rain",
            "icerik_tr": "Gökten belli bir ölçüye göre suyu indiren O'dur.",
            "icerik_en": "And who sends down rain from the sky in a measured amount.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Zuhruf Sûresi, 43:11",
            "kaynak_en": "Diyanet Affairs Translation - Quran 43:11",
            "hikmet_tr": "Hidrolojik döngü ve yağış miktarları istatistiki birer nizamdır.",
            "hikmet_en": "The hydrological cycle and precipitation amounts constitute a statistical order."
        },
        {
            "id": 14, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Göklerin Direksiz Kurulması", "baslik_en": "Establishment of Heavens Without Pillars",
            "icerik_tr": "Allah, gökleri gördüğünüz direkler olmaksızın yükseltendir.",
            "icerik_en": "It is Allah who erected the heavens without pillars that you can see.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Ra'd Sûresi, 13:2",
            "kaynak_en": "Diyanet Affairs Translation - Quran 13:2",
            "hikmet_tr": "Kütle çekim yasaları ve görünmez fiziksel kuvvetler ilahî matematiğin tezahürüdür.",
            "hikmet_en": "Laws of gravitation and invisible physical forces are manifestations of divine mathematics."
        },
        {
            "id": 15, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Rüzgarların Hesaplı Sevk Edilmesi", "baslik_en": "Calculated Directing of Winds",
            "icerik_tr": "Rüzgarların çevrilmesinde, gök ile yer arasında emre amade bekleyen bulutlarda akıl sahipleri için deliller vardır.",
            "icerik_en": "And in the directing of the winds and the clouds driven between the heaven and the earth are signs for people who use reason.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Bakara Sûresi, 2:164",
            "kaynak_en": "Diyanet Affairs Translation - Quran 2:164",
            "hikmet_tr": "Atmosferik basınç ve hava akımları matematiksel denklemlerle işler.",
            "hikmet_en": "Atmospheric pressure and air currents operate via mathematical equations."
        },
        {
            "id": 16, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Ecelin Belirli Bir Sayıyla Tayini", "baslik_en": "Determination of Term by Specific Number",
            "icerik_tr": "Biz onları ancak belirli bir süreye kadar erteliyoruz.",
            "icerik_en": "And We do not delay it except for a limited term.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Mü'minûn Sûresi, 23:43",
            "kaynak_en": "Diyanet Affairs Translation - Quran 23:43",
            "hikmet_tr": "Ömürler ve tarihsel süreçler kesin sayısal sınırlara tabidir.",
            "hikmet_en": "Lifespans and historical processes are subject to precise numerical limits."
        },
        {
            "id": 17, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Cennetlerin Genişlik Ölçüsü", "baslik_en": "Spatial Measure of Paradises",
            "icerik_tr": "Rabbinizin bağışına ve genişliği göklerle yer kadar olan cennete koşun.",
            "icerik_en": "And hasten to forgiveness from your Lord and a garden as wide as the heavens and the earth.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Âl-i İmrân Sûresi, 3:133",
            "kaynak_en": "Diyanet Affairs Translation - Quran 3:133",
            "hikmet_tr": "Ahiret alemlerinin boyutları da insan idrakine ölçü olması için uzamsal terimlerle ifade edilmiştir.",
            "hikmet_en": "The dimensions of hereafter realms are expressed in spatial terms as a measure for human comprehension."
        },
        {
            "id": 18, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Meleklerin Sayısal Orduları", "baslik_en": "Numerical Hosts of Angels",
            "icerik_tr": "Rabbinin ordularını ancak Kendisi bilir.",
            "icerik_en": "And none knows the soldiers of your Lord except Him.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Müddessir Sûresi, 74:31",
            "kaynak_en": "Diyanet Affairs Translation - Quran 74:31",
            "hikmet_tr": "Kâinattaki varlık kademelerinin ve melekî vazifelendirmelerin sonsuz istatistiği.",
            "hikmet_en": "The infinite statistics of existential tiers and angelic duties in the universe."
        },
        {
            "id": 19, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "İnsanın Nutüfeden Hesaplı Evresi", "baslik_en": "Calculated Stages of Human Embryology",
            "icerik_tr": "Sonra onu az bir su halinde sağlam bir karar yerine yerleştirdik.",
            "icerik_en": "Then We placed him as a drop in a firm lodging.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Mü'minûn Sûresi, 23:13",
            "kaynak_en": "Diyanet Affairs Translation - Quran 23:13",
            "hikmet_tr": "Embriyolojik gelişim aşamaları tam zamanlı ve haftalık matematiksel süreçlerdir.",
            "hikmet_en": "Embryological developmental stages are time-bound, weekly mathematical processes."
        },
        {
            "id": 20, "kategori_tr": "Ayet-i Kerime", "kategori_en": "Quranic Verse",
            "baslik_tr": "Defterlerin Hiçbir Şeyi Atlamayan Kaydı", "baslik_en": "Record of Deeds Omitting Nothing",
            "icerik_tr": "Küçük büyük hiçbir şey bırakmaksızın hepsini sayıp dökmüştür.",
            "icerik_en": "It leaves nothing small or great except that it has enumerated it.",
            "kaynak_tr": "Diyanet İşleri Başkanlığı Meali - Kehf Sûresi, 18:49",
            "kaynak_en": "Diyanet Affairs Translation - Quran 18:49",
            "hikmet_tr": "Kâinatta hiçbir amel ve enerji kaybolmaz, mutlak bir bilgi arşivinde saklanır.",
            "hikmet_en": "No action or energy is lost in the universe; all is statistically stored."
        },
        
        # Hadisler (21-40)
        {
            "id": 21, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Hesap Gününün İstatistiki Muhasebesi", "baslik_en": "Statistical Account of Judgment Day",
            "icerik_tr": "Kıyamet gününde hiçbir kul, ömründen, ilminden, malından hesaba çekilmedikçe adım atamaz.",
            "icerik_en": "No servant will step forward on the Day of Judgment until he is asked about his life, knowledge, and wealth.",
            "kaynak_tr": "Tirmizî, Kıyamet 1 / Tirmidhi 2417",
            "kaynak_en": "Tirmidhi, Qiyamah 1 / Tirmidhi 2417",
            "hikmet_tr": "Hayat, sonuçları adalet terazisinde net rakamlarla önümüze konulacak bir hesaptır.",
            "hikmet_en": "Life is an account whose results will be presented with clear figures on the scale of justice."
        },
        {
            "id": 22, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Miras Matematiği (Ferâiz İlimi)", "baslik_en": "Mathematics of Inheritance (Faraid)",
            "icerik_tr": "Ferâiz ilmini öğrenin ve insanlara öğretin. Çünkü o ilmin yarısıdır.",
            "icerik_en": "Learn the laws of inheritance and teach them to people, for it is half of knowledge.",
            "kaynak_tr": "İbn Mâce, Ferâiz 1 / Ibn Majah",
            "kaynak_en": "Ibn Majah, Faraid 1 / Ibn Majah",
            "hikmet_tr": "Kur'an'daki hisselerin doğru dağıtılması matematiğe tam hâkimiyeti gerektirir.",
            "hikmet_en": "Proper distribution of shares in the Quran requires complete mastery of mathematics."
        },
        {
            "id": 23, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "İbadetlerdeki Miktar Ölçüsü (Kulleteyn)", "baslik_en": "Volume Measure in Worship (Qullatayn)",
            "icerik_tr": "Su iki kulle (yaklaşık 200 litre) miktarına ulaşınca kir tutmaz.",
            "icerik_en": "When water reaches the amount of two qullas, it does not carry impurity.",
            "kaynak_tr": "Ebu Davud, Taharet 33 / Abu Dawud 63",
            "kaynak_en": "Abu Dawud, Taharah 33 / Abu Dawud 63",
            "hikmet_tr": "Fıkhi hükümlerde fiziksel hacim ve miktar matematiği esastır.",
            "hikmet_en": "Physical volume and quantity mathematics are essential in jurisprudential rulings."
        },
        {
            "id": 24, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Ay ve Zaman Hesabı", "baslik_en": "Calculation of Moon and Time",
            "icerik_tr": "Biz ümmî bir ümmetiz; yazı yazmayız, hesap yapmayız. Ay şöyledir (bazen 29, bazen 30 gündür).",
            "icerik_en": "We are an unlettered nation; we neither write nor calculate. The month is thus and thus (29 or 30 days).",
            "kaynak_tr": "Buhârî, Savm 13 / Bukhari",
            "kaynak_en": "Bukhari, Sawm 13 / Bukhari",
            "hikmet_tr": "Kameri takvimin ve ay döngülerinin gün hesabı üzerindeki pratik karşılığı.",
            "hikmet_en": "The practical correspondence of lunar calendars and moon cycles on day counts."
        },
        {
            "id": 25, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Amellerin Sayısal Değeri (Sevap Hesabı)", "baslik_en": "Numerical Value of Deeds (Reward Calculation)",
            "icerik_tr": "Ameller niyetlere göredir. Herkese niyet ettiği şey vardır.",
            "icerik_en": "Deeds are judged by intentions, and every person will get what they intended.",
            "kaynak_tr": "Buhârî, Bed'ül-Vahy 1 / Bukhari 1",
            "kaynak_en": "Bukhari, Bad' al-Wahy 1 / Bukhari 1",
            "hikmet_tr": "Maneviyat âleminde niyet, amelin katsayısını ve kat kat artış oranını belirler.",
            "hikmet_en": "In the spiritual realm, intention determines the coefficient and multiplier rate of deeds."
        },
        {
            "id": 26, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Sadakanın 700 Kat Artış Matematiği", "baslik_en": "Mathematics of 700-Fold Increase in Charity",
            "icerik_tr": "Bir hurma tanesi kadarcık sadakayı Allah dağ gibi büyütür...",
            "icerik_en": "Allah nurtures charity as one of you raises his foal, until it becomes like a mountain.",
            "kaynak_tr": "Buhârî, Zekât 8 / Bukhari",
            "kaynak_en": "Bukhari, Zakat 8 / Bukhari",
            "hikmet_tr": "İnfak matematiğinde bire bin veren ilahî bereket denklemi vardır.",
            "hikmet_en": "In the mathematics of charity, there is a divine abundance equation yielding manifold returns."
        },
        {
            "id": 27, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Tövbe Kapısının Sayısal Genişliği", "baslik_en": "Numerical Vastness of Repentance",
            "icerik_tr": "Güneş batıdan doğmadıkça Allah tövbeyi kabul eder.",
            "icerik_en": "Allah accepts the repentance of His servant so long as the death rattle has not begun.",
            "kaynak_tr": "Tirmizî, Dehât 98 / Tirmidhi",
            "kaynak_en": "Tirmidhi / Tirmidhi",
            "hikmet_tr": "Zaman sınırları içinde sunulan ilahî rahmetin istatistiki esnekliği.",
            "hikmet_en": "The statistical flexibility of divine mercy offered within temporal boundaries."
        },
        {
            "id": 28, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Cennetin 8 Kapısının Genişliği", "baslik_en": "Width of Paradise's Eight Gates",
            "icerik_tr": "Cennetin kapılarından ikisi arasındaki mesafe kırk yıllık yoldur.",
            "icerik_en": "The distance between two gates of Paradise is a journey of forty years.",
            "kaynak_tr": "Müslim, Zekât 36 / Muslim",
            "kaynak_en": "Muslim, Zakat 36 / Muslim",
            "hikmet_tr": "Öte alemin boyutları insana manevi genişliği anlatmak için mesafe kavramıyla ölçülendirilir.",
            "hikmet_en": "The dimensions of the afterlife are measured in distance concepts to convey spiritual vastness."
        },
        {
            "id": 29, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Zikirlerin Sayısal Tespihatı", "baslik_en": "Numerical Rosary of Remembrances",
            "icerik_tr": "Kim namazdan sonra 33 defa Sübhanallah, 33 Elhamdülillah, 33 Allahu Ekber derse...",
            "icerik_en": "Whoever glorifies Allah 33 times, praises Him 33 times, and magnifies Him 33 times after every prayer...",
            "kaynak_tr": "Müslim, Mesâcid 146 / Muslim",
            "kaynak_en": "Muslim, Masajid 146 / Muslim",
            "hikmet_tr": "Manevi derecelerin kazanılmasında belirli sayılara riayet etmek sünnettir.",
            "hikmet_en": "Observing specific numbers in acquiring spiritual ranks is part of the Sunnah."
        },
        {
            "id": 30, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Ömrün Sınırları ve 60-70 Yaş Dilimi", "baslik_en": "Limits of Lifespan and the 60-70 Age Bracket",
            "icerik_tr": "Ümmetimin ömrü 60 ile 70 yıl arasındadır; bundan ileri geçen çok azdır.",
            "icerik_en": "The lifespan of my ummah is between sixty and seventy years, and few exceed that.",
            "kaynak_tr": "Tirmizî, Daavât 102 / Tirmidhi",
            "kaynak_en": "Tirmidhi, Da'awat 102 / Tirmidhi",
            "hikmet_tr": "İnsan ömrünün istatistiki ortalaması nebevi beyanla önceden haber verilmiştir.",
            "hikmet_en": "The statistical average of human lifespan was foretold by prophetic statement."
        },
        {
            "id": 31, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Cemaatle Namazın 27 Derece Kat Sayısı", "baslik_en": "27-Fold Coefficient of Congregational Prayer",
            "icerik_tr": "Cemaatle kılınan namaz, tek başına kılınan namazdan 27 derece daha faziletlidir.",
            "icerik_en": "Prayer in congregation is twenty-seven degrees more superior than prayer performed individually.",
            "kaynak_tr": "Buhârî, Ezan 30 / Bukhari",
            "kaynak_en": "Bukhari, Adhan 30 / Bukhari",
            "hikmet_tr": "Toplumsal ibadette manevi kazancın matematiksel katlanma oranı.",
            "hikmet_en": "The mathematical multiplier rate of spiritual gain in communal worship."
        },
        {
            "id": 32, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Hac İbadetinin Sayısal Ölçüleri", "baslik_en": "Numerical Measures of Pilgrimage (Hajj)",
            "icerik_tr": "Hac Arafat'tır.",
            "icerik_en": "Hajj is Arafat.",
            "kaynak_tr": "Ebu Davud, Menasik 57 / Abu Dawud",
            "kaynak_en": "Abu Dawud, Manasik 57 / Abu Dawud",
            "hikmet_tr": "Belirli bir gün ve saatte belirli bir yerde toplanmanın zaman matematiği.",
            "hikmet_en": "The time mathematics of gathering at a specific place on a specific day and hour."
        },
        {
            "id": 33, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Sadaka-i Cariye Kesintisiz İstatistik", "baslik_en": "Continuous Statistics of Ongoing Charity",
            "icerik_tr": "İnsan ölünce amelleri kesilir; ancak üç şey hariç: Sadaka-i cariye, faydalı ilim...",
            "icerik_en": "When a person dies, their deeds end except for three: ongoing charity, beneficial knowledge...",
            "kaynak_tr": "Müslim, Vasiyet 14 / Muslim",
            "kaynak_en": "Muslim, Wasiyyah 14 / Muslim",
            "hikmet_tr": "İyiliklerin geometrik artışla ve sonsuz döngüyle kulun defterine yazılmaya devam etmesi.",
            "hikmet_en": "The continuous recording of good deeds in the servant's ledger with geometric growth."
        },
        {
            "id": 34, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Cehennemin Derinlik Ölçüsü", "baslik_en": "Depth Measure of Hell",
            "icerik_tr": "Bir taş atılsa yetmiş yıl dibine ulaşamaz...",
            "icerik_en": "If a stone were thrown into Hell, it would fall for seventy years before reaching the bottom.",
            "kaynak_tr": "Müslim, Cennet 32 / Muslim",
            "kaynak_en": "Muslim, Jannah 32 / Muslim",
            "hikmet_tr": "Kozmik mesafeler ve azabın boyutları zihne ölçek vermek için sayılarla tasvir edilmiştir.",
            "hikmet_en": "Cosmic distances and dimensions of retribution are depicted with numbers to give scale."
        },
        {
            "id": 35, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Günde 70 Kez İstiğfar Matematiği", "baslik_en": "Mathematics of Seeking Forgiveness 70 Times Daily",
            "icerik_tr": "Vallahi ben günde yetmiş defadan fazla Allah'a tövbe ve istiğfar ederim.",
            "icerik_en": "By Allah, I seek Allah's forgiveness and repent to Him more than seventy times a day.",
            "kaynak_tr": "Buhârî, Daavât 3 / Bukhari",
            "kaynak_en": "Bukhari, Da'awat 3 / Bukhari",
            "hikmet_tr": "Manevi arınma ve kalbi temizleme sürecinin periyodik matematiksel tekrarı.",
            "hikmet_en": "The periodic mathematical repetition of spiritual purification and heart cleansing."
        },
        {
            "id": 36, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Rızkın Dağılım ve Zamanlama Oranı", "baslik_en": "Distribution and Timing Ratio of Sustenance",
            "icerik_tr": "Rızık, ecelin insanı takip etmesinden daha hızlı bir şekilde insanı takip eder.",
            "icerik_en": "Sustenance pursues a person more persistently than their death pursues them.",
            "kaynak_tr": "Taberânî, Mu'cemü'l-Kebîr / Tabarani",
            "kaynak_en": "Tabarani, Al-Mu'jam al-Kabir",
            "hikmet_tr": "Kozmik rızık sisteminin kusursuz istatistiki ve zamanlı sevkıyatı.",
            "hikmet_en": "The flawless statistical and timed dispatch of the cosmic sustenance system."
        },
        {
            "id": 37, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Cuma Günündeki Kabul Saati", "baslik_en": "The Accepted Hour on Friday",
            "icerik_tr": "Cuma gününde öyle bir saat vardır ki mümin kul o saatte dua ederse istedikleri verilir.",
            "icerik_en": "On Friday there is an hour in which a Muslim servant does not stand and pray asking Allah for something except that He gives it to him.",
            "kaynak_tr": "Buhârî, Cuma 37 / Bukhari",
            "kaynak_en": "Bukhari, Jumu'ah 37 / Bukhari",
            "hikmet_tr": "Zaman dilimlerinin matematiksel olarak özel ve bereketli odak noktaları.",
            "hikmet_en": "Mathematically special and blessed focal points within temporal segments."
        },
        {
            "id": 38, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Abdest Suyunun Miktar ve Ölçüsü", "baslik_en": "Amount and Measure of Ablution Water",
            "icerik_tr": "Peygamber efendimiz bir müd su ile abdest alır...",
            "icerik_en": "The Prophet performed ablution with a mudd of water...",
            "kaynak_tr": "Buhârî, Vudû 46 / Bukhari",
            "kaynak_en": "Bukhari, Wudu 46 / Bukhari",
            "hikmet_tr": "Temizlik ve ibadette israfı önleyen optimum fiziksel miktar matematiği.",
            "hikmet_en": "The optimum physical quantity mathematics preventing waste in purification and worship."
        },
        {
            "id": 39, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "Kadir Gecesinin Bin Aydan Üstünlük Oranı", "baslik_en": "Superiority Ratio of the Night of Decree over a Thousand Months",
            "icerik_tr": "Kadir gecesi bin aydan daha hayırlıdır.",
            "icerik_en": "The Night of Decree is better than a thousand months.",
            "kaynak_tr": "Kadr Sûresi, 3. Ayet / Hadis şerhi",
            "kaynak_en": "Quran 97:3 / Hadith Commentary",
            "hikmet_tr": "Zamanın bereketle katlanmasının ve manevi zaman kaldıraçlarının ilahî matematiği.",
            "hikmet_en": "The divine mathematics of temporal multiplication through blessings and spiritual levers."
        },
        {
            "id": 40, "kategori_tr": "Hadis-i Şerif", "kategori_en": "Hadith",
            "baslik_tr": "İbadette Az ve Devamlı Olanın Ölçüsü", "baslik_en": "Measure of Small and Consistent Deeds",
            "icerik_tr": "Amellerin en sevimlisi az da olsa devamlı olanıdır.",
            "icerik_en": "The most beloved deeds to Allah are those that are consistent, even if small.",
            "kaynak_tr": "Buhârî, Rikâk 18 / Bukhari",
            "kaynak_en": "Bukhari, Riqaq 18 / Bukhari",
            "hikmet_tr": "istikrar ve düzen matematiğinin manevi gelişimdeki kalıcı karşılığı.",
            "hikmet_en": "The enduring equivalent of stability and order mathematics in spiritual development."
        },

        # İslam Alimleri & Veliler (41-60)
        {
            "id": 41, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "El-Harezmi ve Cebir İlmi", "baslik_en": "Al-Khwarizmi and Algebra",
            "icerik_tr": "İnsanların miras, vasiyet, taksimat ve ticari muamelelerinde muhtaç oldukları hesap kolaylıklarını cebir metoduyla bir araya getirdim.",
            "icerik_en": "I compiled the computational conveniences needed by people in inheritance, wills, partitioning, and trade using the method of algebra.",
            "kaynak_tr": "El-Harezmi, El-Kitâbü'l-Muhtasar",
            "kaynak_en": "Al-Khwarizmi, Al-Kitab al-Mukhtasar",
            "hikmet_tr": "Matematik ve cebir, toplumsal adaleti korumanın en somut aracıdır.",
            "hikmet_en": "Mathematics and algebra are the most concrete tools for preserving social justice."
        },
        {
            "id": 42, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "İmam Gazali ve Geometrinin Berraklığı", "baslik_en": "Al-Ghazali and Geometric Clarity",
            "icerik_tr": "Matematiksel ispatları inceleyen kimse, akli delillerin kesinliğini anlar. Bu durum zihni safsatalardan korur.",
            "icerik_en": "Whoever examines mathematical proofs understands the certainty of rational arguments, protecting the mind from sophistry.",
            "kaynak_tr": "İmam Gazali, El-Munkızu mine'd-Dalâl",
            "kaynak_en": "Al-Ghazali, Al-Munqidh min al-Dalal",
            "hikmet_tr": "Geometri ve matematik akla disiplin kazandırır.",
            "hikmet_en": "Geometry and mathematics instill discipline in the mind."
        },
        {
            "id": 43, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "İbn Sina ve Sayıların Mefhumu", "baslik_en": "Avicenna and the Concept of Numbers",
            "icerik_tr": "Sayılar, varlığın formel yapısının ilahî zihindeki mükemmel akisleridir. Bütün fiziksel varlıklar matematiksel oranlarla kaimdir.",
            "icerik_en": "Numbers are perfect reflections of the formal structure of existence in the divine mind. All physical beings persist through mathematical ratios.",
            "kaynak_tr": "İbn Sina, Kitabü'ş-Şifa",
            "kaynak_en": "Avicenna, Kitab al-Shifa",
            "hikmet_tr": "Fizik âlemindeki tüm varlıklar soyut sayısal dengelerin somutlaşmış halleridir.",
            "hikmet_en": "All beings in the physical realm are materialized forms of abstract numerical balances."
        },
        {
            "id": 44, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "Ömer Hayyam ve Geometrik Denklemler", "baslik_en": "Omar Khayyam and Geometric Equations",
            "icerik_tr": "Cebir problemlerini ve kübik denklemleri konik kesirler geometri yardımıyla çözerek ilmi bir ileri aşamaya taşıdık.",
            "icerik_en": "We advanced science by solving algebraic problems and cubic equations with the help of conic section geometry.",
            "kaynak_tr": "Ömer Hayyam, Risale fi'l-Cebri ve'l-Mukâbele",
            "kaynak_en": "Omar Khayyam, Treatise on Algebra",
            "hikmet_tr": "Geometri, soyut denklemlerin somut görsel kanıtıdır.",
            "hikmet_en": "Geometry is the concrete visual proof of abstract equations."
        },
        {
            "id": 45, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "El-Farabi ve Seslerin Matematiksel Oranı", "baslik_en": "Al-Farabi and Mathematical Ratio of Sounds",
            "icerik_tr": "Musiki nağmeleri ve ses frekansları arasındaki matematiksel nisbetler ruh üzerinde derin bir uyum ve şifa tesiri icra eder.",
            "icerik_en": "Mathematical ratios between musical notes and sound frequencies exert a profound harmony and healing effect on the soul.",
            "kaynak_tr": "El-Farabi, Kitâbü'l-Mûsîkî el-Kebîr",
            "kaynak_en": "Al-Farabi, Kitab al-Musiqa al-Kabir",
            "hikmet_tr": "Sanat ve estetik bile matematiksel oranlara dayanır.",
            "hikmet_en": "Art and aesthetics are also grounded in mathematical proportions."
        },
        {
            "id": 46, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "İbn Haldun ve Hesap İlminin Medeniyetteki Yeri", "baslik_en": "Ibn Khaldun and the Place of Calculation in Civilization",
            "icerik_tr": "Hesap ve geometri ilmi, insan zihnini tedricî olarak mantıki düşünceye alıştırır ve dürüstlük melekesi kazandırır.",
            "icerik_en": "The science of calculation and geometry gradually trains the human mind in logical thinking and fosters a disposition of integrity.",
            "kaynak_tr": "İbn Haldun, Mukaddime",
            "kaynak_en": "Ibn Khaldun, Muqaddimah",
            "hikmet_tr": "Matematik disiplini ahlaki dürüstlüğü ve doğru mantık yürütmeyi besler.",
            "hikmet_en": "Mathematical discipline nurtures moral integrity and correct reasoning."
        },
        {
            "id": 47, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "Mevlana Celaleddin Rumi ve Nokta ile Daire Metaforu", "baslik_en": "Rumi and the Metaphor of Point and Circle",
            "icerik_tr": "Pergelin bir ayağı şeriat üzerinde sabitken, diğer ayağı yetmiş iki milleti daire gibi dolaşır.",
            "icerik_en": "One leg of the compass is fixed on the Sharia, while the other revolves around seventy-two nations like a circle.",
            "kaynak_tr": "Mevlana, Mesnevî",
            "kaynak_en": "Rumi, Mathnawi",
            "hikmet_tr": "Geometrik pergel metaforu ile hakikatin merkezi ve kuşatıcı evrenselliği anlatılmıştır.",
            "hikmet_en": "The geometric compass metaphor conveys the center and embracing universality of truth."
        },
        {
            "id": 48, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "Muhyiddin İbn Arabi ve Varlık Haritalarının Sayısal Sırları", "baslik_en": "Ibn Arabi and Numerical Secrets of Existence Maps",
            "icerik_tr": "Huruflar ve sayılar kâinatın şifreleridir. Her harfin sayısal değeri ilahî bir ismin tezahürünü gösterir.",
            "icerik_en": "Letters and numbers are the ciphers of the universe. The numerical value of each letter indicates the manifestation of a divine name.",
            "kaynak_tr": "Muhyiddin İbn Arabi, El-Fütûhâtü'l-Mekkiyye",
            "kaynak_en": "Ibn Arabi, Al-Futuhat al-Makkiyya",
            "hikmet_tr": "Kâinatın varlık haritası ontolojik bir matematik ve simya diliyle örülmüştür.",
            "hikmet_en": "The existence map of the universe is woven with an ontological language of mathematics and alchemy."
        },
        {
            "id": 49, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "Nasîrüddîn-i Tûsî ve Trigonometrik Nizam", "baslik_en": "Nasir al-Din al-Tusi and Trigonometric Order",
            "icerik_tr": "Astronomi ve küresel üçgenler üzerindeki hesaplamalarımız gök cisimlerinin yörüngelerini kusursuzca ortaya koyar.",
            "icerik_en": "Our calculations on astronomy and spherical triangles flawlessly reveal the orbits of celestial bodies.",
            "kaynak_tr": "Nasîrüddîn-i Tûsî, Şeklü'l-Kıttâ",
            "kaynak_en": "Nasir al-Din al-Tusi, Treatise on the Quadrilateral",
            "hikmet_tr": "Göklerin mekaniği trigonometrik yasalarla tanzim edilmiştir.",
            "hikmet_en": "The mechanics of the heavens are organized by trigonometric laws."
        },
        {
            "id": 50, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "İbnü'l-Haysem ve Optik Geometri", "baslik_en": "Ibn al-Haytham and Optical Geometry",
            "icerik_tr": "Işığın yayılma yasalarını ve yansıma açılarını geometri ve matematik kanunlarıyla ispat ettik.",
            "icerik_en": "We proved the laws of light propagation and angles of reflection using the laws of geometry and mathematics.",
            "kaynak_tr": "İbnü'l-Haysem, Kitâbü'l-Menâzır",
            "kaynak_en": "Ibn al-Haytham, Book of Optics",
            "hikmet_tr": "Fiziksel optik olayları tamamen geometrik hatlar ve açılarla işler.",
            "hikmet_en": "Physical optical phenomena operate entirely through geometric lines and angles."
        },
        {
            "id": 51, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "Birûnî ve Boylam-Enlem Hesapları", "baslik_en": "Al-Biruni and Longitude-Latitude Calculations",
            "icerik_tr": "Yeryüzünün yarıçapını ve şehirler arası mesafeleri astronomik matematik hesaplarıyla hassas bir şekilde ölçtük.",
            "icerik_en": "We precisely measured the Earth's radius and distances between cities using astronomical mathematical calculations.",
            "kaynak_tr": "Birûnî, Tahdîdü Nihâyâti'l-Emâkin",
            "kaynak_en": "Al-Biruni, The Determination of Coordinates of Cities",
            "hikmet_tr": "Coğrafya ilmi matematiksel ölçümlerle hakikat bulur.",
            "hikmet_en": "The science of geography finds truth through mathematical measurements."
        },
        {
            "id": 52, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "Cemşîd el-Kâşî ve Ondalık Kesirlerin Keşfi", "baslik_en": "Al-Kashi and the Discovery of Decimals",
            "icerik_tr": "Matematik işlemlerinde ondalık kesirleri sistemleştirerek hesaplamalardaki en büyük zorlukları ortadan kaldırdık.",
            "icerik_en": "We eliminated the greatest difficulties in calculations by systematizing decimal fractions in mathematics.",
            "kaynak_tr": "Cemşîd el-Kâşî, Miftâhu'l-Hisâb",
            "kaynak_en": "Al-Kashi, Miftah al-Hisab",
            "hikmet_tr": "Sayıların hassasiyeti medeniyetin pratik işlerini kolaylaştırır.",
            "hikmet_en": "The precision of numbers facilitates the practical affairs of civilization."
        },
        {
            "id": 53, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "Sabit bin Kurre ve Mekanik Oranlar", "baslik_en": "Thabit ibn Qurra and Mechanical Ratios",
            "icerik_tr": "Kantar ve mekanik kaldıraç sistemlerindeki ağırlık oranları geometri kanunlarına tam mutabakattadır.",
            "icerik_en": "Weight ratios in steelyards and mechanical lever systems are in exact conformity with the laws of geometry.",
            "kaynak_tr": "Sabit bin Kurre, Kitâp fi'l-Karasat",
            "kaynak_en": "Thabit ibn Qurra, Book on Balance",
            "hikmet_tr": "Mekanik ve fizik dünyası matematiksel kaldıraç oranlarıyla yönetilir.",
            "hikmet_en": "The mechanical and physical world is governed by mathematical leverage ratios."
        },
        {
            "id": 54, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "Akşemseddin ve Hücrelerin Sayısal Çoğalma Düzeni", "baslik_en": "Akshamsaddin and Numerical Multiplication Order of Cells",
            "icerik_tr": "Hastalıkların ve canlı dokuların gelişiminde görünmez tohumlar belirli sayısal oranlarla çoğalır.",
            "icerik_en": "In the development of diseases and living tissues, invisible seeds multiply in specific numerical ratios.",
            "kaynak_tr": "Akşemseddin, Mâddetü'l-Hayât",
            "kaynak_en": "Akshamsaddin, Maddat al-Hayat",
            "hikmet_tr": "Biyolojik yaşamın mikroskobik dünyasında da ilahî bir matematik vardır.",
            "hikmet_en": "A divine mathematics exists even in the microscopic world of biological life."
        },
        {
            "id": 55, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "İmam Şafii ve Fıkhi Hükümlerde Miktar", "baslik_en": "Imam Shafi'i and Quantity in Jurisprudence",
            "icerik_tr": "Şer'i delillerin ve ibadet vakitlerinin tayininde kesin sayısal ölçüler esas alınmıştır.",
            "icerik_en": "Precise numerical measures are established in determining legal proofs and times of worship.",
            "kaynak_tr": "İmam Şafii, Er-Risâle",
            "kaynak_en": "Imam Shafi'i, Al-Risala",
            "hikmet_tr": "İbadetlerin standardizasyonu için sayılar ve ölçüler kilit rol oynar.",
            "hikmet_en": "Numbers and measures play a key role in the standardization of worship."
        },
        {
            "id": 56, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "Yunus Emre ve Varlığın Birlik Noktası", "baslik_en": "Yunus Emre and the Unity Point of Existence",
            "icerik_tr": "Bir ben vardır bende, benden içeri...",
            "icerik_en": "There is an 'I' within me, deeper than me...",
            "kaynak_tr": "Yunus Emre Divanı",
            "kaynak_en": "Yunus Emre Divan",
            "hikmet_tr": "Benlik merkezli dairenin dışındaki sonsuzluk noktası.",
            "hikmet_en": "The point of infinity outside the ego-centered circle."
        },
        {
            "id": 57, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "İmam Âzam ve Ticari Hesap Hassasiyeti", "baslik_en": "Imam Azam and Commercial Calculation Precision",
            "icerik_tr": "Ticarette ve ortaklıklarda en küçük küsüratların dahi adil paylaşılması takvânın gereğidir.",
            "icerik_en": "Fair sharing of even the smallest fractions in trade and partnerships is a requirement of piety.",
            "kaynak_tr": "İmam Âzam Ebû Hanife, Menâkıb",
            "kaynak_en": "Imam Azam Abu Hanifa, Manaqib",
            "hikmet_tr": "İslam ticareti, kusursuz bir hesap dürüstlüğüne dayanır.",
            "hikmet_en": "Islamic commerce relies on impeccable computational honesty."
        },
        {
            "id": 58, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "İmam Gazali ve İlimlerin Sınıflandırma Matematiği", "baslik_en": "Al-Ghazali's Classification Mathematics of Sciences",
            "icerik_tr": "İlimler riyazi, mantıki, tabii ve ilahi olarak hiyerarşik bir ağaç gibi birbirine bağlıdır.",
            "icerik_en": "Sciences are interconnected like a hierarchical tree: mathematical, logical, natural, and divine.",
            "kaynak_tr": "İmam Gazali, İhyâu Ulûmi'd-Dîn",
            "kaynak_en": "Al-Ghazali, Ihya Ulum al-Din",
            "hikmet_tr": "Bilgi havuzu sistemli bir sınıflama matematiğine sahiptir.",
            "hikmet_en": "The pool of knowledge possesses a systematic classification mathematics."
        },
        {
            "id": 59, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "Abdülkâdir Geylânî ve Manevi Basamakların Sayısı", "baslik_en": "Abd al-Qadir al-Jilani and the Number of Spiritual Ranks",
            "icerik_tr": "Evliyanın manevi terakki mertebeleri ve zikir halleri belirli sırat-ı müstakim ölçülerine göredir.",
            "icerik_en": "The spiritual ascension ranks and states of remembrance of the saints are according to precise straight path measures.",
            "kaynak_tr": "Abdülkâdir Geylânî, El-Gunye",
            "kaynak_en": "Abd al-Qadir al-Jilani, Al-Gunyah",
            "hikmet_tr": "Maneviyat âleminde de kuralsızlık değil, disiplinli bir basamak matematiği vardır.",
            "hikmet_en": "In the spiritual realm too, there is a disciplined step-by-step mathematics rather than lawlessness."
        },
        {
            "id": 60, "kategori_tr": "İslam Alimleri & Veliler", "kategori_en": "Scholars & Saints",
            "baslik_tr": "İbn Tufeyl ve Hayy bin Yakzan'ın Doğal Matematik Keşfi", "baslik_en": "Ibn Tufayl and Hayy ibn Yaqzan's Discovery of Natural Mathematics",
            "icerik_tr": "Yalnız başına adada yaşayan insan, gök cisimlerinin hareketlerini gözlemleyerek yaratıcının matematiksel sanatını keşfeder.",
            "icerik_en": "A human living alone on an island discovers the creator's mathematical art by observing celestial movements and numerical order.",
            "kaynak_tr": "İbn Tufeyl, Hayy bin Yakzan",
            "kaynak_en": "Ibn Tufayl, Hayy ibn Yaqzan",
            "hikmet_tr": "Saf akıl ve gözlem kâinattaki matematiksel tasarımı doğrudan okuyabilir.",
            "hikmet_en": "Pure reason and observation can directly read the mathematical design in the universe."
        },

        # Bediüzzaman Said Nursi (61-80)
        {
            "id": 61, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "İsm-i Adl ve Kâinattaki Hassas Ölçü", "baslik_en": "The Name Al-Adl and Precise Measure in Universe",
            "icerik_tr": "Güneş sisteminden tut, ta kan küreciklerine ve atom altı parçacıklara kadar her şey hassas bir matematiksel nizamla tartılmıştır.",
            "icerik_en": "From the solar system down to blood corpuscles and subatomic particles, everything is weighed with a precise mathematical order.",
            "kaynak_tr": "Risale-i Nur, Lem'alar",
            "kaynak_en": "Risale-i Nur, The Flashes",
            "hikmet_tr": "İsm-i Adl kâinattaki kozmik denge ve mükemmel matematik olarak tecelli eder.",
            "hikmet_en": "The name Al-Adl manifests as cosmic balance and perfect mathematics in the universe."
        },
        {
            "id": 62, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Kâinatın Mühendislik Dili", "baslik_en": "Engineering Language of the Universe",
            "icerik_tr": "Bütün kâinattaki gök cisimleri ve mahlukat, mükemmel bir geometri ve mühendisane bir ölçü ile tanzim olunmuştur.",
            "icerik_en": "All celestial bodies and creatures in the universe are organized with perfect geometry and engineering measurement.",
            "kaynak_tr": "Risale-i Nur, Asa-yı Musa",
            "kaynak_en": "Risale-i Nur, The Staff of Moses",
            "hikmet_tr": "Evren, İlahî bir Mimarın çizimi olan geometrik bir saray gibidir.",
            "hikmet_en": "The universe is like a geometric palace drawn by a Divine Architect."
        },
        {
            "id": 63, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Aklın Nuru Fünun-u Medeniyedir", "baslik_en": "The Light of Mind is Positive Sciences",
            "icerik_tr": "Vicdanın ziyası din ilimleridir. Aklın nuru pozitif bilimler ve matematiktir. İkisinin imtizacıyla hakikat tecelli eder.",
            "icerik_en": "The light of conscience is religious sciences. The light of the mind is positive sciences and mathematics. Truth manifests through their fusion.",
            "kaynak_tr": "Risale-i Nur, Münazarat",
            "kaynak_en": "Risale-i Nur, The Debates",
            "hikmet_tr": "Din ile matematik ve müspet fenler çatışmaz; birbirini tamamlar.",
            "hikmet_en": "Religion and mathematics/positive sciences do not clash; they complement each other."
        },
        {
            "id": 64, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Güneşin Hassas Hızı ve Kütle Dengesi", "baslik_en": "Precise Speed and Mass Balance of the Sun",
            "icerik_tr": "Bir elmayı teraziye koymak gibi, koca Güneş'i gezegenleriyle beraber hassas bir mizan-ı adaletle yerinde tutan bir kudret vardır.",
            "icerik_en": "Like placing an apple on a scale, there is a power keeping the mighty Sun together with its planets in place with a precise scale of justice.",
            "kaynak_tr": "Risale-i Nur, Sözler",
            "kaynak_en": "Risale-i Nur, The Words",
            "hikmet_tr": "Gezegenlerin yörünge hızları ve kütleçekim hesapları İlahî kudretin mizanıdır.",
            "hikmet_en": "Orbital speeds and gravitational calculations of planets are the balance of divine power."
        },
        {
            "id": 65, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Kur'an'daki Şifreler ve Cifr Matematiği", "baslik_en": "Ciphers and Jifr Mathematics in the Quran",
            "icerik_tr": "Kur'an'ın kelime ve harflerinde öyle bir ebced ve cifr matematiği vardır ki, istikbale ait birçok olayı sayısal kodlarla işaret eder.",
            "icerik_en": "There is such abjad and jifr mathematics in the words and letters of the Quran that it signals many future events with numerical codes.",
            "kaynak_tr": "Risale-i Nur, Şualar",
            "kaynak_en": "Risale-i Nur, The Rays",
            "hikmet_tr": "Kur'an'ın lafızlarında mucizevi matematiksel uyumlar vardır.",
            "hikmet_en": "There are miraculous mathematical harmonies in the utterances of the Quran."
        },
        {
            "id": 66, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Kültür-ü Riyaziye (Matematik Birikimi)", "baslik_en": "Mathematical Accumulation (Ilm al-Riyadiyat)",
            "icerik_tr": "Bediüzzaman, medrese ilimlerinin yanı sıra riyaziyat, cebr, hendese ve heyet ilimlerini en derin detaylarıyla tetkik etmiştir.",
            "icerik_en": "Bediuzzaman studied mathematics, algebra, geometry, and astronomy in deep detail alongside traditional madrasa sciences.",
            "kaynak_tr": "Risale-i Nur, Tarihçe-i Hayat",
            "kaynak_en": "Risale-i Nur, Biography",
            "hikmet_tr": "İslami ilimlerde derinleşmek, matematik ve mantık disiplinlerine hâkim olmayı gerektirir.",
            "hikmet_en": "Deepening in Islamic sciences requires mastery of mathematical and logical disciplines."
        },
        {
            "id": 67, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Zatî, Sıfatî ve Esmaî Mizanlar", "baslik_en": "Essential, Attributive, and Nominal Balances",
            "icerik_tr": "Kâinattaki her bir mevcudun üzerinde İlahî isimlerin dokunmuş olduğu hassas birer ölçü ve mizan nakşedilmiştir.",
            "icerik_en": "On every existent being in the universe, delicate measures and balances woven by Divine Names are inscribed.",
            "kaynak_tr": "Risale-i Nur, Sözler",
            "kaynak_en": "Risale-i Nur, The Words",
            "hikmet_tr": "Varlık kılıfı, ilahî isimlerin matematiksel nakışlarıyla süslenmiştir.",
            "hikmet_en": "The garment of existence is adorned with mathematical embroideries of divine names."
        },
        {
            "id": 68, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Atomların ve Yıldızların Aynı Kanuna Tabi Olması", "baslik_en": "Atoms and Stars Subject to the Same Law",
            "icerik_tr": "Zerrelerden yıldızlara kadar bütün mevcudiyet, aynı mutlak kanun ve matematiksel nizama boyun eğmektedir.",
            "icerik_en": "From dust particles to stars, all existence submits to the same absolute law and mathematical order.",
            "kaynak_tr": "Risale-i Nur, Mektubat",
            "kaynak_en": "Risale-i Nur, Letters",
            "hikmet_tr": "Büyük ile küçük, zerre ile küre Sâni karşısında eşittir ve aynı matematik kanunuyla döner.",
            "hikmet_en": "Large and small, atom and sphere are equal before the Maker and rotate with the same mathematical law."
        },
        {
            "id": 69, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Hücrelerin ve Çekirdeklerin Program Matematiği", "baslik_en": "Program Mathematics of Cells and Seeds",
            "icerik_tr": "Küçücük bir çekirdeğin içine koca bir ağacın programı, kader kalemiyle yazılmış kusursuz bir matematiksel kodla yerleştirilmiştir.",
            "icerik_en": "Inside a tiny seed, the program of a giant tree is placed with a flawless mathematical code written by the pen of destiny.",
            "kaynak_tr": "Risale-i Nur, Sözler",
            "kaynak_en": "Risale-i Nur, The Words",
            "hikmet_tr": "Genetik kodlar ve çekirdekler, ilahî mukadderatın mikro düzeydeki matematik arşivleridir.",
            "hikmet_en": "Genetic codes and seeds are micro-level mathematical archives of divine destiny."
        },
        {
            "id": 70, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Kâinatın Kitabını Okuma Yöntemi", "baslik_en": "Method of Reading the Book of the Universe",
            "icerik_tr": "Kâinat büyük bir kitaptır; hurufatı kelimât-ı tekviniye olup her bir mevcudu birer matematik harf hükmündedir.",
            "icerik_en": "The universe is a grand book; its letters are existential words, and every existent entity functions as a mathematical letter.",
            "kaynak_tr": "Risale-i Nur, İşaratü'l-İ'câz",
            "kaynak_en": "Risale-i Nur, Signs of Miraculousness",
            "hikmet_tr": "Fen bilimleri kâinat kitabının matematiksel gramerini okuma çabasıdır.",
            "hikmet_en": "Natural sciences are the effort to read the mathematical grammar of the book of the universe."
        },
        {
            "id": 71, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Ruhların ve Meleklerin Boyutsal Sayıları", "baslik_en": "Dimensional Numbers of Spirits and Angels",
            "icerik_tr": "Maneviyat âleminin kendine has hız, boyut ve sayısal kanunları maddî âlemin kanunlarından çok daha ulvîdir.",
            "icerik_en": "The speed, dimension, and numerical laws specific to the spiritual realm are far more sublime than those of the material realm.",
            "kaynak_tr": "Risale-i Nur, Mesnevî-i Nuriye",
            "kaynak_en": "Risale-i Nur, Mathnawi al-Nuriya",
            "hikmet_tr": "Fizik ötesi âlemlerin de kendine mahsus soyut matematik yasaları vardır.",
            "hikmet_en": "Meta-physical realms also possess their own distinct abstract mathematical laws."
        },
        {
            "id": 72, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Tesadüfün Matematiksel İmkansızlığı", "baslik_en": "Mathematical Impossibility of Coincidence",
            "icerik_tr": "Milyonlarca ihtimal içinde tek bir mükemmel nizamın tutturulması tesadüfe verilemez; mutlak bir irade ve hesap gerektirir.",
            "icerik_en": "Achieving a single perfect order among millions of possibilities cannot be attributed to coincidence; it requires an absolute will and calculation.",
            "kaynak_tr": "Risale-i Nur, Barla Lahikası",
            "kaynak_en": "Risale-i Nur, Barla Letters",
            "hikmet_tr": "Olasılık hesapları tesadüf ihtimalini sıfıra indirir, ilahî tasarrufu ispat eder.",
            "hikmet_en": "Probability calculations reduce the chance of coincidence to zero, proving divine governance."
        },
        {
            "id": 73, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Zamanın İzafiyeti ve Anların Matematiği", "baslik_en": "Relativity of Time and Mathematics of Moments",
            "icerik_tr": "Zaman mekâna ve şuur sahiplerine göre değişir; bir saniye bin yıl hükmüne geçebilir.",
            "icerik_en": "Time varies according to space and conscious beings; a second can assume the judgment of a thousand years.",
            "kaynak_tr": "Risale-i Nur, Sözler",
            "kaynak_en": "Risale-i Nur, The Words",
            "hikmet_tr": "Zaman mutlak değil, ilahî iradenin esnek bir matematiksel boyutudur.",
            "hikmet_en": "Time is not absolute; it is a flexible mathematical dimension of the divine will."
        },
        {
            "id": 74, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "İnsanın Kâinatın Özü Olması (Mikrokozmos)", "baslik_en": "Human Being as the Essence of Universe (Microcosm)",
            "icerik_tr": "İnsan kâinatın bir küçük örneğidir; kâinattaki bütün matematiksel dengeler insanda da küçük ölçekte mevcuttur.",
            "icerik_en": "Man is a miniature sample of the universe; all mathematical balances in the universe exist in man on a small scale.",
            "kaynak_tr": "Risale-i Nur, Fihrist",
            "kaynak_en": "Risale-i Nur, Index",
            "hikmet_tr": "İnsan bedeni ve ruhu, kozmik matematiğin özet bir tablosudur.",
            "hikmet_en": "The human body and soul constitute an abridged table of cosmic mathematics."
        },
        {
            "id": 75, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "İlim ve Hikmetin Matematiksel Paydası", "baslik_en": "Mathematical Common Denominator of Knowledge and Wisdom",
            "icerik_tr": "Hikmet, eşyanın hakikatini ve matematiksel tertibini okuyarak Sanatkârını bilmektir.",
            "icerik_en": "Wisdom is knowing the Maker by reading the truth and mathematical arrangement of things.",
            "kaynak_tr": "Risale-i Nur, Lem'alar",
            "kaynak_en": "Risale-i Nur, The Flashes",
            "hikmet_tr": "Gerçek bilim, kâinattaki rakamların arkasındaki manayı okuyabilmektir.",
            "hikmet_en": "True science is the ability to read the meaning behind numbers in the universe."
        },
        {
            "id": 76, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Haşir ve Son Hesap Matematiği", "baslik_en": "Resurrection and Mathematics of Final Accounting",
            "icerik_tr": "Milyarlarca insanın ve mahlukatın mahşerde toplanması ve hesaplarının görülmesi ilahî ilmin mutlak matematiğiyle birden görülür.",
            "icerik_en": "The gathering of billions of people and creatures in the Hereafter and their accounting are simultaneously observed through absolute mathematics.",
            "kaynak_tr": "Risale-i Nur, Sözler",
            "kaynak_en": "Risale-i Nur, The Words",
            "hikmet_tr": "Ahiret adaleti en kusursuz istatistiki hesap günüdür.",
            "hikmet_en": "The justice of the hereafter is the most flawless statistical day of reckoning."
        },
        {
            "id": 77, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Mahlukattaki Sanat ve Ölçü Birliği", "baslik_en": "Unity of Art and Measure in Creation",
            "icerik_tr": "Bütün çiçeklerde ve hayvanlarda görülen simetri, renk ve sayı uyumları bir tek Sâni'in mührünü gösterir.",
            "icerik_en": "The symmetry, color, and numerical harmonies seen in all flowers and animals show the seal of a single Maker.",
            "kaynak_tr": "Risale-i Nur, Mektubat",
            "kaynak_en": "Risale-i Nur, Letters",
            "hikmet_tr": "Canlılardaki sayısal ve geometrik desenler birlik tevhidinin delilidir.",
            "hikmet_en": "Numerical and geometric patterns in living beings are evidence of the unity of Oneness."
        },
        {
            "id": 78, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Kaza ve Kaderin Değişmez Defterleri", "baslik_en": "Unchanging Ledgers of Decree and Destiny",
            "icerik_tr": "Levh-i Mahfuz, kâinatın yazılmış en büyük matematiksel planı ve kader programıdır.",
            "icerik_en": "The Preserved Tablet is the greatest written mathematical plan and destiny program of the universe.",
            "kaynak_tr": "Risale-i Nur, Sözler",
            "kaynak_en": "Risale-i Nur, The Words",
            "hikmet_tr": "Geçmiş ve geleceğin tüm olayları kader sicilinde kesin sayılarla kayıtlıdır.",
            "hikmet_en": "All events of past and future are recorded with exact numbers in the registry of destiny."
        },
        {
            "id": 79, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Esma-i Hüsna'nın Sayısal Tezahürleri", "baslik_en": "Numerical Manifestations of Asma al-Husna",
            "icerik_tr": "Her bir İlahî isim kâinatta kendine mahsus bir alan açar ve o alanın matematiksel sınırlarını tayin eder.",
            "icerik_en": "Each Divine Name opens a realm of its own in the universe and determines the mathematical limits of that realm.",
            "kaynak_tr": "Risale-i Nur, Şualar",
            "kaynak_en": "Risale-i Nur, The Rays",
            "hikmet_tr": "İlahî isimlerin tecellileri evrende niceliksel birer nizam oluşturur.",
            "hikmet_en": "The manifestations of divine names form a quantitative order in the universe."
        },
        {
            "id": 80, "kategori_tr": "Bediüzzaman Said Nursi", "kategori_en": "Bediuzzaman",
            "baslik_tr": "Medeniyetin İlim ve Matematikle İlerlemesi", "baslik_en": "Advancement of Civilization through Science and Mathematics",
            "icerik_tr": "İnsanlık medeniyetteki terakkisini fen bilimleri ve riyaziyatın gelişmesiyle elde etmiştir.",
            "icerik_en": "Humanity has achieved its progress in civilization through the development of natural sciences and mathematics.",
            "kaynak_tr": "Risale-i Nur, Hutbe-i Şamiye",
            "kaynak_en": "Risale-i Nur, The Damascus Sermon",
            "hikmet_tr": "Maddi kalkınmanın motoru matematik ve pozitif fenlerdir.",
            "hikmet_en": "The engine of material development is mathematics and positive sciences."
        }
    ]

# --- ARAYÜZ VE GÖRÜNTÜLEME MANTIĞI ---
st.markdown(f"<h1 class='main-title'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='sub-title'>{t['subtitle']}</p>", unsafe_allow_html=True)

# Yasal Koruma ve Sorumluluk Reddi Bildirimi
if dil == "Türkçe":
    st.warning(
        "⚖️ **Yasal Uyarı / Legal Notice:** Bu web uygulamasındaki tüm içerik yalnızca **bilgi paylaşımı** amacıyla sunulmuştur. "
        "Kur'an-ı Kerim ayet mealleri **Diyanet İşleri Başkanlığı** kaynaklarından referans alınmıştır. "
        "**Ticari olarak kullanılamaz**, çoğaltılamaz ve kopyalanamaz. "
        "Uygulama üzerindeki hiçbir bilgi ve veri kopyalanamaz, başka mecralarda izinsiz yayınlanamaz. "
        "Yazılım geliştiricinin veya içerik sağlayıcının uygulama kullanımından doğabilecek herhangi bir sorumluluğu bulunmamaktadır. "
        "Her hakkı saklıdır © 2026."
    )
else:
    st.warning(
        "⚖️ **Legal Notice:** All content in this web application is provided solely for **information sharing** purposes. "
        "Quranic verse translations are referenced from **Diyanet Affairs** sources. "
        "It **cannot be used commercially**, reproduced, or copied. "
        "No information or data on the application can be copied or published elsewhere without permission. "
        "The software developer or content provider bears no responsibility arising from the use of the application. "
        "All rights reserved © 2026."
    )

df_master = pd.DataFrame(st.session_state.master_data)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(t['total_records'], len(df_master))
col2.metric(t['ayets'], len(df_master[df_master['kategori_tr'] == 'Ayet-i Kerime']))
col3.metric(t['hadiths'], len(df_master[df_master['kategori_tr'] == 'Hadis-i Şerif']))
col4.metric(t['scholars'], len(df_master[df_master['kategori_tr'] == 'İslam Alimleri & Veliler']))
col5.metric(t['said_nursi'], len(df_master[df_master['kategori_tr'] == 'Bediüzzaman Said Nursi']))

st.divider()

st.sidebar.header(t['search_header'])

kategoriler_tr = ["Tümü / All", "Ayet-i Kerime", "Hadis-i Şerif", "İslam Alimleri & Veliler", "Bediüzzaman Said Nursi"]
kategoriler_en = ["All", "Quranic Verse", "Hadith", "Scholars & Saints", "Bediuzzaman"]

secilen_kategori_index = st.sidebar.selectbox(t['select_cat'], range(len(kategoriler_tr)), format_func=lambda x: kategoriler_tr[x] if dil == "Türkçe" else kategoriler_en[x])
secilen_kategori_tr = kategoriler_tr[secilen_kategori_index]

arama_metni = st.sidebar.text_input(t['search_placeholder'], placeholder="kader, mizan, destiny, measure...")

st.sidebar.divider()

filtered_df = df_master.copy()

if secilen_kategori_tr != "Tümü / All":
    filtered_df = filtered_df[filtered_df['kategori_tr'] == secilen_kategori_tr]

if arama_metni:
    arama_kucuk = arama_metni.lower()
    filtered_df = filtered_df[
        filtered_df['baslik_tr'].str.contains(arama_kucuk, case=False, na=False) |
        filtered_df['baslik_en'].str.contains(arama_kucuk, case=False, na=False) |
        filtered_df['icerik_tr'].str.contains(arama_kucuk, case=False, na=False) |
        filtered_df['icerik_en'].str.contains(arama_kucuk, case=False, na=False) |
        filtered_df['hikmet_tr'].str.contains(arama_kucuk, case=False, na=False) |
        filtered_df['hikmet_en'].str.contains(arama_kucuk, case=False, na=False)
    ]

# İndirme butonu ve sütun yapısı tamamen kaldırıldı, başlık doğrudan gösteriliyor
st.subheader(f"📖 Arşiv / Archive ({len(filtered_df)} kayıt / records)")

if len(filtered_df) == 0:
    st.info(t['no_result'])
else:
    for _, row in filtered_df.iterrows():
        cat_text = row['kategori_tr'] if dil == "Türkçe" else row['kategori_en']
        title_text = row['baslik_tr'] if dil == "Türkçe" else row['baslik_en']
        content_text = row['icerik_tr'] if dil == "Türkçe" else row['icerik_en']
        hikmet_text = row['hikmet_tr'] if dil == "Türkçe" else row['hikmet_en']
        kaynak_text = row['kaynak_tr'] if dil == "Türkçe" else row['kaynak_en']
        
        badge_class = "badge-ayet"
        if "Hadis" in row['kategori_tr'] or "Hadith" in row['kategori_en']: 
            badge_class = "badge-hadis"
        elif "Alim" in row['kategori_tr'] or "Scholars" in row['kategori_en']: 
            badge_class = "badge-alim"
        elif "Bediüzzaman" in row['kategori_tr'] or "Bediuzzaman" in row['kategori_en']: 
            badge_class = "badge-bediuzzaman"

        hikmet_label = "💡 Hikmet:" if dil == "Türkçe" else "💡 Wisdom:"
        kaynak_label = "📖 Kaynak:" if dil == "Türkçe" else "📖 Source:"

        st.markdown(f"""
        <div class="quote-card">
            <span class="{badge_class}">{cat_text}</span>
            <h3 style="margin-top: 10px; color: #1e3d59;">{title_text}</h3>
            <p style="font-size: 1.1rem; line-height: 1.6; color: #2b2b2b;">"{content_text}"</p>
            <p style="color: #17b978; font-weight: 500;"><strong>{hikmet_label}</strong> {hikmet_text}</p>
            <p class="source-text"><strong>{kaynak_label}</strong> {kaynak_text}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #888;'>{t['footer']}</p>", unsafe_allow_html=True)