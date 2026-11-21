# File: mesin_data.py
# Khusus ngolah data riset & nyimpen riwayat tes user pakai library pandas

import os
from datetime import datetime
import pandas as pd


def baca_csv():
    tabel = pd.read_csv("data_stres_tidur_mahasiswa.csv")
    return tabel


def bandingkan_data(df, kat_stres, kat_tidur, kode_gender):
    total_semua = len(df)
    rata_stres = df["skor_stres"].mean()
    rata_tidur = df["skor_tidur"].mean()

    # Cari mahasiswa di CSV yang kategori stres & tidurnya sama kayak user
    data_sama = df[(df["kategori_stres"] == kat_stres) & (df["kategori_tidur"] == kat_tidur)]
    jumlah_sama = len(data_sama)
    persen_sama = (jumlah_sama / total_semua) * 100

    # Cari khusus yang jenis kelaminnya sama (L atau P)
    data_gender = df[df["jenis_kelamin"] == kode_gender]
    total_gender = len(data_gender)
    sama_gender = data_gender[(data_gender["kategori_stres"] == kat_stres) & (data_gender["kategori_tidur"] == kat_tidur)]
    jumlah_sama_gender = len(sama_gender)
    persen_gender = (jumlah_sama_gender / total_gender) * 100

    return total_semua, rata_stres, rata_tidur, jumlah_sama, persen_sama, total_gender, jumlah_sama_gender, persen_gender


def ringkasan_csv(df):
    sebaran_stres = df["kategori_stres"].value_counts()
    sebaran_tidur = df["kategori_tidur"].value_counts()
    tabel_silang = pd.crosstab(df["kategori_stres"], df["kategori_tidur"])
    return sebaran_stres, sebaran_tidur, tabel_silang


# --- FUNGSI BARU: SIMPAN HASIL TES USER KE CSV ---
def simpan_riwayat(nama, gender, skor_s, kat_s, skor_t, kat_t):
    nama_file = "riwayat_tes.csv"
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Bikin 1 baris data baru dalam bentuk tabel DataFrame pandas
    baris_baru = pd.DataFrame([{
        "waktu_tes": waktu_sekarang,
        "nama": nama,
        "jenis_kelamin": gender,
        "skor_stres": skor_s,
        "kategori_stres": kat_s,
        "skor_tidur": skor_t,
        "kategori_tidur": kat_t,
    }])

    # Kalau file riwayat_tes.csv udah ada, gabungin data lama + baris baru
    if os.path.exists(nama_file):
        tabel_lama = pd.read_csv(nama_file)
        tabel_gabung = pd.concat([tabel_lama, baris_baru], ignore_index=True)
        tabel_gabung.to_csv(nama_file, index=False)
    else:
        # Kalau belum ada (pengisi pertama), langsung bikin file CSV baru
        baris_baru.to_csv(nama_file, index=False)


# --- FUNGSI BARU: BACA RIWAYAT TES USER ---
def baca_riwayat():
    nama_file = "riwayat_tes.csv"
    if os.path.exists(nama_file):
        return pd.read_csv(nama_file)
    return None