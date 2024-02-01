import streamlit as st
import eda
import prediction

PAGES = {
    "Exploration Data Analysis": eda,
    "Prediction": prediction
}

page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Prediction'])

if page == 'Home Page':

    with st.columns(3)[1]:
        st.header('Welcome Page')
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSmzBS6rNnS-WM6H4STTHomATSn51OvU_wM5u8hzsfrHxT8H4FFUjcrGzF1dy6AIC3ZRk&usqp=CAU')
    st.write('')
    st.write('Tujuan Project   : Memprediksi Permohonan Pinjaman Menggunakan Model Klasifikasi')
    st.write('')

    with st.expander("Latar Belakang"):
        st.caption('Prediksi Persetujuan Pinjaman dibuat untuk membantu bank menyelesaikan masalah dalam menilai apakah pemohon pinjaman layak mendapatkan pinjaman atau tidak.')
        st.caption('Dengan menggunakan model ini, kita dapat memprediksi persetujuan pinjaman dengan lebih objektif untuk mengurangi risiko kecenderungan yang dapat mempengaruhi keputusan dan memastikan setiap pemohon pinjaman diperlakukan secara adil.')

    with st.expander("Kesimpulan"):
        st.caption('''
    
    - Dataset terdiri dari 4269 baris dengan 13 kolom termasuk target `loan_status`.

    - Dilakukan oversampling untuk menangani ketidakseimbangan data dengan menggunakan SMOTE.
                   
    - Empat model klasifikasi yang diuji: K-Nearest Neighbors (KNN), Support Vector Machine (SVM), Random Forest (RF),  Decision Tree (Tree), dan Gradient Boosting (GB). 
    
    - Matrix evaluasi yang dipilih adalah precision. Alasan penggunaannya karena dalam konteks pinjaman 'precision' dapat membantu mengukur seberapa akurat model dapat memprediksi persetujuan pinjaman.
                   
    - Model Gradient Boosting (GB) dipilih sebagai model terbaik berdasarkan hasil cross-validation dan evaluasi kinerja pada data test.
    
    - Kelebihan Model GB adalah cenderung emiliki akurasi yang tinggi karena mampu memperbaiki kesalahan prediksi model sebelumnya. Namun kekurangannya adalah rentan terhadap overfitting.''')

    st.caption('Untuk memulai, silakan pilih menu lain pada Select Box di sebelah kiri layar Anda')
    st.write('')
    st.write('')


elif page == 'Exploration Data Analysis':
    eda.app()
else:
    prediction.app()


