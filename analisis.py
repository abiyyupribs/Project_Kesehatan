# ==============================================================================
# FILE: analisis.py
# TUGAS: Hitung kemiripan dengan 245 responden 3 jurnal, saran, & simpan CSV
# ==============================================================================

import os
import pandas as pd


def cek_kemiripan_jurnal(kat_stres, kat_tidur):
    # Bandingkan kategori stres user dengan 245 responden dari 3 jurnal
    if kat_stres == "Normal":
        info_stres = "Kelompok minoritas — hanya ~5,3% di Jurnal 2 (8/152) dan 0% di Jurnal 1 & 3."
    elif kat_stres == "Stres Ringan":
        info_stres = "Mirip dengan **50,0% responden Jurnal 1** (16/32) dan **52,5% responden Jurnal 3** (32/61)."
    elif kat_stres == "Stres Sedang":
        info_stres = "Sangat umum! Mirip dengan **51,4% total sampel** (126 dari 245 mahasiswa di 3 jurnal)."
    else:
        info_stres = "Mirip dengan **40,1% responden Jurnal 2** (61/152) dan **3,3% responden Jurnal 3** (2/61)."

    # Bandingkan kualitas tidur user dengan 245 responden dari 3 jurnal
    if kat_tidur == "Kualitas Tidur Baik":
        info_tidur = "Mirip dengan **15,5% total sampel** (38 dari 245 mahasiswa) yang tidurnya tetap terjaga."
    else:
        info_tidur = "Mirip dengan **84,5% total sampel** (207 dari 245 mahasiswa di 3 jurnal) yang tidurnya buruk."

    return info_stres, info_tidur


def ambil_saran_stres(kat_stres):
    if kat_stres == "Normal":
        return [
            "Pertahankan keseimbangan waktu kuliah/skripsi, istirahat, dan ibadah.",
            "Tetap buat jadwal harian kecil supaya tugas tidak menumpuk.",
        ]
    elif kat_stres == "Stres Ringan":
        return [
            "Pecah target skripsi/tugas besar jadi target kecil harian.",
            "Ambil jeda istirahat 10-15 menit tiap 1-2 jam belajar.",
        ]
    elif kat_stres == "Stres Sedang":
        return [
            "Kurangi begadang sistem kebut semalam dan atur ulang prioritas tugas.",
            "Lakukan relaksasi ringan (tarik napas dalam atau jalan santai 20 menit).",
            "Diskusikan hambatan tugas dengan teman atau dosen pembimbing.",
        ]
    else:
        return [
            "Kurangi aktivitas tambahan di luar kuliah sementara waktu.",
            "Ceritakan tekanan yang dirasakan ke keluarga, teman dekat, atau dosen wali.",
            "Manfaatkan layanan konseling kampus atau tenaga profesional.",
        ]


def ambil_saran_tidur(kat_tidur):
    if kat_tidur == "Kualitas Tidur Baik":
        return [
            "Pertahankan durasi tidur 7-8 jam/malam dan jam tidur yang teratur.",
            "Jaga kebiasaan ini supaya fokus kuliah tetap optimal.",
        ]
    else:
        return [
            "Biasakan tidur dan bangun di jam yang sama setiap hari.",
            "Jauhkan layar HP/laptop minimal 30-60 menit sebelum tidur.",
            "Hindari kopi, teh kental, atau makan berat menjelang jam tidur.",
            "Konsultasikan ke tenaga kesehatan jika susah tidur lebih dari 2 minggu.",
        ]


def simpan_riwayat(nama, gender, umur, s_stres, k_stres, s_cemas, k_cemas, s_depresi, k_depresi, s_tidur, k_tidur):
    # Bungkus hasil tes jadi 1 baris tabel lalu tempel ke riwayat_tes.csv
    baris_baru = pd.DataFrame([[
        pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"),
        nama, gender, umur,
        s_stres, k_stres, s_cemas, k_cemas,
        s_depresi, k_depresi, s_tidur, k_tidur,
    ]], columns=[
        "Waktu", "Nama", "Gender", "Umur",
        "Skor_Stres", "Kategori_Stres", "Skor_Cemas", "Kategori_Cemas",
        "Skor_Depresi", "Kategori_Depresi", "Skor_Tidur", "Kategori_Tidur",
    ])
    ada_file = os.path.exists("riwayat_tes.csv")
    baris_baru.to_csv("riwayat_tes.csv", mode="a", header=not ada_file, index=False)