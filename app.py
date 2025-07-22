import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("Dataset_Kelompok_16_Mini_Tim_B.csv")

# Judul halaman
st.title("Visualisasi Data Program IUP PTN Indonesia")

# 1. Distribusi Daya Tampung per PTN
st.header("Distribusi Daya Tampung Program IUP per PTN")
plt.figure(figsize=(10, 6))
sns.barplot(x="Universitas", y="Daya Tampung", data=data, estimator=sum, ci=None)
plt.xticks(rotation=45)
st.pyplot(plt)

# 2. Perbandingan Biaya UKT Antar Jurusan di Setiap PTN
st.header("Perbandingan Biaya UKT Antar Jurusan di Setiap PTN")
plt.figure(figsize=(10, 6))
sns.boxplot(x="Universitas", y="Biaya UKT", data=data)
plt.xticks(rotation=45)
st.pyplot(plt)

# 3. Rasio Biaya UKT terhadap Daya Tampung per PTN
st.header("Rasio Biaya UKT terhadap Daya Tampung per PTN")
data["Rasio UKT/Daya Tampung"] = data["Biaya UKT"] / data["Daya Tampung"]
rasio_df = data.groupby("Universitas")["Rasio UKT/Daya Tampung"].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x="Universitas", y="Rasio UKT/Daya Tampung", data=rasio_df)
plt.xticks(rotation=45)
st.pyplot(plt)

# 4. Rata-rata Biaya UKT per PTN
st.header("Rata-rata Biaya UKT per PTN")
ukt_avg = data.groupby("Universitas")["Biaya UKT"].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x="Universitas", y="Biaya UKT", data=ukt_avg)
plt.xticks(rotation=45)
st.pyplot(plt)

# Footer
st.markdown("---")
st.markdown("Dibuat oleh Erina Sandriani - Magang Vinix Seven Aurum 2025")
