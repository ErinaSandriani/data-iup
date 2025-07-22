import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("Dataset_Kelompok_16_Mini_Tim_B.csv")

# Judul aplikasi
st.title("Visualisasi Interaktif Data Program IUP")

# Sidebar filter
st.sidebar.header("Filter Data")
universitas = st.sidebar.selectbox("Pilih Universitas:", sorted(data["Universitas"].unique()))
jurusan = st.sidebar.selectbox("Pilih Jurusan:", sorted(data[data["Universitas"] == universitas]["Jurusan/Program Studi"].unique()))

# Filter data
filtered_data = data[(data["Universitas"] == universitas) & (data["Jurusan/Program Studi"] == jurusan)]

# Tampilkan data
st.subheader("Data Terpilih")
st.dataframe(filtered_data)

# Visualisasi Daya Tampung
st.subheader("Visualisasi Daya Tampung dan Biaya UKT")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"**Pie Chart Daya Tampung untuk {jurusan} di {universitas}**")
    plt.figure(figsize=(4, 4))
    plt.pie(filtered_data["Daya Tampung"], labels=filtered_data["Jurusan/Program Studi"], autopct='%1.1f%%', colors=sns.color_palette("Set2"))
    st.pyplot(plt.gcf())
    plt.clf()

with col2:
    st.markdown(f"**Bar Chart Biaya UKT untuk {jurusan} di {universitas}**")
    plt.figure(figsize=(6, 4))
    sns.barplot(data=filtered_data, x="Jurusan/Program Studi", y="Biaya UKT", palette="coolwarm")
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())
    plt.clf()

# Footer
st.markdown("---")
st.markdown("**Dibuat oleh Erina Sandriani - Magang Vinix Seven Aurum 2025**")
