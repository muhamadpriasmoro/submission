import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load main_data.csv
main_data = pd.read_csv("./dashboard/main_data.csv")

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://raw.githubusercontent.com/muhamadpriasmoro/dicoding_project/main/picture/bike.jpg")
    st.write("Proyek Analisis Data: Bike Sharing") 
    st.write("Nama: Muhamad Priasmoro")
    st.write("Email: priasmorosejati@gmail.com")
    st.write("ID Dicoding: priasmoro")

# Title
st.title('Proyek Analisis Data')

# Visualization & Explanatory Analysis
st.header('Visualization & Explanatory Analysis')

# Pertanyaan 1: Hubungan Antara Suhu dan Jumlah Penyewaan Sepeda
st.subheader('Pertanyaan 1: Hubungan Korelasi Antara Suhu dan Jumlah Penyewaan Sepeda')

# Memilih kolom suhu (temp_x) dan jumlah penyewaan sepeda (cnt_x)
selected_df = main_data[['temp_x', 'cnt_x', 'dteday_y', 'yr_y', 'hr', 'cnt_y']]

# Menghitung korelasi antara suhu dan jumlah penyewaan sepeda
correlation = selected_df['temp_x'].corr(selected_df['cnt_x'])
st.write(f"Korelasi antara suhu dan jumlah penyewaan sepeda: {correlation}")

# Membuat scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(selected_df['temp_x'], selected_df['cnt_x'], color='blue', alpha=0.5)
ax.set_xlabel('Suhu (temp)')
ax.set_ylabel('Jumlah Penyewaan Sepeda (cnt)')
ax.set_title('Hubungan Antara Suhu dan Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Pertanyaan 2: Jumlah Penyewaan Sepeda pada Liburan Musim Panas Tahun 2012
st.subheader('Pertanyaan 2: Jumlah Penyewaan Sepeda pada Liburan Musim Panas Tahun 2012')

# Filter untuk liburan musim panas tahun 2012
try:
    summer_holiday_2012 = main_data[(main_data["dteday_x"].str.startswith("2012")) & (main_data["season_x"] == 2) & (main_data["holiday_x"] == 1)]
    total_bikes_summer_2012 = summer_holiday_2012["cnt_x"].sum()
    st.write(f"Jumlah total sepeda yang disewakan pada liburan musim panas tahun 2012 adalah: {total_bikes_summer_2012}")
except KeyError:
    st.write("Column 'yr' is not present in the DataFrame.")

# Pertanyaan 3: Distribusi Penyewaan Sepeda pada Hari Natal Tahun 2011
# Title
st.subheader('Pertanyaan 3: Distribusi Per Jam Penyewaan Sepeda pada Hari Natal (2011)')

st.image("https://raw.githubusercontent.com/muhamadpriasmoro/dicoding_project/main/picture/fitered.png")

# Plot distribusi per jam sewa sepeda
st.image("https://raw.githubusercontent.com/muhamadpriasmoro/dicoding_project/main/picture/cahart.png")

st.header('Conclusion')
st.markdown("""
- **Conclusion Pertanyaan 1:**\
  Terdapat pola korelasi antara jumlah penyewaan sepeda dengan suhu. Korelasi antara suhu dan jumlah penyewaan sepeda adalah 0.6274940090334918, yang menunjukkan hubungan positif yang cukup kuat. Semakin hangat suhu, semakin banyak yang menyewa sepeda.

- **Conclusion Pertanyaan 2:**\
  Jumlah total sepeda yang disewakan pada liburan musim panas tahun 2012 adalah sebanyak 12.413.

- **Conclusion Pertanyaan 3:**\
  Terjadi peningkatan penyewaan sepeda pada jam 13 - 15 pada Hari Natal tahun 2011.
""")
