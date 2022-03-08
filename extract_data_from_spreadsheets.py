import pandas as pd

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    #print(mes)
    tabela_vendas = pd.read_excel(f'files/{mes}.xlsx')
    #print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        valor_vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} o vendedor {vendedor} vendeu o valor de {valor_vendas} e bateu a meta!')
