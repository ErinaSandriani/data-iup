import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Aplikasi
st.title("Analisis Data Program IUP PTN Indonesia")
st.subheader("Dataset: Survei Program IUP oleh Kelompok 16 Mini Tim B")

# Load Dataset
df = pd.read_csv("Dataset_Kelompok_16_Mini_Tim_B.csv")

# Tampilkan Data Mentah
if st.checkbox("Tampilkan Data Mentah"):
    st.write(df)

# Informasi Dataset
st.markdown("### Ringkasan Data")
st.write(df.describe(include='all'))

# Data Cleaning sederhana: Hapus duplikasi dan baris kosong
df_cleaned = df.drop_duplicates().dropna()

# Visualisasi: Pie Chart Jumlah Responden per Kampus
if 'Kampus' in df_cleaned.columns:
    st.markdown("### Distribusi Responden per Kampus")
    kampus_counts = df_cleaned['Kampus'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(kampus_counts, labels=kampus_counts.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

# Visualisasi: Barplot jika ada kolom Biaya
if 'Biaya' in df_cleaned.columns and 'Kampus' in df_cleaned.columns:
    st.markdown("### Rata-rata Biaya IUP per Kampus")
    df_cleaned['Biaya'] = pd.to_numeric(df_cleaned['Biaya'], errors='coerce')
    biaya_mean = df_cleaned.groupby('Kampus')['Biaya'].mean().sort_values()
    fig2, ax2 = plt.subplots()
    sns.barplot(x=biaya_mean.values, y=biaya_mean.index, ax=ax2)
    ax2.set_xlabel("Biaya (Rata-rata)")
    st.pyplot(fig2)

# Footer
st.caption("Dibuat oleh Erina Sandriani - Magang Vinix Seven Aurum 2025")
