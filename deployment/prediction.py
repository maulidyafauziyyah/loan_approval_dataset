import streamlit as st
import pandas as pd
import joblib
from PIL import Image

def app():
# Load All Files

    with open('model.pkl', 'rb') as file:
        full_process = joblib.load(file)
    
    st.title("Loan Status Data")
    
    df = pd.read_csv('loan_approval_dataset.csv')    
    st.write(df) 

    st.title("Loan Status Prediction")
    st.write('---')

    st.image('https://previews.123rf.com/images/bsd555/bsd5552002/bsd555200201831/140754430-get-approval-concept-icon-loan-and-credit-legal-certificate-official-confirmation-corporate-document.jpg')

    st.write('Pilih dan Isi Sesuai Data Diri Anda')


    # loan_id = st.number_input(label='Masukkan Nomor Pinjaman', min_value=0,max_value=9999999)
    # no_of_dependents = st.number_input(label='Masukkan Jumlah Tanggungan', min_value=0,max_value=10)
    # education = st.selectbox(label='Pilih Status Pendidikan', options=['Graduate','Not Graduate'])
    # self_employed = st.selectbox(label='Pilih Status Pekerjaan', options=['Yes (Bekerja)','No (Tidak Bekerja)'])
    # income_annum = st.number_input(label='Masukkan Pendapatan per Tahun', min_value=0,max_value=9999999)
    # loan_amount = st.number_input(label='Masukkan Jumlah Pinjaman', min_value=0,max_value=90000000)
    loan_term = st.selectbox(label='Pilih Jangka Waktu Pinjaman (dalam Tahun)', options=[2,4,6,8,10,12])
    cibil_score = st.slider('Geser Untuk Memasukkan Skor Kredit Anda', 300, 900)
    # residential_assets_value = st.number_input(label='Masukkan Nilai Aset Properti', min_value=0,max_value=99999999)
    # commercial_assets_value = st.number_input(label='Masukkan Nilai Aset Komersial', min_value=0,max_value=99999999)
    # luxury_assets_value = st.number_input(label='Masukkan Nilai Aset Barang Mewah', min_value=0,max_value=99999999)
    # bank_asset_value = st.number_input(label='Masukkan Nilai Aset di Bank', min_value=0,max_value=99999999)
    
    st.write('Berikut adalah hasil dari data yang telah Anda masukkan : ')
    

    data_inf = pd.DataFrame({
        # 'no_of_dependents' : no_of_dependents,
        # 'education' : education,
        # 'self_employed' : self_employed,
        # 'income_annum' : income_annum,
        # 'loan_amount' : loan_amount,
        'loan_term' : loan_term,
        'cibil_score' : cibil_score,
        # 'residential_assets_value' : residential_assets_value,
        # 'commercial_assets_value' : commercial_assets_value,
        # 'luxury_assets_value' : luxury_assets_value,
        # 'bank_asset_value' : bank_asset_value,
        }, index=[0])

    st.table(data_inf)

    if st.button("Predict"):
            prediction =  full_process.predict(data_inf)

            if prediction[0] == 1:
                prediction = 'Permohonan Pinjaman Anda Disetujui'
            else:
                prediction = 'Permohonan Pinjaman Anda Tidak Disetujui'

            st.subheader('Hasil model prediksi adalah :')
            st.subheader(prediction)

if __name__ == "__name__":
     app()