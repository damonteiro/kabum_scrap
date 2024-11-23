import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sqlalchemy import create_engine

# Criar o banco de dados SQLite
engine = create_engine('sqlite:///banco.db', echo=True)

# Criar um DataFrame com os dados (se necessário, ajuste ou carregue de outra fonte)
data = {
    "percent": [5,10,5,10,7,30,10,4,10,5,5,10,10],
    "oferta": ["Em itens selecionados",
        "Em sua 1ª compra no kabum!",
        "Em itens selecionados",
        "Para sua compra no app kabum!",
        "Em itens samsung",
        "Em ssd lexar",
        "Em mochilas",
        "Em itens lenovo",
        "Soundbar lg s40t, bluetooth 5.3",
        "Em produtos lg",
        "Para itens selecionados",
        "Projetor lg cinebeam smart laser",
        "Em notebooks"],
    
    "link": [
        "www.kabum.com.br/promocao/TOPDOKABUM2024",
        "www.kabum.com.br/",
        "www.kabum.com.br/promocao/5OFFMAGALU",
        "www.kabum.com.br/Promocao/APPNINJA",
        "www.kabum.com.br/promocao/SAMSUNG7",
        "www.kabum.com.br/promocao/LEXAR30OFF",
        "www.kabum.com.br/moda/bolsas-e-mochilas",
        "www.kabum.com.br/promocao/NOTELENOVONOV",
        "www.kabum.com.br/produto/615556/soundbar-lg-s40t-bluetooth-5-3-300w-subwoofer-2-1-canais-preto",
        "www.kabum.com.br/promocao/LG5OFFNOV",
        "www.kabum.com.br/promocao/CONECTA5",
        "www.kabum.com.br/produto/544042/projetor-lg-cinebeam-smart-laser-3840-x-2160-4k-uhd-2700-lumens-with-300-graus-hu810pw",
        "www.kabum.com.br/promocao/NOTE3PNOV"],
    
    "cupom": ["TOPDOKABUM",
        "TONOKABUM",
        "TOP5HOJE",
        "APPNINJA",
        "SAMSUNG7",
        "LEXAR30",
        "MOCHILA10",
        "LENOVO",
        "LG10",
        "LG5",
        "CONECTA5",
        "PROJETOR10",
        "SALDAO10"],
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
    media = df_lido['percent'].mean()
    st.sidebar.header("Estatísticas:")
    st.sidebar.write(f"Média: {media:.2f}")
elif estatistica_escolhida == 'Mediana':
    mediana = df_lido['percent'].median()
    st.sidebar.header("Estatísticas:")
    st.sidebar.write(f"Mediana: {mediana:.2f}")
elif estatistica_escolhida == 'DP':
    desvio_padrao = df_lido['percent'].std()
    st.sidebar.header("Estatísticas:")
    st.sidebar.write(f"Desvio Padrão: {desvio_padrao:.2f}")

# Gráficos
graficos = ['univariada', 'multivariada']
st.sidebar.header('Gráficos:')
tipo_grafico = st.sidebar.selectbox('Selecione um tipo de análise gráfica', graficos)

st.subheader("Gráficos e Visualizações")

if tipo_grafico == 'univariada':
    expander1 = st.expander('Sessão Gráficos Univariados')

    with expander1:
        fig, axs = plt.subplots(3, 1, figsize=(10, 10))

        # Primeiro gráfico: Histograma
        axs[0].hist(df_lido['percent'], bins=10, color='blue', alpha=0.7)
        axs[0].set_title("Histograma de Percentuais de Desconto")

        # Segundo gráfico: Percentuais Ordenados
        axs[1].plot(sorted(df_lido['percent']), marker='o')
        axs[1].set_title("Percentuais Ordenados")

        # Terceiro gráfico: Boxplot
        Q1 = np.percentile(df_lido['percent'], 25)
        Q3 = np.percentile(df_lido['percent'], 75)
        I = Q3 - Q1
        max_outlier = Q3 + 1.5 * I
        min_outlier = Q1 - 1.5 * I
        outliers = df_lido[(df_lido['percent'] > max_outlier) | (df_lido['percent'] < min_outlier)]

        sns.boxplot(x=df_lido['percent'], ax=axs[2])
        axs[2].set_title("Boxplot de Percentuais de Desconto")

        # Exibindo no Streamlit
        st.pyplot(fig)

        if not outliers.empty:
            st.write("Outliers detectados:")
            st.write(outliers)
        else:
            st.write("Nenhum outlier detectado.")

elif tipo_grafico == 'multivariada':
    expander2 = st.expander('Sessão Gráficos Multivariados')

    with expander2:
        fig2, ax2 = plt.subplots(figsize=(10, 6))

        # Gráfico de dispersão
        sns.scatterplot(
            x=df_lido['percent'],
            y=df_lido.index,  # Utilizando o índice como um eixo para representar as ofertas
            hue=df_lido['oferta'],
            palette="viridis",
            s=100,  # Tamanho dos pontos
            ax=ax2
        )

        ax2.set_title("Relação dos Percentuais de Desconto com Ofertas")
        ax2.set_xlabel("Percentual de Desconto")
        ax2.set_ylabel("Índice das Ofertas")
        ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

        st.pyplot(fig2)
        st.write("Gráfico de dispersão mostrando os percentuais de desconto por oferta.")
