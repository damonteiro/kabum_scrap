import pandas as pd

desconto = pd.read_csv('../basesoriginais/desconto.csv')
descricao = pd.read_csv('../basesoriginais/descricao.csv')
nomeCupom= pd.read_csv('../basesoriginais/nomeCupom.csv')
link = pd.read_csv('../basesoriginais/link.csv')

desconto['% Desconto'] = desconto['% Desconto'].str.replace('OFF', '').str.replace('%', '')
#Consertando letras minúsculas
df = pd.DataFrame({'Oferta': descricao['Oferta']})
df['Oferta'] = df['Oferta'].str.capitalize()
link['Link'] = link['Link'].str.replace('https://', '', regex=False)
#Juntando e limpando as tabelas
itens3 = pd.concat([desconto,df,link,nomeCupom], axis=1)
itens3.fillna(-9, inplace=True)
itens = itens3.drop_duplicates()


#Salvando em csv
itens.to_csv("../basestratadas/TabelaPrecos.csv",index=False)
