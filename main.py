# File: main.py
# File utama buat jalanin tampilan web, tinggal import dari materi.py, soal.py, dan mesin_data.py

import streamlit as st
from materi import DEFINISI_STRES, DEFINISI_TIDUR, FAKTA_RISET, ambil_saran_stres, ambil_saran_tidur
from soal import SOAL_STRES, SOAL_TIDUR, cek_stres, cek_tidur
from mesin_data import baca_csv, bandingkan_data, ringkasan_csv, simpan_riwayat, baca_riwayat

st.set_page_config(page_title="Diagnosa Stres & Tidur", page_icon="🩺")
st.title("🩺 Diagnosa Stres Akademik & Kualitas Tidur")
st.caption("Sumber Data & Instrumen: Skripsi Agus (ITSKes ICMe Jombang, 2023)")

# Baca file CSV riset dulu
try:
    df = baca_csv()
except FileNotFoundError:
    st.error("File 'data_stres_tidur_mahasiswa.csv' tidak ditemukan di folder ini!")
    st.stop()

# Bikin 3 Tab menu di bagian atas web
tab_materi, tab_tes, tab_data = st.tabs(["📖 Pengenalan", "📝 Mulai Tes", "📊 Data Riset & Riwayat"])

# ================= TAB 1: PENGENALAN MATERI =================
with tab_materi:
    st.subheader("Mengenal Stres Akademik & Kualitas Tidur")
    kol1, kol2 = st.columns(2)
    kol1.info(f"**Apa itu Stres Akademik?**\n\n{DEFINISI_STRES}")
    kol2.info(f"**Apa itu Kualitas Tidur?**\n\n{DEFINISI_TIDUR}")
    st.success(f"**Fakta Riset (40 Mahasiswa):**\n\n{FAKTA_RISET}")

    with st.expander("Lihat Aturan Penilaian Skor"):
        st.write("- **Stres Akademik:** `< 37` Rendah | `37 - 58` Sedang | `>= 59` Tinggi")
        st.write("- **Kualitas Tidur:** `0 - 5` Baik | `6 - 7` Cukup Baik | `8 - 14` Tidak Baik | `15 - 21` Sangat Tidak Baik")

# ================= TAB 2: KUESIONER & HASIL =================
with tab_tes:
    with st.form("form_tes"):
        c1, c2 = st.columns([2, 1])
        nama = c1.text_input("Nama / Inisial", placeholder="Contoh: Mhs_01")
        pilih_gender = c2.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])

        st.subheader("1. Kuesioner Stres Akademik")
        jawab_stres = []
        for nomor, teks_soal in enumerate(SOAL_STRES, start=1):
            pilih = st.radio(f"{nomor}. {teks_soal}", ["Ya", "Tidak"], index=None, horizontal=True, key=f"s_{nomor}")
            jawab_stres.append(pilih)

        st.subheader("2. Kuesioner Kualitas Tidur")
        jawab_tidur = []
        for nomor, (teks_soal, pilihan) in enumerate(SOAL_TIDUR, start=1):
            pilih = st.radio(f"{nomor}. {teks_soal}", pilihan, index=None, key=f"t_{nomor}")
            jawab_tidur.append(pilih)

        tombol_cek = st.form_submit_button("Cek Hasil Diagnosa", type="primary")

    if tombol_cek:
        if None in jawab_stres or None in jawab_tidur:
            st.warning("Masih ada pertanyaan yang belum diisi bray!")
        else:
            # Bersihkan input nama (cegah karakter awal rumus Excel seperti =, +, -, @)
            nama_bersih = nama.strip()
            while len(nama_bersih) > 0 and nama_bersih[0] in ("=", "+", "-", "@"):
                nama_bersih = nama_bersih[1:].strip()

            if nama_bersih == "":
                nama_user = "Anonim"
            else:
                nama_user = nama_bersih

            if pilih_gender == "Laki-laki":
                kode_gender = "L"
            else:
                kode_gender = "P"

            # Hitung total skor stres pakai loop for biasa
            skor_s = 0
            for jawaban in jawab_stres:
                if jawaban == "Ya":
                    skor_s = skor_s + 5
                else:
                    skor_s = skor_s + 1

            # Hitung total skor tidur pakai loop for biasa
            skor_t = 0
            for jawaban in jawab_tidur:
                angka = int(jawaban[0])
                skor_t = skor_t + angka

            # Cek kategori dan ambil saran
            kat_s = cek_stres(skor_s)
            kat_t = cek_tidur(skor_t)
            saran_s = ambil_saran_stres(kat_s)
            saran_t = ambil_saran_tidur(kat_t)

            # SIMPAN OTOMATIS KE FILE riwayat_tes.csv
            simpan_riwayat(nama_user, pilih_gender, skor_s, kat_s, skor_t, kat_t)

            # Bandingkan dengan CSV riset pakai fungsi di mesin_data.py
            total, rata_s, rata_t, jml_sama, persen_sama, tot_g, jml_g, persen_g = bandingkan_data(
                df, kat_s, kat_t, kode_gender
            )

            st.success(f"Hasil Diagnosa untuk **{nama_user}** ({pilih_gender}) — Otomatis tersimpan ke `riwayat_tes.csv`!")
            m1, m2 = st.columns(2)
            m1.metric("Stres Akademik", kat_s, f"Skor: {skor_s}/80")
            m2.metric("Kualitas Tidur", kat_t, f"Skor: {skor_t}/21")

            st.info(
                f"**Perbandingan Data Riset:**\n"
                f"- Rata-rata skor riset: Stres **{rata_s:.1f}** | Tidur **{rata_t:.1f}**\n"
                f"- Kondisi sama di seluruh riset: **{jml_sama}/{total} mahasiswa ({persen_sama:.1f}%)**\n"
                f"- Kondisi sama di kelompok {pilih_gender}: **{jml_g}/{tot_g} orang ({persen_g:.1f}%)**"
            )

            st.subheader("💡 Saran Penanganan")
            st.write(f"**Untuk {kat_s}:**")
            for poin in saran_s:
                st.write(f"- {poin}")

            st.write(f"**Untuk {kat_t}:**")
            for poin in saran_t:
                st.write(f"- {poin}")

# ================= TAB 3: DATA RISET & RIWAYAT USER =================
with tab_data:
    sebaran_s, sebaran_t, tabel_silang = ringkasan_csv(df)

    st.subheader("1. Riwayat Pengguna yang Pernah Tes (`riwayat_tes.csv`)")
    df_riwayat = baca_riwayat()
    if df_riwayat is not None:
        st.dataframe(df_riwayat)
    else:
        st.info("Belum ada data pengisi. Coba isi kuesioner di Tab 'Mulai Tes', nanti datanya muncul di sini!")

    st.divider()
    st.subheader("2. Tabel Persilangan Data Riset Skripsi (`pd.crosstab`)")
    st.dataframe(tabel_silang)

    g1, g2 = st.columns(2)
    g1.bar_chart(sebaran_s)
    g2.bar_chart(sebaran_t)

    st.subheader("3. Data Mentah 40 Responden Skripsi (CSV)")
    st.dataframe(df)