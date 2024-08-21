import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import numpy as np

# Função para gerar a curva de crescimento
def gerar_curva_crescimento(sexo, idade, altura, peso):
    # Simulando dados de percentis da OMS (exemplo, você pode usar dados reais)
    idades = np.arange(0, 20, 1)  # Idades de 0 a 19 anos
    
    if sexo.upper() == "MASCULINO":
        altura_media = np.array([50 + i*5 for i in range(20)])  # Altura média simulada
        peso_medio = np.array([3 + i*2 for i in range(20)])  # Peso médio simulado
    elif sexo.upper() == "FEMININO":
        altura_media = np.array([48 + i*4.8 for i in range(20)])  # Altura média simulada
        peso_medio = np.array([2.8 + i*1.8 for i in range(20)])  # Peso médio simulado
    else:
        raise ValueError("Sexo deve ser 'MASCULINO' ou 'FEMININO'.")

    # Criando o gráfico da curva de crescimento
    fig = go.Figure()

    # Curva de altura
    fig.add_trace(go.Scatter(x=idades, y=altura_media, mode='lines', name='Altura Média'))

    # Curva de peso
    fig.add_trace(go.Scatter(x=idades, y=peso_medio, mode='lines', name='Peso Médio'))

    # Ponto do usuário
    fig.add_trace(go.Scatter(x=[idade], y=[altura], mode='markers', name='Altura do Usuário',
                             marker=dict(size=10, color='red')))
    fig.add_trace(go.Scatter(x=[idade], y=[peso], mode='markers', name='Peso do Usuário',
                             marker=dict(size=10, color='blue')))

    # Customizando o layout do gráfico
    fig.update_layout(title=f'Curva de Crescimento ({sexo.capitalize()})',
                      xaxis_title='Idade (anos)',
                      yaxis_title='Altura / Peso',
                      yaxis=dict(title='Altura (cm) / Peso (kg)', overlaying='y', side='left'),
                      legend_title="Parâmetros",
                      hovermode="x")

    # Exibindo o gráfico
    return fig

st.title('Consultar curvas de crescimento')

doenca = st.selectbox("Doença", ["Sem doença"])
sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])
idade_em_anos = st.number_input("Idade em anos", step=1)
peso_em_kg = st.number_input("Peso em Kg")
altura_em_cm = st.number_input("Altura em Cm")
if st.button("Consultar"):
    st.plotly_chart(gerar_curva_crescimento(sexo, idade_em_anos, altura_em_cm, peso_em_kg))