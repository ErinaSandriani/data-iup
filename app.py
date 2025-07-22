import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
data = pd.read_csv('Dataset_Kelompok_16_Mini_Tim_B.csv')

# Title
st.title("Visualisasi Interaktif Data Program IUP")

# Sidebar Filter
st.sidebar.header("Filter Data")
selected_univ = st.sidebar.selectbox("Pilih Universitas:", sorted(data['Universitas'].unique()))
filtered_data_jurusan = data[data['Universitas'] == selected_univ]
selected_jurusan = st.sidebar.selectbox("Pilih Jurusan:", sorted(filtered_data_jurusan['Jurusan/Program Studi'].unique()))

# Filtered Row
filtered_row = data[
    (data['Universitas'] == selected_univ) &
    (data['Jurusan/Program Studi'] == selected_jurusan)
]

# Show Data Terpilih
st.subheader("Data Terpilih")
st.dataframe(filtered_row)

# Visualisasi Bar: Distribusi Daya Tampung per Universitas (dengan Highlight)
st.subheader("Distribusi Daya Tampung per Universitas")
highlight = selected_univ
colors = ['#FFA07A' if u == highlight else '#D3D3D3' for u in data['Universitas']]
fig1, ax1 = plt.subplots()
sns.barplot(data=data, x="Universitas", y="Daya Tampung", palette=colors, ax=ax1)
ax1.set_title("Daya Tampung Program IUP per Universitas")
plt.xticks(rotation=45)
st.pyplot(fig1)

# Visualisasi Biaya UKT per Jurusan (Highlight)
st.subheader("Distribusi Biaya UKT per Jurusan di " + selected_univ)
subset = data[data['Universitas'] == selected_univ]
colors2 = ['#90EE90' if j == selected_jurusan else '#D3D3D3' for j in subset['Jurusan/Program Studi']]
fig2, ax2 = plt.subplots()
sns.barplot(data=subset, x='Jurusan/Program Studi', y='Biaya UKT', palette=colors2, ax=ax2)
plt.xticks(rotation=90)
st.pyplot(fig2)

# Pie Chart Biaya UKT
st.subheader("Visualisasi Pie Chart Biaya UKT")
fig3, ax3 = plt.subplots()
ax3.pie(filtered_row['Biaya UKT'], labels=filtered_row['Jurusan/Program Studi'], autopct='%1.1f%%')
ax3.set_title(f"Biaya UKT {selected_jurusan} di {selected_univ}")
st.pyplot(fig3)

# Statistik Umum
st.subheader("Statistik Umum")
col1, col2 = st.columns(2)
with col1:
    st.metric("Rata-rata Biaya UKT", f"Rp{data['Biaya UKT'].mean():,.0f}")
    st.metric("Biaya UKT Tertinggi", f"Rp{data['Biaya UKT'].max():,.0f}")
    st.metric("Biaya UKT Terendah", f"Rp{data['Biaya UKT'].min():,.0f}")
with col2:
    st.metric("Rata-rata Daya Tampung", f"{data['Daya Tampung'].mean():.1f}")
    st.metric("Daya Tampung Tertinggi", f"{data['Daya Tampung'].max()}")
    st.metric("Daya Tampung Terendah", f"{data['Daya Tampung'].min()}")

# Rekomendasi Jurusan berdasarkan Budget
st.subheader("Rekomendasi Jurusan Berdasarkan Budget")
budget = st.slider("Masukkan Budget UKT Anda (Rp)", min_value=int(data['Biaya UKT'].min()), max_value=int(data['Biaya UKT'].max()), value=int(data['Biaya UKT'].mean()))
rekomendasi = data[data['Biaya UKT'] <= budget].sort_values(by='Biaya UKT')
st.write(f"Jurusan dengan Biaya UKT di bawah Rp{budget:,}:")
st.dataframe(rekomendasi[['Universitas', 'Jurusan/Program Studi', 'Biaya UKT']])

# Footer
st.markdown("---")
st.caption("Dibuat oleh Erina Sandriani – Magang Vinix Seven Aurum 2025")
