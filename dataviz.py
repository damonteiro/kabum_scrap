import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

api_url = "127.0.0.1:5000"

response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    metrics = data['metrics']
    dados_gerais = pd.DataFrame(data['data'])
    descontos = dados_gerais['% Desconto']
else:
    st.error("Erro ao conectar à API")
    st.stop()
    

tipos_analise = [None,'Média','Mediana','DP']

st.sidebar.header('Tipo de análise estatística:')
estatisca_escolhida = st.sidebar.selectbox('Selecione o tipo de análise', tipos_analise)

if estatisca_escolhida == None:
    pass
elif estatisca_escolhida =='Média':
    st.sidebar.header("Estatísticas:")
    st.sidebar.write(f"Média: {metrics['mean']:.2f}")
elif estatisca_escolhida =='Mediana':
    st.sidebar.header("Estatísticas:")
    st.sidebar.write(f"Mediana: {metrics['median']:.2f}")
else:
    st.sidebar.header("Estatísticas:")
    st.sidebar.write(f"Desvio Padrão: {metrics['std_dev']:.2f}")
    

graficos = ['univariada','multivariada']

st.sidebar.header('Gráficos:')
tipo_grafico = st.sidebar.selectbox('Selecione um tipo de análise gráfica',graficos)

st.subheader("Gráficos e Visualizações")

if tipo_grafico == 'univariada':

    expander1 = st.expander('Sessão Gráficos Univariados')

    with expander1:
        fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Primeiro gráfico
        axs[0].hist(descontos, bins=10, color='blue', alpha=0.7)
        axs[0].set_title("Histograma de Descontos")

# Segundo gráfico
        axs[1].plot(sorted(descontos), marker='o')
        axs[1].set_title("Descontos Ordenados")

#terceiro gráfico

        Q1 = np.percentile(descontos, 25)
        Q3 = np.percentile(descontos, 75)
        I = Q3 - Q1
        max = Q3 + 1.5 * I
        min = Q1 - 1.5 * I
        outlier = []
        mediana = np.median(descontos)

        for i in range(len(descontos)):
            if descontos[i] > max or descontos[i]<min:
                outlier.append(descontos[i])

        sns.boxplot(x=descontos, ax=axs[2])
        axs[2].set_title("Boxplot de Descontos")

# Exibindo no Streamlit
        st.pyplot(fig)

        if len(outlier)>0:
            for i in outlier:
                st.write(f'outliers: {i}')
        else:
            st.write('Nenhum outlier detectado')

elif tipo_grafico =='multivariada':
    expander2 = st.expander('Sessão Gráficos Multivariados')

    with expander2:
        fig2,ax2 = plt.subplots(figsize=(10,6))

        sns.scatterplot(
            x=descontos,  # Usa a variável 'descontos' diretamente para o eixo X
            y=dados_gerais['Cupom'],  # Índices do DataFrame para o eixo Y
            hue=dados_gerais['Oferta'],  # Diferencia os pontos pela coluna 'Cupom'
            palette="viridis", 
            s=100, # Tamanho dos pontos
            ax=ax2
        )

        ax2.set_title("Relação da media de Desconto por Desconto")
        ax2.set_xlabel("% Desconto")
        ax2.set_ylabel("Oferta (Índice)")
        ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

        st.pyplot(fig2)
        st.write('Pela falta de dados comparativos númericos, não foi possível criar um gráfico de disperção ideal.')
