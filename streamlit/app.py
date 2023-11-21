import streamlit as st

# Título do aplicativo
st.title("Aplicativo Streamlit com Colunas e Barra Lateral")

# Criar uma estrutura de duas colunas
col1, col2 = st.columns(2)

# No primeiro bloco de coluna
with col1:
    st.header("Conteúdo da Coluna 1")
    st.write("Esta é a primeira coluna")

# No segundo bloco de coluna
with col2:
    st.header("Conteúdo da Coluna 2")
    st.write("Esta é a segunda coluna")

# Adicionar widgets e conteúdo à barra lateral
st.sidebar.header("Barra Lateral")

# Adicionar um widget de caixa de seleção à barra lateral
option = st.sidebar.selectbox("Selecione uma opção:", ["Opção 1", "Opção 2", "Opção 3"])

# Adicionar um botão à barra lateral
if st.sidebar.button("Clique em mim"):
    st.sidebar.write("Botão clicado!")

# Adicionar um slider à barra lateral
slider_value = st.sidebar.slider("Selecione um valor", 0, 100, 50)

# Adicionar um gráfico à barra lateral
st.sidebar.line_chart({"data": [1, 2, 3, 4, 5]})

"""

import streamlit as st

# Título do aplicativo
st.title("Meu Primeiro Aplicativo Streamlit")

# Título da seção
st.header("Seção 1")

# Texto simples
st.write("Este é um exemplo simples de um aplicativo Streamlit.")

# Adicionando um gráfico
import matplotlib.pyplot as plt
import numpy as np

# Gerando alguns dados aleatórios
data = np.random.randn(1000)

# Criando um histograma
fig, ax = plt.subplots()
ax.hist(data, bins=20)

# Exibindo o gráfico no Streamlit
st.pyplot(fig)

# Adicionando uma opção de seleção
option = st.selectbox("Selecione uma opção", ["Opção 1", "Opção 2", "Opção 3"])

# Exibindo a opção selecionada
st.write("Você selecionou:", option)

"""
