import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
from tabelas import *

def classificar_e_plotar(sexo, idade_em_meses, altura_em_cm=None, peso_em_kg=None):
    if sexo.lower() == 'feminino':
        df_peso = df_peso_meninas
        df_altura = df_altura_meninas
    elif sexo.lower() == 'masculino':
        df_peso = df_peso_meninos
        df_altura = df_altura_meninos
    else:
        raise ValueError("Sexo deve ser 'MASCULINO' ou 'FEMININO'")
    
    if peso_em_kg is not None:
        peso_min = df_peso["Peso mínimo (kg)"].iloc[idade_em_meses]
        peso_medio = df_peso["Peso médio (kg)"].iloc[idade_em_meses]
        peso_max = df_peso["Peso máximo (kg)"].iloc[idade_em_meses]
        
        classificacao = None
        if peso_em_kg < peso_min:
            classificacao = "Abaixo do esperado"
        elif peso_em_kg > peso_max:
            classificacao = "Acima do esperado"
        else:
            classificacao = "Dentro do esperado"
        
        # Plotagem
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_peso["Idade (meses)"], y=df_peso["Peso mínimo (kg)"], 
                                 mode='lines+markers', name='Peso Mínimo'))
        fig.add_trace(go.Scatter(x=df_peso["Idade (meses)"], y=df_peso["Peso médio (kg)"], 
                                 mode='lines+markers', name='Peso Médio'))
        fig.add_trace(go.Scatter(x=df_peso["Idade (meses)"], y=df_peso["Peso máximo (kg)"], 
                                 mode='lines+markers', name='Peso Máximo'))
        fig.add_trace(go.Scatter(x=[idade_em_meses], y=[peso_em_kg], 
                                 mode='markers', name='Seu Peso', 
                                 marker=dict(color='firebrick', size=10, symbol='x')))
        fig.update_layout(title=f'Classificação do Peso: {classificacao}',
                          xaxis_title='Idade (meses)',
                          yaxis_title='Peso (kg)')
        return classificacao, fig

    if altura_em_cm is not None:
        altura_min = df_altura["Altura mínima (cm)"].iloc[idade_em_meses]
        altura_medio = df_altura["Altura média (cm)"].iloc[idade_em_meses]
        altura_max = df_altura["Altura máxima (cm)"].iloc[idade_em_meses]
        
        classificacao = None
        if altura_em_cm < altura_min:
            classificacao = "Abaixo do esperado"
        elif altura_em_cm > altura_max:
            classificacao = "Acima do esperado"
        else:
            classificacao = "Dentro do esperado"
        
        # Plotagem
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_altura["Idade (meses)"], y=df_altura["Altura mínima (cm)"], 
                                 mode='lines+markers', name='Altura Mínima'))
        fig.add_trace(go.Scatter(x=df_altura["Idade (meses)"], y=df_altura["Altura média (cm)"], 
                                 mode='lines+markers', name='Altura Média'))
        fig.add_trace(go.Scatter(x=df_altura["Idade (meses)"], y=df_altura["Altura máxima (cm)"], 
                                 mode='lines+markers', name='Altura Máxima'))
        fig.add_trace(go.Scatter(x=[idade_em_meses], y=[altura_em_cm], 
                                 mode='markers', name='Sua Altura', 
                                 marker=dict(color='firebrick', size=10, symbol='x')))
        fig.update_layout(title=f'Classificação da Altura: {classificacao}',
                          xaxis_title='Idade (meses)',
                          yaxis_title='Altura (cm)')
        return classificacao, fig


# Exemplo de uso
st.write('# Consultar curvas de crescimento')
st.write('*Nutricionista Fernanda Schumacher*')

st.write('# Parâmetros')

coluna_sexo, coluna_nome, coluna_doenca = st.columns([2, 2, 4])
with coluna_sexo:
    sexo = st.selectbox("Sexo:", ["MASCULINO", "FEMININO"])
with coluna_nome:
    if sexo=="MASCULINO":
        nome_exemplo = "JOÃO"
    if sexo=="FEMININO":
        nome_exemplo = "MARIA"

    nome = st.text_input("Nome:", nome_exemplo)
with coluna_doenca:
    doenca = st.selectbox("Situação:", ["SEM DOENÇA - de 0 a 2 anos"])

st.write("Idade:")
coluna_idade_anos, coluna_idade_meses, _ = st.columns([2, 2, 4])
with coluna_idade_anos:
    idade_em_anos = st.number_input("Anos completos:", step=1, min_value=0, max_value=20)

with coluna_idade_meses:
    idade_em_meses = st.number_input("Meses completos:", step=1, min_value=0, max_value=11)

coluna_tabalhar_com, coluna_peso_altura, _ = st.columns([2, 2, 4])

with coluna_tabalhar_com:
    trabalhar_com = st.radio("Trabalhar com", ["Peso", "Altura"])

if trabalhar_com == "Peso":
    with coluna_peso_altura:
        peso_em_kg = st.number_input("Peso (em Kg)", step=1, min_value=0, max_value=100)

if trabalhar_com == "Altura":
    with coluna_peso_altura:
        altura_em_cm = st.number_input("Altura (em Cm)", step=1, min_value=0, max_value=200)

if st.button("Consultar"):
    if trabalhar_com == "Peso":
        classificacao, figura = classificar_e_plotar(sexo, idade_em_meses=(idade_em_anos*12)+idade_em_meses, peso_em_kg=peso_em_kg)
        
    if trabalhar_com == "Altura":
        classificacao, figura = classificar_e_plotar(sexo, idade_em_meses=(idade_em_anos*12)+idade_em_meses, altura_em_cm=altura_em_cm)
        
    st.write(f'# Gráfico de {nome}')
    st.write(f"### Classificação: {classificacao}")
    st.plotly_chart(figura)
