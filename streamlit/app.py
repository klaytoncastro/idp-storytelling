import streamlit as st
import plotly.express as px

# Título do aplicativo
st.title("Meu Aplicativo Streamlit")

# Criar uma estrutura de duas colunas
col1, col2 = st.columns(2)

# No primeiro bloco de coluna
with col1:
    st.header("Gráfico de Pizza")
    st.write("Esta é a primeira coluna com um gráfico de pizza.")
    
    # Dados para o gráfico de pizza
    data = {'Categorias': ['Maçãs', 'Bananas', 'Laranjas'], 'Valores': [30, 45, 25]}
    df = pd.DataFrame(data)
    
    # Criar um gráfico de pizza com o Plotly
    fig_pie = px.pie(df, values='Valores', names='Categorias')
    st.plotly_chart(fig_pie)

# No segundo bloco de coluna
with col2:
    st.header("Gráfico de Barras")
    st.write("Esta é a segunda coluna com um gráfico de barras.")
    
    # Dados para o gráfico de barras
    categories = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D']
    values = [10, 30, 20, 25]
    fig_bar = px.bar(x=categories, y=values)
    st.plotly_chart(fig_bar)

# Adicionar Markdown na seção 3
st.header("Seção 3")
markdown_text = """
Este é um exemplo de conteúdo em Markdown.

- Você pode **enfatizar** palavras ou criar listas como esta.
- Também é possível incluir links: [Google](https://www.google.com/).
- Ou até mesmo imagens:
![Streamlit](https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png)
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
