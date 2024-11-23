import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sqlalchemy import create_engine

# Criar o banco de dados SQLite
engine = create_engine('sqlite:///banco.db', echo=True)

# Dados fictícios de preços de notebooks
data = {
    "notebook": [
        "Dell XPS 13 9310", "Apple MacBook Air M2 256GB", "Lenovo ThinkPad X1 Carbon 9ª Geração",
        "Acer Aspire 5", "HP Pavilion 15", "Samsung Galaxy Book 2 Pro 15", "Asus VivoBook 15",
        "MSI GF63 Thin 11SC-212XBR", "LG Gram 14", "Microsoft Surface Laptop 4", 
        "Lenovo IdeaPad 3 15", "Dell Inspiron 15 3000"
    ],
    "preco": [
        7599.00, 10999.00, 8999.00, 3399.00, 4299.00, 5499.00, 3699.00, 6599.00, 6999.00, 7799.00,
        2799.00, 3299.00
    ],
    # Adicionando tamanho de tela fictício
    "tamanho_tela": [
        13.3, 13.3, 14.0, 15.6, 15.6, 15.6, 15.6, 15.6, 14.0, 13.5, 15.6, 15.6
    ]
}

df = pd.DataFrame(data)

# Salvando os dados no banco de dados SQLite
df.to_sql('dados', con=engine, if_exists='replace', index=False)

# Lendo os dados do banco
df_lido = pd.read_sql('SELECT * FROM dados', con=engine)

# Opções para análise estatística
tipos_analise = [None, 'Média', 'Mediana', 'DP']
st.sidebar.header('Tipo de análise estatística:')
estatistica_escolhida = st.sidebar.selectbox('Selecione o tipo de análise', tipos_analise)

# Calcular estatísticas básicas
if estatistica_escolhida == 'Média':
    media = df_lido['preco'].mean()
    st.sidebar.header("Estatísticas:")
    st.sidebar.write(f"Média: R$ {media:.2f}")
elif estatistica_escolhida == 'Mediana':
    mediana = df_lido['preco'].median()
    st.sidebar.header("Estatísticas:")
    st.sidebar.write(f"Mediana: R$ {mediana:.2f}")
elif estatistica_escolhida == 'DP':
    desvio_padrao = df_lido['preco'].std()
    st.sidebar.header("Estatísticas:")
    st.sidebar.write(f"Desvio Padrão: R$ {desvio_padrao:.2f}")

# Gráficos
graficos = ['univariada', 'multivariada']
st.sidebar.header('Gráficos:')
tipo_grafico = st.sidebar.selectbox('Selecione um tipo de análise gráfica', graficos)

st.subheader("Gráficos e Visualizações")

# Gráficos Univariados
if tipo_grafico == 'univariada':
    expander1 = st.expander('Sessão Gráficos Univariados')

    with expander1:
        fig, axs = plt.subplots(2, 2, figsize=(12, 12))  # Organizando em 2x2 (2 em cima e 2 embaixo)

        # Primeiro gráfico: Histograma
        axs[0, 0].hist(df_lido['preco'], bins=10, color='blue', alpha=0.7)
        axs[0, 0].set_title("Histograma de Preços de Notebooks", fontsize=16)
        axs[0, 0].set_xlabel("Preço (R$)", fontsize=14)
        axs[0, 0].set_ylabel("Frequência", fontsize=14)

        # Segundo gráfico: Boxplot
        sns.boxplot(x=df_lido['preco'], ax=axs[0, 1], linewidth=2)
        axs[0, 1].set_title("Boxplot de Preços de Notebooks", fontsize=16)

        # Terceiro gráfico: Contagem de Notebooks
        preço_por_notebook = df_lido.groupby('notebook')['preco'].sum()  # Agrupando e somando os preços
        axs[1, 0].bar(preço_por_notebook.index, preço_por_notebook.values, color='green', linewidth=2, edgecolor='black')
        axs[1, 0].set_title("Soma dos Preços por Notebook", fontsize=16)
        axs[1, 0].set_xlabel("Nome do Notebook", fontsize=14)
        axs[1, 0].set_ylabel("Preço Total (R$)", fontsize=14)
        axs[1, 0].tick_params(axis='x', rotation=45)  # Inclina os rótulos para facilitar leitura

        # Quarto gráfico: Gráfico de Pizza (distribuição de preços)
        preço_por_notebook = df_lido.groupby('notebook')['preco'].sum()
        axs[1, 1].pie(preço_por_notebook, labels=preço_por_notebook.index, autopct='%1.1f%%', startangle=90)
        axs[1, 1].set_title("Distribuição Percentual dos Preços dos Notebooks", fontsize=16)

        # Exibindo no Streamlit
        st.pyplot(fig)

# Gráficos Multivariados
elif tipo_grafico == 'multivariada':
    expander2 = st.expander('Sessão Gráficos Multivariados')

    with expander2:
        fig2, axs2 = plt.subplots(2, 2, figsize=(15, 12))

        # Gráfico de Dispersão
        sns.scatterplot(
            x=df_lido['preco'],  # Preço no eixo X
            y=df_lido['tamanho_tela'],  # Tamanho da tela no eixo Y
            hue=df_lido['notebook'],  # Diferenciação por nome do notebook
            palette="viridis",  # Paleta de cores
            s=100,  # Tamanho dos pontos
            ax=axs2[0, 0]
        )
        axs2[0, 0].set_title("Relação entre Preço e Tamanho da Tela", fontsize=16)

        # Gráfico de Boxplot (Preço por Notebook)
        sns.boxplot(x='notebook', y='preco', data=df_lido, ax=axs2[0, 1])
        axs2[0, 1].set_title("Preço por Notebook", fontsize=16)

        # Gráfico de Barras (Preço médio por Notebook)
        preço_medio_por_notebook = df_lido.groupby('notebook')['preco'].mean()
        sns.barplot(x=preço_medio_por_notebook.index, y=preço_medio_por_notebook.values, ax=axs2[1, 0])
        axs2[1, 0].set_title("Preço Médio por Notebook", fontsize=16)

        # Gráfico de Histograma (Preço por Notebook)
        sns.histplot(df_lido['preco'], kde=True, color='purple', ax=axs2[1, 1])
        axs2[1, 1].set_title("Histograma dos Preços", fontsize=16)

        # Exibindo no Streamlit
        st.pyplot(fig2)
        st.write("Gráficos multivariados: relação entre preço, tamanho da tela e diferentes notebooks.")
