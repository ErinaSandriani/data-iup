import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("Dataset_Kelompok_16_Mini_Tim_B.csv")

# Bersihkan data jika perlu
df = df.dropna(subset=["Universitas", "Program Studi", "UKT", "Daya Tampung"])

# Ubah kolom UKT dan Daya Tampung ke numerik
df["UKT"] = pd.to_numeric(df["UKT"], errors="coerce")
df["Daya Tampung"] = pd.to_numeric(df["Daya Tampung"], errors="coerce")

# Judul Aplikasi
st.title("Rekomendasi Jurusan Berdasarkan Budget UKT")
st.markdown("Aplikasi ini membantu pengguna menemukan jurusan yang sesuai dengan anggaran UKT yang dimiliki.")

# Input dari pengguna
budget = st.slider("Masukkan batas maksimal biaya UKT (Rp)", min_value=1000000, max_value=40000000, step=500000)

# Filter berdasarkan budget
filtered_df = df[df["UKT"] <= budget]

# Tampilkan hasil
st.subheader("Rekomendasi Program Studi")
if not filtered_df.empty:
    st.write(f"Menampilkan jurusan dengan UKT di bawah Rp {budget:,}")
    st.dataframe(filtered_df[["Universitas", "Program Studi", "UKT", "Daya Tampung"]].sort_values("UKT"))
    
    # Visualisasi
    fig = px.bar(filtered_df.sort_values("UKT").head(10),
                 x="Program Studi",
                 y="UKT",
                 color="Universitas",
                 title="10 Jurusan dengan UKT Terendah Sesuai Budget",
                 labels={"UKT": "Biaya UKT (Rp)"})
    st.plotly_chart(fig)
else:
    st.warning("Tidak ada jurusan yang sesuai dengan budget yang dimasukkan.")
