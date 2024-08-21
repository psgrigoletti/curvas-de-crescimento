import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import numpy as np

def gerar_curva_crescimento_altura(sexo, idade_em_anos, altura_em_cm):
    # Simulação de dados de percentis (exemplo aproximado)
    idades = np.arange(0, 20, 1)  # Idades de 0 a 19 anos
    
    if sexo.upper() == "MASCULINO":
        altura_p3 = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140]
        altura_p50 = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
        altura_p97 = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]
    elif sexo.upper() == "FEMININO":
        altura_p3 = [44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99, 104, 109, 114, 119, 124, 129, 134, 139]
        altura_p50 = [48, 53, 58, 63, 68, 73, 78, 83, 88, 93, 98, 103, 108, 113, 118, 123, 128, 133, 138, 143]
        altura_p97 = [52, 57, 62, 67, 72, 77, 82, 87, 92, 97, 102, 107, 112, 117, 122, 127, 132, 137, 142, 147]
    else:
        raise ValueError("Sexo deve ser 'MASCULINO' ou 'FEMININO'.")

    # Criando o gráfico da curva de crescimento
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=idades, y=altura_p3, mode='lines', name='Altura P3', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=idades, y=altura_p50, mode='lines', name='Altura P50'))
    fig.add_trace(go.Scatter(x=idades, y=altura_p97, mode='lines', name='Altura P97', line=dict(dash='dash')))

    # Ponto do usuário
    fig.add_trace(go.Scatter(x=[idade_em_anos], y=[altura_em_cm], mode='markers', name='Altura da Criança',
                             marker=dict(size=10, color='red')))

    # Customizando o layout do gráfico
    fig.update_layout(title=f'Curva de Crescimento - Idade x Altura ({sexo.capitalize()})',
                      xaxis_title='Idade (anos)',
                      yaxis_title='Altura (cm)')

    # Determinando o percentil
    percentil = "Desconhecido"
    if altura_em_cm < altura_p3[idade_em_anos]:
        percentil = "< P3"
    elif altura_em_cm == altura_p3[idade_em_anos]:
        percentil = "P3"
    elif altura_p3[idade_em_anos] < altura_em_cm < altura_p50[idade_em_anos]:
        percentil = "Entre P3 e P50"
    elif altura_em_cm == altura_p50[idade_em_anos]:
        percentil = "P50"
    elif altura_p50[idade_em_anos] < altura_em_cm < altura_p97[idade_em_anos]:
        percentil = "Entre P50 e P97"
    elif altura_em_cm == altura_p97[idade_em_anos]:
        percentil = "P97"
    elif altura_em_cm > altura_p97[idade_em_anos]:
        percentil = "> P97"

    return fig, percentil

def gerar_curva_crescimento_peso(sexo, idade_em_anos, peso_em_kg):
    # Simulação de dados de percentis (exemplo aproximado)
    idades = np.arange(0, 20, 1)  # Idades de 0 a 19 anos
    
    if sexo.upper() == "MASCULINO":
        peso_p3 = [2.5, 3.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0]
        peso_p50 = [3.2, 4.5, 6.0, 7.0, 8.5, 10.0, 11.5, 13.0, 14.5, 16.0, 17.5, 19.0, 20.5, 22.0, 23.5, 25.0, 26.5, 28.0, 29.5, 31.0]
        peso_p97 = [4.0, 5.5, 7.5, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0, 25.0, 27.0, 29.0, 31.0, 33.0, 35.0, 37.0, 39.0, 41.0]
    elif sexo.upper() == "FEMININO":
        peso_p3 = [2.4, 3.4, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8, 10.8, 11.8, 12.8, 13.8, 14.8, 15.8, 16.8, 17.8, 18.8, 19.8, 20.8, 21.8]
        peso_p50 = [3.0, 4.3, 5.7, 6.7, 8.0, 9.3, 10.6, 11.9, 13.2, 14.5, 15.8, 17.1, 18.4, 19.7, 21.0, 22.3, 23.6, 24.9, 26.2, 27.5]
        peso_p97 = [3.9, 5.3, 6.8, 7.8, 9.5, 11.2, 12.9, 14.6, 16.3, 18.0, 19.7, 21.4, 23.1, 24.8, 26.5, 28.2, 29.9, 31.6, 33.3, 35.0]
    else:
        raise ValueError("Sexo deve ser 'MASCULINO' ou 'FEMININO'.")

    # Criando o gráfico da curva de crescimento
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=idades, y=peso_p3, mode='lines', name='Peso P3', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=idades, y=peso_p50, mode='lines', name='Peso P50'))
    fig.add_trace(go.Scatter(x=idades, y=peso_p97, mode='lines', name='Peso P97', line=dict(dash='dash')))

    # Ponto do usuário
    fig.add_trace(go.Scatter(x=[idade_em_anos], y=[peso_em_kg], mode='markers', name='Peso da Criança',
                             marker=dict(size=10, color='red')))

    # Customizando o layout do gráfico
    fig.update_layout(title=f'Curva de Crescimento - Idade x Peso ({sexo.capitalize()})',
                      xaxis_title='Idade (anos)',
                      yaxis_title='Peso (kg)')

    # Determinando o percentil
    percentil = "Desconhecido"
    if peso_em_kg < peso_p3[idade_em_anos]:
        percentil = "< P3"
    elif peso_em_kg == peso_p3[idade_em_anos]:
        percentil = "P3"
    elif peso_p3[idade_em_anos] < peso_em_kg < peso_p50[idade_em_anos]:
        percentil = "Entre P3 e P50"
    elif peso_em_kg == peso_p50[idade_em_anos]:
        percentil = "P50"
    elif peso_p50[idade_em_anos] < peso_em_kg < peso_p97[idade_em_anos]:
        percentil = "Entre P50 e P97"
    elif peso_em_kg == peso_p97[idade_em_anos]:
        percentil = "P97"
    elif peso_em_kg > peso_p97[idade_em_anos]:
        percentil = "> P97"

    return fig, percentil

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
    doenca = st.selectbox("Doença:", ["SEM DOENÇA"])

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
        figura, classificacao = gerar_curva_crescimento_peso(sexo, idade_em_anos, peso_em_kg)
        
    if trabalhar_com == "Altura":
        figura, classificacao = st.plotly_chart(gerar_curva_crescimento_altura(sexo, idade_em_anos, altura_em_cm))

    st.write(f'# Gráfico de {nome}')
    st.write(f"### Classificação: {classificacao}")
    st.plotly_chart(figura)
