import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Dataset_Kelompok_16_Mini_Tim_B.csv")

# Judul
st.title("Visualisasi Interaktif Data Program IUP")

# Pilihan interaktif untuk jurusan dan universitas
selected_univ = st.selectbox("Pilih Universitas:", df["Universitas"].unique())
selected_jurusan = st.selectbox("Pilih Jurusan:", df[df["Universitas"] == selected_univ]["Jurusan/Program Studi"].unique())

# Filter data
filtered_df = df[(df["Universitas"] == selected_univ) & (df["Jurusan/Program Studi"] == selected_jurusan)]

# Tampilkan hasil
st.subheader("Data Terpilih")
st.write(filtered_df)

# Visualisasi
if not filtered_df.empty:
    st.subheader("Visualisasi Perbandingan Daya Tampung dan Biaya UKT")
    fig, ax = plt.subplots()
    sns.barplot(data=filtered_df, x="Jurusan/Program Studi", y="Daya Tampung", ax=ax)
    ax.set_title(f"Daya Tampung untuk {selected_jurusan} di {selected_univ}")
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    sns.barplot(data=filtered_df, x="Jurusan/Program Studi", y="Biaya UKT", ax=ax2)
    ax2.set_title(f"Biaya UKT untuk {selected_jurusan} di {selected_univ}")
    st.pyplot(fig2)
else:
    st.write("Tidak ada data untuk kombinasi tersebut.")
