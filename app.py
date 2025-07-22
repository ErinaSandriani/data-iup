import streamlit as st
import pandas as pd
import plotly.express as px

# Judul Aplikasi
st.set_page_config(page_title="Visualisasi Interaktif Data Program IUP", layout="wide")
st.title("Visualisasi Interaktif Data Program IUP")

# Load data
df = pd.read_csv("Dataset_Kelompok_16_Mini_Tim_B.csv")

# Menampilkan kolom untuk debug jika diperlukan
# st.write("Kolom dalam dataset:", df.columns.tolist())

# Perbaikan: nama kolom harus persis sesuai yang ada di CSV
df = df.dropna(subset=["Universitas", "Jurusan/Program Studi", "Biaya UKT", "Daya Tampung"])

# Sidebar filter
st.sidebar.header("Filter Data")
selected_univ = st.sidebar.selectbox("Pilih Universitas:", df["Universitas"].unique())
filtered_df = df[df["Universitas"] == selected_univ]

selected_jurusan = st.sidebar.selectbox("Pilih Jurusan:", filtered_df["Jurusan/Program Studi"].unique())
final_df = filtered_df[filtered_df["Jurusan/Program Studi"] == selected_jurusan]

# Tampilkan data yang terpilih
st.subheader("Data Terpilih")
st.dataframe(final_df)

# Bar chart semua universitas (dengan highlight yang dipilih)
st.subheader("Distribusi Daya Tampung per Universitas")

highlight_df = df.copy()
highlight_df["Highlight"] = highlight_df.apply(
    lambda row: "Highlight" if (row["Universitas"] == selected_univ and row["Jurusan/Program Studi"] == selected_jurusan) else "Lainnya",
    axis=1
)

fig1 = px.bar(
    highlight_df,
    x="Universitas",
    y="Daya Tampung",
    color="Highlight",
    title="Daya Tampung Program IUP per Universitas",
    color_discrete_map={"Highlight": "#EF553B", "Lainnya": "lightgray"}
)
st.plotly_chart(fig1, use_container_width=True)

# Bar chart semua universitas untuk Biaya UKT
st.subheader("Distribusi Biaya UKT per Universitas")

fig2 = px.bar(
    highlight_df,
    x="Universitas",
    y="Biaya UKT",
    color="Highlight",
    title="Biaya UKT Program IUP per Universitas",
    color_discrete_map={"Highlight": "#00CC96", "Lainnya": "lightgray"}
)
st.plotly_chart(fig2, use_container_width=True)

# Visualisasi pie chart dan bar chart per data terpilih
st.subheader("Visualisasi Daya Tampung dan Biaya UKT")

col1, col2 = st.columns(2)

with col1:
    fig3 = px.pie(final_df, names="Jurusan/Program Studi", values="Daya Tampung",
                  title=f"Pie Chart Daya Tampung untuk {selected_jurusan} di {selected_univ}")
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    fig4 = px.bar(final_df, x="Jurusan/Program Studi", y="Biaya UKT",
                  title=f"Bar Chart Biaya UKT untuk {selected_jurusan} di {selected_univ}",
                  color_discrete_sequence=["#636EFA"])
    st.plotly_chart(fig4, use_container_width=True)

# Footer
st.markdown(
    "<br><hr><center>Dibuat oleh Erina Sandriani - Magang Vinix Seven Aurum 2025</center>",
    unsafe_allow_html=True
)
