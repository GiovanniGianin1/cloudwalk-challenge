import pandas as pd

# Carrega o CSV
df = pd.read_csv('data/transactions.csv')

# Converte para JSON no formato de lista de dicionários
df.to_json('data/transactions.json', orient='records', lines=False)

print("Arquivo JSON gerado com sucesso!")