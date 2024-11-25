# Importa a biblioteca streamlit e datetime para manipulação de datas
import streamlit as st
from main import bot

# Título da página
st.title("Bot Baixar XML 🤖")

dt_inicial = st.date_input(label= "Data de Emissão Inicial", format="DD/MM/YYYY")
dt_final = st.date_input(label="Data de Emissão Final", format="DD/MM/YYYY")

fornecedores = ["AVINE COMERCIAL E AVICULA DO NORD LTDA", "AGRICOLA FAMOSA LTDA", "DEFAVERI E CAPPELLARO PROD E COM FRUTAS", "AVINE ALIMENTOS INDUSTRIALIZADOS LTDA", "CLAUDIA REGINA CECCAGNO CAPPELLARO EIREL"]
fornecedor = st.selectbox("Escolha o fornecedor:", fornecedores)

if st.button("Iniciar automação"):
    bot(dt_inicial, dt_final, fornecedor)
