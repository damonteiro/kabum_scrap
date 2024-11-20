import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask
import time


navegador = webdriver.Chrome()
navegador.get('https://www.kabum.com.br')
navegador.find_element(By.XPATH, '//*[@id="cuponsMenuSuperior"]').click()

time.sleep(5)
percentDesc = []
for i in range(1,14):
    try:
        percentDesc.append(navegador.find_element(By.XPATH, f'//*[@id="cupons-ativos"]/div[{i}]/div/div[2]/p[1]').text)
    except:                                                 
        pass
    
tipoDesc = []
for b in range(1,14):
    try:
        tipoDesc.append(navegador.find_element(By.XPATH, f'//*[@id="cupons-ativos"]/div[{b}]/div/div[2]/p[2]').text)
    except:
        pass

linkOferta = []
for c in range(1,14):
    try:
        elemento = navegador.find_element(By.XPATH, f'//*[@id="cupons-ativos"]/div[{c}]/div/div[2]/a')
        linkOferta.append(elemento.get_attribute('href'))
    except:
        pass

cupom = []
for d in range(1,14):
    try:
        cupom.append(navegador.find_element(By.XPATH, f'//*[@id="cupons-ativos"]/div[{d}]/div/div[2]/p[3]').text)
    except:
        pass



#DataFrames de cada tabela
nomeCupom = pd.DataFrame(cupom, columns=['Cupom'])
desconto = pd.DataFrame(percentDesc, columns=['% Desconto'])
descricao = pd.DataFrame(tipoDesc, columns=['Oferta'])
link = pd.DataFrame(linkOferta, columns=['Link'])

nomeCupom.to_csv("../basesoriginais/nomeCupom.csv",index=False)
desconto.to_csv("../basesoriginais/desconto.csv",index=False)
descricao.to_csv("../basesoriginais/descricao.csv",index=False)
link.to_csv('../basesoriginais/link.csv',index=False)



