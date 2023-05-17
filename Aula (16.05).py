#!/usr/bin/env python
# coding: utf-8

# In[86]:


import pandas as pd
import plotly.express as px

tabela = pd.read_csv(r"C:\Intensivão python\Aula 2\clientes.csv", encoding = "latin", sep=";").drop("Unnamed: 8", axis=1).dropna()
tabela ["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")


# In[87]:


display(tabela)
display(tabela.info())
display(tabela.describe())


# In[88]:


for coluna in tabela.columns:
    graph = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    graph.show()

