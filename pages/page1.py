import streamlit as st

st.title("Olá, Mundo no Streamlit! 🎈")
st.write("Este é um exemplo simples de aplicativo web.")
nome = st.text_input("Digite seu nome:")
if nome:
    st.write(f"Bem-vindo, {nome}!")
