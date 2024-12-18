import streamlit as st 

st.title("Halaman Nabung")

with st.form("nabung"):
    nama = st.text_input("Masukan Nama")
    nominal = st.number_input("Masukan Nominal")
    submit_button = st.form_submit_button("Simpan")

    if submit_button:
        st.write(nama)
        st.session_state['Nabung']. append({
            "Nama" : nama,
            "Nominal" : nominal,
        })
        st.success("Berhasil Nabung")