# File: soal.py
# Isinya daftar pertanyaan kuesioner dan rumus penentu kategori skor

SOAL_STRES = [
    "Saya tidak merasa puas pada nilai pelajaran saya",
    "Saya merasa banyak tugas kuliah",
    "Saya merasa banyak tugas dengan deadline mepet",
    "Pendidikan lanjut dan pekerjaan akan membawa banyak tekanan akademis",
    "Orang tua terlalu memperhatikan nilai sehingga membawa tekanan berat",
    "Saya merasa kecewa pada dosen ketika hasil pembelajaran saya jelek",
    "Saya merasa banyak tekanan dalam perkuliahan",
    "Saya merasa terlalu banyak tes dan ulangan",
    "Nilai itu penting dan menentukan masa depan hidup saya",
    "Saya kecewa pada dosen ketika nilai tes tidak sesuai harapan",
    "Banyak kompetisi di antara teman kelas yang membawa tekanan akademik",
    "Saya merasa kurang percaya diri dengan hasil nilai pelajaran saya",
    "Sangat sulit untuk berkonsentrasi di kelas",
    "Saya merasa stres ketika tidak mencapai standar diri saya sendiri",
    "Ketika gagal pada harapan, saya merasa belum cukup baik",
    "Saya sulit tidur karena khawatir belum mencapai tujuan yang direncanakan",
]

SOAL_TIDUR = [
    ("Kualitas tidur keseluruhan sebulan terakhir?", ["0 = Sangat baik", "1 = Cukup baik", "2 = Kurang baik", "3 = Sangat buruk"]),
    ("Lama waktu yang dibutuhkan sampai tertidur?", ["0 = < 15 menit", "1 = 16 - 30 menit", "2 = 31 - 60 menit", "3 = > 60 menit"]),
    ("Rata-rata durasi tidur efektif per malam?", ["0 = > 7 jam", "1 = 6 - 7 jam", "2 = 5 - 6 jam", "3 = < 5 jam"]),
    ("Efisiensi tidur (lama tidur dibanding waktu di kasur)?", ["0 = > 85% (nyenyak)", "1 = 75 - 84%", "2 = 65 - 74%", "3 = < 65% (sering terjaga)"]),
    ("Seberapa sering terbangun tengah malam / mimpi buruk / gerah?", ["0 = Tidak pernah", "1 = < 1x seminggu", "2 = 1 - 2x seminggu", "3 = 3x atau lebih/minggu"]),
    ("Seberapa sering mengonsumsi obat bantu tidur?", ["0 = Tidak pernah", "1 = < 1x seminggu", "2 = 1 - 2x seminggu", "3 = 3x atau lebih/minggu"]),
    ("Seberapa sering mengantuk atau sulit fokus di siang hari?", ["0 = Tidak ada masalah", "1 = Sedikit masalah", "2 = Ada masalah", "3 = Masalah besar"]),
]


def cek_stres(skor):
    if skor < 37:
        return "Stres Rendah"
    elif skor < 59:
        return "Stres Sedang"
    else:
        return "Stres Tinggi"


def cek_tidur(skor):
    if skor <= 5:
        return "Tidur Baik"
    elif skor <= 7:
        return "Tidur Cukup Baik"
    elif skor <= 14:
        return "Tidur Tidak Baik"
    else:
        return "Tidur Sangat Tidak Baik"