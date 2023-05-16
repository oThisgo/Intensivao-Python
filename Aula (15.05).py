#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pyautogui
import time
import pandas
import pyperclip

pyautogui.hotkey("ctrl","t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=921, y=354)
pyautogui.write("oThisgo")
pyautogui.click(x=930, y=413)
pyautogui.write("t17s01d05")
pyautogui.click(x=997, y=483)
time.sleep(5)
pyautogui.click(x=1707, y=309)


# In[34]:


tabela = pandas.read_csv(r"C:\Users\thiag\Downloads\Compras.csv", sep=";")
display(tabela)


# In[35]:


valor_total = tabela["ValorFinal"].sum()
quantidade_total = tabela["Quantidade"].sum()
valor_medio = valor_total / quantidade_total
print("Valor total:", valor_total)
print("Quantidade total:", quantidade_total)
print("valor médio:", valor_medio)


# In[46]:


pyautogui.hotkey("ctrl","t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")
time.sleep(5)

assunto = "Relatórios"
texto = f"""
Olá, Estes são os relatórios:

Quantidade de vendas: {quantidade_total}
Valor médio: {valor_medio:.2f}
Valor total: {valor_total:.2f}"""

pyautogui.click(x=129, y=177)
time.sleep(3)
pyautogui.write("thiagosds1701@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")


# In[ ]:





# In[ ]:




