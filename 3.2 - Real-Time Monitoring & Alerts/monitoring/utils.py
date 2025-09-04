import pandas as pd

def load_transactions(path='data/transactions.csv'):
    df = pd.read_csv(path, parse_dates=['timestamp'])
    return df

def aggregate_by_minute(df):
    grouped = df.groupby(['timestamp', 'status'])['count'].sum().unstack(fill_value=0)
    return grouped.reset_index()