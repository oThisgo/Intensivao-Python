import pyautogui as pag
import pandas as pd
import unicodedata as ucd
from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get("https://google.com")

tabela = pd.read_excel(r"C:\Intensivão python\Aula 3\commodities.xlsx")

for linha in tabela.index:
    
    #ucd.normalize("NFKD", produto).encode("ascii", "ignore") para adaptar caracteres especiais
    
    produto = tabela.loc[linha, "Produto"]
    produto = produto.replace("ó","o").replace("ç","c").replace("ú","u").replace("é","e").replace("ã","a").replace("á","a")
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    navegador.get(link)
    
    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace(".","").replace(",",".")
    cotacao = float(cotacao)
    print(cotacao)
    
    tabela.loc[linha, "Preço Atual"] = cotacao 
    display(tabela)
    
tabela ["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]
display(tabela)

navegador.quit()
tabela.to_excel("C:\Intensivão python\Aula 3\commodities_atualizado.xlsx", index=False)