from sklearn.ensemble import IsolationForest
import pandas as pd

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05, random_state=42)
        self.fitted = False
        self.status_columns = []

    def fit(self, df):
        # Detecta todos os status únicos
        self.status_columns = [col for col in df.columns if col != 'timestamp']
        
        # Preenche colunas ausentes com 0
        for col in self.status_columns:
            if col not in df.columns:
                df[col] = 0

        df_filtered = df[self.status_columns].fillna(0)
        self.model.fit(df_filtered)
        self.fitted = True

    def predict(self, df_minute):
        if not self.fitted:
            raise ValueError("Model not trained. Call fit() first.")

        # Garante que todas as colunas estejam presentes
        for col in self.status_columns:
            if col not in df_minute.columns:
                df_minute[col] = 0

        df_filtered = df_minute[self.status_columns].fillna(0)
        scores = self.model.predict(df_filtered)
        df_minute['anomaly'] = scores
        return df_minute[df_minute['anomaly'] == -1]