import pandas as pd

df = pd.read_csv('data/transactions.csv')

df.to_json('data/transactions.json', orient='records', lines=False)

print("Arquivo JSON gerado com sucesso!")