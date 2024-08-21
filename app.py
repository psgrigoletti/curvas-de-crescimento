import streamlit as st

st.title('Consultar curvas de crescimento')

doenca = st.selectbox("Doença", ["Sem doença"])
sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])
idade_em_anos = st.number_input("Idade em anos", step=1)
peso_em_kg = st.number_input("Peso em Kg")
altura_em_cm = st.number_input("Altura em Cm")
if st.button("Consultar"):
    st.write("Gerar gráfico...")
