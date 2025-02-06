import streamlit as st  # Por convenção, vamos apelidar o streamlit de st

# Aqui definimos o título da página e o layout como wide
st.set_page_config(page_title="Página principal",layout="wide")

#Título do seu dashboard
st.write("""
# Página principal
Seguem informações iniciais
""")

#python -m streamlit run init_page.py
#ou
#streamlit run init_page.py