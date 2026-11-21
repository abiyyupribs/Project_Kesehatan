# File: materi.py
# Isinya cuma teks pengenalan dan daftar saran dari Skripsi Agus (2023)

DEFINISI_STRES = (
    "Stres akademik adalah tekanan pikiran akibat tuntutan kuliah, "
    "seperti tugas yang menumpuk, deadline mepet, dan cemas menghadapi ujian atau tugas akhir."
)

DEFINISI_TIDUR = (
    "Kualitas tidur adalah ukuran seberapa nyenyak dan efektif tidur memulihkan tubuh, "
    "mulai dari lama waktu tidur, cepat tidaknya tertidur, sampai rasa segar saat bangun."
)

FAKTA_RISET = (
    "Hasil riset pada 40 mahasiswa semester 8 di ITSKes ICMe Jombang (Agus, 2023) menunjukkan "
    "57,5% mengalami stres tinggi, 57,5% kualitas tidurnya tidak baik, dan keduanya saling berhubungan."
)


def ambil_saran_stres(kategori):
    if kategori == "Stres Rendah":
        return [
            "Pertahankan keseimbangan antara jadwal kuliah, ibadah, dan waktu istirahat.",
            "Jaga manajemen waktu belajar agar tugas tidak menumpuk di akhir.",
        ]
    elif kategori == "Stres Sedang":
        return [
            "Atur prioritas tugas dan hindari Sistem Kebut Semalam (SKS) saat mendekati deadline.",
            "Sisihkan waktu untuk relaksasi atau istirahat agar emosi tetap stabil.",
            "Diskusikan materi kuliah yang sulit dengan teman atau dosen pembimbing.",
        ]
    else:
        return [
            "Kurangi beban berlebih dan buat batasan jam belajar agar pikiran punya waktu istirahat.",
            "Pecah tugas besar menjadi target harian kecil supaya lebih mudah dikerjakan.",
            "Konsultasikan masalah akademik ke dosen wali atau layanan konseling kampus.",
        ]


def ambil_saran_tidur(kategori):
    if kategori == "Tidur Baik":
        return [
            "Pertahankan durasi tidur ideal (> 7 jam/malam) dan jam bangun yang teratur.",
            "Teruskan kebiasaan tidur sehat agar konsentrasi kuliah tetap optimal.",
        ]
    elif kategori == "Tidur Cukup Baik":
        return [
            "Kurangi kebiasaan begadang untuk main game atau nonton hingga larut malam.",
            "Batasi minum kopi, teh, minuman berenergi, dan rokok menjelang jam tidur.",
        ]
    else:
        return [
            "Tidur dan bangun di jam yang sama setiap hari, serta jauhkan HP sebelum tidur.",
            "Hindari kopi, minuman berenergi, dan makanan tinggi gula sebelum tidur.",
            "Rutin olahraga ringan di pagi atau sore hari agar malamnya lebih mudah nyenyak.",
            "Jika susah tidur terus berlanjut dan mengganggu kuliah, periksakan ke tenaga kesehatan.",
        ]