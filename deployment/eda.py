import streamlit as st
from PIL import Image

def app():
    st.title('Exploration Data Analysis')

    
    st.subheader('Mengetahui Persentase Permohonan Pinjaman yang Disetujui dengan Permohonan Pinjaman yang Ditolak')
    image = Image.open('eda1.png')
    st.image(image, caption='figure 1')

    with st.expander('Notes'):
        st.caption('Persentase pinjaman yang disetujui adalah sebesar 62.2%, sedangkan pinjaman yang ditolak adalah sebesar 37.8%. Dapat disimpulkan bahwa persentase pinjaman yang disetujui lebih besar dibandingkan dengan persentase pinjaman yang ditolak.')


    st.subheader('Mengetahui Pengaruh Skor Kredit Terhadap Status Pinjaman')
    image = Image.open('eda2.png')
    st.image(image, caption='figure 2')

    with st.expander('Notes'):
        st.caption('Semakin tinggi nilai kredit skor, maka semakin besar peluang permohonan pinjaman disetujui.')



    st.subheader('Mengetahui Pengaruh Status Pekerjaan Terhadap Status Pinjaman')
    image = Image.open('eda3.png')
    st.image(image, caption='figure 3')

    with st.expander('Notes'):
        st.caption('Status pekerjaan pemohon baik yang bekerja maupun yang tidak bekerja tidak berdampak signifikan terhadap status pinjaman. Terlihat bahwa jumlah status pinjaman disetujui dan pinjaman ditolak pada setiap status pekerjaan memiliki persentase yang sama.')

    st.subheader('Mengetahui Distribusi Data dari Jumlah Pinjaman dan mengetahui 3 Jumlah Pinjaman Tertinggi')
    image = Image.open('eda4.png')
    st.image(image, caption='figure 4')

    with st.expander('Notes'):
        st.caption('Persebaran distribusi pada data jumlah pinjaman menunjukkan adanya kemiringan ke kanan (positif) dan ekor distribusi lebih panjang ke sebelah kanan. Kemudian untuk 3 jumlah pinjaman tertinggi diposisi pertama adalah pemohon dengan loan ID 509 dengan jumlah pinjaman sebesar 39.500.000, kemudian diposisi kedua adalah pemohon dengan loan ID 258 dengan jumlah pinjaman sebesar 38.800.000, dan diposisi ketiga adalah pemohon dengan loan ID 1027 dengan jumlah pinjaman sebesar 38.700.000.')

    st.subheader('Mengetahui Pengaruh Jangka Waktu Pinjaman Terhadap Status Pinjaman')
    image = Image.open('eda5.png')
    st.image(image, caption='figure 5')

    with st.expander('Notes'):
        st.caption('Pinjaman dengan jangka waktu yang lebih lama cenderung lebih sering ditolak daripada pinjaman dengan jangka waktu yang lebih pendek. Sedangkat pinjaman dengan jangka waktu yang pendek cenderung memiliki peluang besar untuk disetujui. Sedangkan pinjaman dengan jangka waktu yang lebih pendek cenderung memiliki peluang yang lebih besar untuk disetujui.')

    
    st.subheader('Mengetahui Hubungan antara Jumlah Pendapatan perTahun terhadap vs Jumlah Pinjaman')
    image = Image.open('eda6.png')
    st.image(image, caption='figure 6')

    with st.expander('Notes'):
        st.caption('Jumlah pendapatan pertahun dengan jumlah pinjaman memiliki korelasi positif. Artinya semakin tinggi jumlah pendapatan pertahun, maka semakin besar jumlah pinjaman yang diajukan.')

