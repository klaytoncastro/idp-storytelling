import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Título do aplicativo
st.title("Meu Primeiro Aplicativo Streamlit")

# Criar uma estrutura de duas colunas
col1, col2 = st.columns(2)

# No primeiro bloco de coluna
with col1:
    st.header("Gráfico de Pizza")
    st.write("Esta é a primeira coluna com um gráfico de pizza.")

    # Dados para o gráfico de pizza
    labels = ['Maçãs', 'Bananas', 'Laranjas']
    sizes = [30, 45, 25]
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

    # Configurar aspect ratio para tornar o gráfico de pizza circular
    ax_pie.set_aspect('equal')

    st.pyplot(fig_pie)

# No segundo bloco de coluna
with col2:
    st.header("Gráfico de Barras")
    st.write("Esta é a segunda coluna com um gráfico de barras.")

    # Dados para o gráfico de barras
    categories = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D']
    values = [10, 30, 20, 25]
    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(categories, values)
    st.pyplot(fig_bar)

# Adicionar Markdown
st.header("Trecho em Markdown")
markdown_text = """
Este é um exemplo de conteúdo em Markdown. Você pode formatar títulos de seções conforme abaixo:

# Título Grande
## Título Médio
### Subtítulo

- Você também pode **enfatizar** palavras, colocá-las em *itálico* ou criar listas como esta.
- É possível incluir links: [Google](https://www.google.com/).
- Ou, ainda, imagens: ![Logo](https://images.ecency.com/p/C3TZR1g81UNbFzApDTmvFatkwuDREJFVGiTUu9JN1JupzFWrWjCXzkxpcAdZdG64uv1GM5m4qvUwx3T2geEoHyBfmXu3UFwEcgv3E5vfT8n9be5bvsUik4N?format=match&mode=fit&width=200&height=100)
"""

st.markdown(markdown_text)

# Adicionar widgets e conteúdo à barra lateral
st.sidebar.header("Barra Lateral")

# Adicionar um widget de caixa de seleção à barra lateral
option_sidebar = st.sidebar.selectbox("Selecione uma opção na Barra Lateral", ["Opção A", "Opção B", "Opção C"])

# Adicionar um botão à barra lateral
if st.sidebar.button("Clique na Barra Lateral"):
    st.sidebar.write("Botão clicado na Barra Lateral!")

# Adicionar um slider à barra lateral
slider_value = st.sidebar.slider("Selecione um valor na Barra Lateral", 0, 100, 50)

# Adicionar um gráfico à barra lateral
st.sidebar.line_chart({"data": [1, 2, 3, 4, 5]})
