<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>
    <h1>Análise de Preços de Notebooks</h1>

<p>Este projeto visa realizar uma análise detalhada dos preços de notebooks utilizando dados fictícios. A análise é realizada com o uso de bibliotecas populares de Python, como <code>pandas</code>, <code>matplotlib</code>, <code>seaborn</code> e <code>streamlit</code>, para gerar gráficos e relatórios interativos. O objetivo é fornecer uma visão clara sobre a distribuição dos preços, comparações entre diferentes modelos e um resumo estatístico das informações.</p>

   <h2>Funcionalidades</h2>
    <p>O projeto permite ao usuário visualizar e analisar os seguintes aspectos:</p>
    <ul>
        <li><strong>Análise Univariada</strong>:
            <ul>
                <li><strong>Histograma</strong>: Exibe a distribuição dos preços dos notebooks.</li>
                <li><strong>Boxplot</strong>: Visualiza a variação dos preços e identifica possíveis outliers.</li>
                <li><strong>Gráfico de Barras</strong>: Mostra a soma total dos preços de cada modelo de notebook.</li>
                <li><strong>Gráfico de Pizza</strong>: Exibe a distribuição percentual do preço total por notebook.</li>
            </ul>
        </li>
        <li><strong>Análise Multivariada</strong>:
            <ul>
                <li><strong>Dispersão (Scatter Plot)</strong>: Relaciona o preço com o tamanho da tela de cada notebook, com distinção por marca/modelo.</li>
                <li><strong>Boxplot</strong>: Exibe os preços de cada notebook em uma distribuição comparativa.</li>
                <li><strong>Gráfico de Barras</strong>: Mostra o preço médio por notebook.</li>
                <li><strong>Histograma</strong>: Apresenta a distribuição de preços com a linha de densidade.</li>
            </ul>
        </li>
        <li><strong>Estatísticas Descritivas</strong>:
            O usuário pode optar por visualizar estatísticas básicas, como média, mediana e desvio padrão, dos preços dos notebooks.
        </li>
    </ul>

   <h2>Tecnologias Utilizadas</h2>
    <ul>
        <li><strong>Python</strong>: Linguagem principal utilizada para a análise de dados e geração de gráficos.</li>
        <li><strong>pandas</strong>: Biblioteca para manipulação de dados e análise estatística.</li>
        <li><strong>matplotlib</strong> e <strong>seaborn</strong>: Bibliotecas para visualização de dados.</li>
        <li><strong>streamlit</strong>: Ferramenta para criar dashboards interativos com Python.</li>
        <li><strong>SQLAlchemy</strong>: Para conexão e armazenamento dos dados em um banco de dados SQLite.</li>
    </ul>

   <h2>Instalação</h2>
    <p>Para instalar e rodar este projeto, siga os passos abaixo:</p>
    <ol>
        <li>Clone o repositório:
            <pre><code>git clone https://github.com/seu-usuario/projeto-preco-notebooks.git</code></pre>
        </li>
        <li>Instale as dependências:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Execute o app Streamlit:
            <pre><code>streamlit run app.py</code></pre>
        </li>
    </ol>

   <h2>Como Funciona</h2>
    <p>O projeto funciona da seguinte maneira:</p>
    <ul>
        <li><strong>Banco de Dados</strong>: O projeto utiliza um banco de dados SQLite para armazenar os dados de notebooks e preços.</li>
        <li><strong>Análises Estatísticas</strong>: Ao abrir a aplicação, o usuário pode escolher entre realizar uma análise univariada ou multivariada. Baseado na escolha, gráficos e análises estatísticas são exibidos.</li>
        <li><strong>Interface Interativa</strong>: A interface foi construída utilizando o Streamlit, que permite a interação do usuário com os dados de forma simples e rápida.</li>
    </ul>

   <h2>Exemplo de Uso</h2>
    <p>Após rodar o aplicativo, você poderá interagir com as opções na barra lateral, escolhendo o tipo de análise estatística e os gráficos que deseja visualizar. As opções de gráficos incluem histogramas, boxplots, gráficos de barras e dispersão, fornecendo uma compreensão clara sobre a distribuição e relações entre os dados dos notebooks.</p>

   <h2>Contribuições</h2>
    <p>Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou correções, sinta-se à vontade para abrir um <strong>issue</strong> ou <strong>pull request</strong>.</p>
</body>
</html>
