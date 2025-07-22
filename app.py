import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("Dataset_Kelompok_16_Mini_Tim_B.csv")

# Title
st.title("Visualisasi Interaktif Data Program IUP")

# Sidebar Filters
st.sidebar.header("Filter Data")
universitas_pilihan = st.sidebar.selectbox("Pilih Universitas:", sorted(df['Universitas'].unique()))
jurusan_pilihan = st.sidebar.selectbox("Pilih Jurusan:", sorted(df['Jurusan/Program Studi'].unique()))

# Filter Data untuk Highlight
highlight_df = df[(df["Universitas"] == universitas_pilihan) & (df["Jurusan/Program Studi"] == jurusan_pilihan)]

# Tampilkan Data Terpilih
st.subheader("Data Terpilih")
st.dataframe(highlight_df)

# Buat kolom warna untuk highlight
df['Highlight'] = df.apply(lambda row: 
    'Highlight' if (row['Universitas'] == universitas_pilihan and row['Jurusan/Program Studi'] == jurusan_pilihan)
    else 'Lainnya', axis=1)

# Warna
warna_map = {'Highlight': '#FF5733', 'Lainnya': '#C0C0C0'}

# Visualisasi 1: Daya Tampung per PTN
st.subheader("Distribusi Daya Tampung per Universitas")
fig1, ax1 = plt.subplots(figsize=(10,5))
sns.barplot(data=df, x='Universitas', y='Daya Tampung', hue='Highlight', palette=warna_map, dodge=False, ax=ax1)
plt.xticks(rotation=45)
plt.title("Daya Tampung Program IUP per Universitas")
st.pyplot(fig1)

# Visualisasi 2: Perbandingan Biaya UKT antar Jurusan per PTN
st.subheader("Perbandingan Biaya UKT antar Jurusan di Setiap PTN")
fig2, ax2 = plt.subplots(figsize=(10,5))
sns.scatterplot(data=df, x='Universitas', y='Biaya UKT', hue='Highlight', palette=warna_map, ax=ax2, s=100)
plt.xticks(rotation=45)
plt.title("Biaya UKT antar Jurusan")
st.pyplot(fig2)

# Visualisasi 3: Rasio Biaya UKT per Daya Tampung
st.subheader("Rasio Biaya UKT terhadap Daya Tampung")
df['Rasio'] = df['Biaya UKT'] / df['Daya Tampung']
fig3, ax3 = plt.subplots(figsize=(10,5))
sns.barplot(data=df, x='Universitas', y='Rasio', hue='Highlight', palette=warna_map, dodge=False, ax=ax3)
plt.xticks(rotation=45)
plt.title("Rasio Biaya UKT / Daya Tampung per Universitas")
st.pyplot(fig3)

# Visualisasi 4: Rata-rata Biaya UKT per PTN
st.subheader("Rata-rata Biaya UKT per Universitas")
avg_ukt = df.groupby('Universitas')['Biaya UKT'].mean().reset_index()
avg_ukt['Highlight'] = avg_ukt['Universitas'].apply(
    lambda x: 'Highlight' if x == universitas_pilihan else 'Lainnya'
)
fig4, ax4 = plt.subplots(figsize=(10,5))
sns.barplot(data=avg_ukt, x='Universitas', y='Biaya UKT', hue='Highlight', palette=warna_map, dodge=False, ax=ax4)
plt.xticks(rotation=45)
plt.title("Rata-rata UKT Program IUP")
st.pyplot(fig4)

# Footer
st.markdown("<br><hr><center>Dibuat oleh Erina Sandriani - Magang Vinix Seven Aurum 2025</center>", unsafe_allow_html=True)
