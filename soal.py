# ==============================================================================
# FILE: soal.py
# TUGAS: Menyimpan daftar soal DASS-42 & PSQI beserta keterangan jawabannya
# ==============================================================================

# Pilihan jawaban standar DASS-42 (angka di depan otomatis jadi skor)
PILIHAN_DASS = [
    "0 = Tidak pernah",
    "1 = Kadang-kadang",
    "2 = Sering",
    "3 = Hampir selalu",
]

# 1. DAFTAR 14 PERTANYAAN STRES (DASS-42)
SOAL_STRES = [
    "1. Saya merasa mudah marah karena hal-hal kecil atau sepele.",
    "2. Saya cenderung bereaksi berlebihan terhadap suatu situasi.",
    "3. Saya merasa kesulitan untuk bersantai atau relaksasi.",
    "4. Saya merasa mudah kesal.",
    "5. Saya merasa banyak menghabiskan energi karena rasa cemas.",
    "6. Saya merasa tidak sabaran ketika mengalami penundaan (misal menunggu atau macet).",
    "7. Saya merasa mudah tersinggung.",
    "8. Saya merasa sulit untuk beristirahat.",
    "9. Saya merasa mudah marah.",
    "10. Saya kesulitan untuk kembali tenang setelah ada sesuatu yang mengganggu.",
    "11. Saya sulit mentoleransi gangguan terhadap hal yang sedang saya kerjakan.",
    "12. Saya berada dalam keadaan tegang atau gelisah.",
    "13. Saya tidak dapat memaklumi hal apa pun yang menghalangi penyelesaian tugas saya.",
    "14. Saya merasa mudah gelisah.",
]

# 2. DAFTAR 14 PERTANYAAN KECEMASAN (DASS-42)
SOAL_CEMAS = [
    "1. Saya merasa mulut saya terasa kering.",
    "2. Saya mengalami kesulitan bernapas (misalnya napas cepat atau sesak padahal tidak habis olahraga).",
    "3. Saya merasakan kelemahan atau gemetar pada anggota tubuh (misal kaki terasa goyah).",
    "4. Saya merasa cemas berlebihan dalam suatu situasi, namun baru lega jika situasi itu berakhir.",
    "5. Saya merasa lemas seperti mau pingsan.",
    "6. Saya berkeringat secara berlebihan padahal cuaca tidak panas dan tidak habis olahraga.",
    "7. Saya merasa ketakutan tanpa alasan yang jelas.",
    "8. Saya mengalami kesulitan dalam menelan.",
    "9. Saya merasakan jantung berdebar kencang padahal tidak sedang beraktivitas berat.",
    "10. Saya merasa mudah panik.",
    "11. Saya takut terhambat oleh tugas-tugas baru yang belum biasa saya lakukan.",
    "12. Saya merasa ketakutan.",
    "13. Saya khawatir akan situasi di mana saya mungkin panik dan mempermalukan diri sendiri.",
    "14. Saya merasa gemetar (misalnya pada bagian tangan).",
]

# 3. DAFTAR 14 PERTANYAAN DEPRESI (DASS-42)
SOAL_DEPRESI = [
    "1. Saya tidak dapat merasakan hal yang positif sama sekali.",
    "2. Saya merasa sepertinya tidak kuat lagi untuk melakukan suatu kegiatan.",
    "3. Saya merasa pesimis dan tidak ada hal yang dapat diharapkan di masa depan.",
    "4. Saya merasa sedih dan tertekan.",
    "5. Saya kehilangan minat pada banyak hal (misalnya makan atau bersosialisasi).",
    "6. Saya merasa diri saya tidak layak atau tidak berharga.",
    "7. Saya merasa hidup ini tidak berharga.",
    "8. Saya tidak dapat menikmati hal-hal yang saya lakukan.",
    "9. Saya merasa hilang harapan dan putus asa.",
    "10. Saya sulit untuk merasa antusias pada banyak hal.",
    "11. Saya merasa diri saya tidak berharga.",
    "12. Saya merasa tidak ada harapan untuk masa depan.",
    "13. Saya merasa hidup ini tidak berarti.",
    "14. Saya sulit menumbuhkan inisiatif untuk memulai suatu pekerjaan.",
]

# 4. DAFTAR 7 KOMPONEN KUALITAS TIDUR (PSQI) + KETERANGAN TIAP JAWABAN
SOAL_TIDUR = [
    ("1. Kualitas tidur keseluruhan sebulan terakhir?", ["0 = Sangat baik", "1 = Cukup baik", "2 = Kurang baik", "3 = Sangat buruk"]),
    ("2. Lama waktu yang dibutuhkan sampai tertidur?", ["0 = < 15 menit", "1 = 16 - 30 menit", "2 = 31 - 60 menit", "3 = > 60 menit"]),
    ("3. Rata-rata durasi tidur efektif per malam?", ["0 = > 7 jam", "1 = 6 - 7 jam", "2 = 5 - 6 jam", "3 = < 5 jam"]),
    ("4. Efisiensi tidur (lama tidur dibanding waktu di kasur)?", ["0 = > 85% (nyenyak)", "1 = 75 - 84%", "2 = 65 - 74%", "3 = < 65% (sering terjaga)"]),
    ("5. Seberapa sering terbangun tengah malam / mimpi buruk / gerah?", ["0 = Tidak pernah", "1 = < 1x seminggu", "2 = 1 - 2x seminggu", "3 = 3x atau lebih/minggu"]),
    ("6. Seberapa sering mengonsumsi obat bantu tidur?", ["0 = Tidak pernah", "1 = < 1x seminggu", "2 = 1 - 2x seminggu", "3 = 3x atau lebih/minggu"]),
    ("7. Seberapa sering mengantuk atau sulit fokus di siang hari?", ["0 = Tidak ada masalah", "1 = Sedikit masalah", "2 = Ada masalah", "3 = Masalah besar"]),
]


# 5. ATURAN PENENTU KATEGORI SKOR
def cek_stres(skor):
    if skor <= 14:
        return "Normal"
    elif skor <= 18:
        return "Stres Ringan"
    elif skor <= 25:
        return "Stres Sedang"
    elif skor <= 33:
        return "Stres Berat"
    else:
        return "Stres Sangat Berat"


def cek_cemas(skor):
    if skor <= 7:
        return "Normal"
    elif skor <= 9:
        return "Kecemasan Ringan"
    elif skor <= 14:
        return "Kecemasan Sedang"
    elif skor <= 19:
        return "Kecemasan Berat"
    else:
        return "Kecemasan Sangat Berat"


def cek_depresi(skor):
    if skor <= 9:
        return "Normal"
    elif skor <= 13:
        return "Depresi Ringan"
    elif skor <= 20:
        return "Depresi Sedang"
    elif skor <= 27:
        return "Depresi Berat"
    else:
        return "Depresi Sangat Berat"


def cek_tidur(skor):
    if skor <= 5:
        return "Kualitas Tidur Baik"
    else:
        return "Kualitas Tidur Buruk"