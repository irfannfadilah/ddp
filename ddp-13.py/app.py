import streamlit as st 


st.write('hello')

dashboard = st.Page("./pages/dashboard.py", title="Dashboard")
nabung = st.Page("./pages/nabung.py", title="nabung")

pg = st.navigation({
    "Dashboard": [dashboard],
    "Nabung": [nabung],
})

if "Nabung" not in st.session_state:
    st.session_state['Nabung'] = []
    
pg.run()