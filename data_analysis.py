import pandas as pd
import plotly.express as px

tabela = pd.read_csv("files/telecom_users.csv")

#Apagando uma coluna(axis=1, se forem várias passa uma lista no nome)
#ou linha (axis=0, e ao invés de passar o nome da coluna, passa o número da linha)
tabela = tabela.drop("Unnamed: 0", axis=1)

#Alterando o tipo de uma coluna e tratando erro para a mesma
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

#Excluir valores vazios
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)
#ver todas as informações da tabela, para descartar os dados nulos por exemplo
print(tabela.info())
#Quantidade
print(tabela["Churn"].value_counts())
#Percentual
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()
