import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
data = pd.read_csv('Dataset_Kelompok_16_Mini_Tim_B.csv')

# Title
st.title("🎓 Dashboard Interaktif Program IUP")

# Sidebar
st.sidebar.header("🎯 Filter Data")
selected_univ = st.sidebar.selectbox("Pilih Universitas:", sorted(data['Universitas'].unique()))
filtered_jurusan = data[data['Universitas'] == selected_univ]
selected_jurusan = st.sidebar.selectbox("Pilih Jurusan:", sorted(filtered_jurusan['Jurusan/Program Studi'].unique()))

# Filtered Row
filtered_row = data[
    (data['Universitas'] == selected_univ) & 
    (data['Jurusan/Program Studi'] == selected_jurusan)
]

# Data Terpilih
st.subheader("📌 Data Terpilih")
st.dataframe(filtered_row)

# 1. Distribusi Daya Tampung per Universitas
st.subheader("📊 Daya Tampung per Universitas")
fig1 = px.bar(
    data,
    x='Universitas',
    y='Daya Tampung',
    color='Universitas',
    title='Daya Tampung Program IUP per PTN',
    color_discrete_sequence=px.colors.qualitative.Set3
)
fig1.update_layout(xaxis_title=None, yaxis_title="Daya Tampung", showlegend=False)
st.plotly_chart(fig1, use_container_width=True)

# 2. Biaya UKT per Jurusan (di univ terpilih)
st.subheader(f"💰 Biaya UKT per Jurusan di {selected_univ}")
fig2 = px.bar(
    filtered_jurusan,
    x='Jurusan/Program Studi',
    y='Biaya UKT',
    color='Jurusan/Program Studi',
    title=f"Perbandingan Biaya UKT di {selected_univ}",
    color_discrete_sequence=px.colors.qualitative.Vivid
)
fig2.update_layout(xaxis_tickangle=-45, showlegend=False)
st.plotly_chart(fig2, use_container_width=True)

# 3. Pie Chart – Komposisi Biaya UKT Jurusan Terpilih
st.subheader("📈 Proporsi Biaya UKT Jurusan Terpilih")
if not filtered_row.empty:
    fig3 = px.pie(
        names=["Terpilih", "Lainnya"],
        values=[filtered_row['Biaya UKT'].values[0], filtered_jurusan['Biaya UKT'].sum() - filtered_row['Biaya UKT'].values[0]],
        color_discrete_sequence=['#00CC96', '#FFD700'],
        title=f"Proporsi Biaya UKT {selected_jurusan}"
    )
    st.plotly_chart(fig3, use_container_width=True)

# 4. Statistik Umum
st.subheader("📊 Statistik Umum")
col1, col2 = st.columns(2)
with col1:
    st.metric("Rata-rata Biaya UKT", f"Rp{data['Biaya UKT'].mean():,.0f}")
    st.metric("Biaya UKT Tertinggi", f"Rp{data['Biaya UKT'].max():,.0f}")
    st.metric("Biaya UKT Terendah", f"Rp{data['Biaya UKT'].min():,.0f}")
with col2:
    st.metric("Rata-rata Daya Tampung", f"{data['Daya Tampung'].mean():.1f}")
    st.metric("Daya Tampung Tertinggi", f"{data['Daya Tampung'].max()}")
    st.metric("Daya Tampung Terendah", f"{data['Daya Tampung'].min()}")

# 5. Rekomendasi Jurusan Berdasarkan Budget
st.subheader("🎯 Rekomendasi Berdasarkan Budget")
budget = st.slider("Masukkan Budget UKT Anda (Rp)", min_value=int(data['Biaya UKT'].min()), max_value=int(data['Biaya UKT'].max()), value=int(data['Biaya UKT'].mean()))
rekomendasi = data[data['Biaya UKT'] <= budget].sort_values(by='Biaya UKT')
st.success(f"Jurusan dengan Biaya UKT di bawah Rp{budget:,}:")
st.dataframe(rekomendasi[['Universitas', 'Jurusan/Program Studi', 'Biaya UKT']])

# Footer
st.markdown("---")
st.caption("✨ Dibuat oleh Erina Sandriani – Magang Vinix Seven Aurum 2025")
