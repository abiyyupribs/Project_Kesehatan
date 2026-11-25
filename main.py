# ==============================================================================
# FILE: main.py (Super Pendek - Cuma Tampilan Utama & Import Modul)
# ==============================================================================

import os
import pandas as pd
import streamlit as st

from soal import (
    PILIHAN_DASS, SOAL_STRES, SOAL_CEMAS, SOAL_DEPRESI, SOAL_TIDUR,
    cek_stres, cek_cemas, cek_depresi, cek_tidur,
)
from materi import INFO_STRES, INFO_DASS42, INFO_PSQI, KENAPA_HARUS_TES
from analisis import cek_kemiripan_jurnal, ambil_saran_stres, ambil_saran_tidur, simpan_riwayat

st.set_page_config(page_title="Cek Stres & Tidur Mahasiswa", page_icon="🩺", layout="wide")
st.title("🩺 Aplikasi Deteksi Dini Stres & Kualitas Tidur Mahasiswa")
st.write("Instrumen baku **DASS-42** & **PSQI** berdasarkan rujukan **3 Jurnal Ilmiah**.")

# Fungsi tampilkan soal DASS-42 pakai tombol radio menyamping
def tanya_dass(daftar_soal, kode):
    return [st.radio(teks, PILIHAN_DASS, index=None, horizontal=True, key=f"{kode}_{i}") for i, teks in enumerate(daftar_soal)]

tab1, tab2, tab3 = st.tabs(["📚 1. Pengenalan & 3 Jurnal", "📝 2. Isi Kuesioner", "📊 3. Hasil & Riwayat"])

# ==================== TAB 1: MATERI & 3 JURNAL ====================
with tab1:
    k1, k2 = st.columns(2)
    k1.info(f"**Apa itu Stres Akademik?**\n\n{INFO_STRES}")
    k2.info(f"**Kenapa Harus Deteksi Dini?**\n\n{KENAPA_HARUS_TES}")

    k3, k4 = st.columns(2)
    k3.success(f"**Apa itu Kuesioner DASS-42?**\n\n{INFO_DASS42}")
    k4.success(f"**Apa itu Kuesioner PSQI?**\n\n{INFO_PSQI}")

    st.divider()
    df_jurnal = pd.read_csv("referensi_jurnal.csv")
    st.dataframe(df_jurnal, use_container_width=True, hide_index=True)
    st.bar_chart(df_jurnal, x="Penulis", y=["Stres_Sedang_Berat_Persen", "Tidur_Buruk_Persen"])

# ==================== TAB 2: KUESIONER ====================
with tab2:
    st.info("📌 **Petunjuk:** Jawab berdasarkan kondisi yang kamu rasakan **selama 1 minggu terakhir**.")

    with st.form("form_tes"):
        c1, c2, c3 = st.columns(3)
        nama = c1.text_input("Nama / Inisial", placeholder="Contoh: Mhs_01")
        gender = c2.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        umur = c3.number_input("Umur", min_value=17, max_value=35, value=21)

        st.markdown("### Bagian A: Tingkat Stres (DASS-42)")
        jawab_stres = tanya_dass(SOAL_STRES, "stres")

        st.markdown("### Bagian B: Tingkat Kecemasan (DASS-42)")
        jawab_cemas = tanya_dass(SOAL_CEMAS, "cemas")

        st.markdown("### Bagian C: Tingkat Depresi (DASS-42)")
        jawab_depresi = tanya_dass(SOAL_DEPRESI, "depresi")

        st.markdown("### Bagian D: Kualitas Tidur (PSQI)")
        jawab_tidur = [st.radio(t, p, index=None, key=f"tidur_{i}") for i, (t, p) in enumerate(SOAL_TIDUR)]

        klik_hitung = st.form_submit_button("✅ Hitung Hasil & Lihat Saran", type="primary")

    if klik_hitung:
        nama_bersih = nama.strip()
        if nama_bersih == "" or None in (jawab_stres + jawab_cemas + jawab_depresi + jawab_tidur):
            st.warning("Pastikan nama sudah diisi dan semua pertanyaan sudah dijawab ya bray!")
        else:
            if nama_bersih[0] in ["=", "+", "-", "@"]:
                nama_bersih = "'" + nama_bersih

            # Hitung skor & kategori pakai modul soal.py
            s_stres, s_cemas = sum(int(j[0]) for j in jawab_stres), sum(int(j[0]) for j in jawab_cemas)
            s_depresi, s_tidur = sum(int(j[0]) for j in jawab_depresi), sum(int(j[0]) for j in jawab_tidur)
            k_stres, k_cemas = cek_stres(s_stres), cek_cemas(s_cemas)
            k_depresi, k_tidur = cek_depresi(s_depresi), cek_tidur(s_tidur)

            # Simpan & bandingkan hasil pakai modul analisis.py
            simpan_riwayat(nama_bersih, gender, umur, s_stres, k_stres, s_cemas, k_cemas, s_depresi, k_depresi, s_tidur, k_tidur)
            mirip_stres, mirip_tidur = cek_kemiripan_jurnal(k_stres, k_tidur)

            st.success(f"Hasil untuk **{nama_bersih}** berhasil disimpan!")
            h1, h2, h3, h4 = st.columns(4)
            h1.metric("Stres", f"{s_stres}/42", k_stres)
            h2.metric("Kecemasan", f"{s_cemas}/42", k_cemas)
            h3.metric("Depresi", f"{s_depresi}/42", k_depresi)
            h4.metric("Kualitas Tidur", f"{s_tidur}/21", k_tidur)

            st.info(f"📊 **Kemiripan dengan 245 Responden (3 Jurnal):**\n- **Stres:** {mirip_stres}\n- **Tidur:** {mirip_tidur}")

            s1, s2 = st.columns(2)
            s1.write(f"**Saran Stres ({k_stres}):**\n" + "\n".join(f"- {p}" for p in ambil_saran_stres(k_stres)))
            s2.write(f"**Saran Tidur ({k_tidur}):**\n" + "\n".join(f"- {p}" for p in ambil_saran_tidur(k_tidur)))

# ==================== TAB 3: RIWAYAT ====================
with tab3:
    if os.path.exists("riwayat_tes.csv"):
        df_riwayat = pd.read_csv("riwayat_tes.csv")
        st.write("**Hasil Tes Paling Baru:**")
        st.dataframe(df_riwayat.tail(1), use_container_width=True, hide_index=True)
        st.write("**Semua Riwayat Pengguna:**")
        st.dataframe(df_riwayat, use_container_width=True, hide_index=True)
    else:
        st.info("Belum ada data tes. Silakan isi kuesioner di Tab 2 dulu.")