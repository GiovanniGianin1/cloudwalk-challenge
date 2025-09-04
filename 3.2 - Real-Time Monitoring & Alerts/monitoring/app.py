from flask import Flask, request, jsonify
import pandas as pd
from model import AnomalyDetector
from utils import load_transactions, aggregate_by_minute

app = Flask(__name__)

detector = AnomalyDetector()
df = load_transactions('data/transactions.csv')
grouped = aggregate_by_minute(df)
detector.fit(grouped)

@app.route('/monitor', methods=['POST'])
def monitor():
    data = request.get_json()
    df = pd.DataFrame(data)
    grouped = aggregate_by_minute(df)
    anomalies = detector.predict(grouped)
    alert_flag = 'alert' if not anomalies.empty else 'ok'
    return jsonify({'status': 'processed', 'alert': alert_flag})

@app.route('/train', methods=['POST'])
def train_model():
    data = request.get_json()
    df = pd.DataFrame(data)
    grouped = aggregate_by_minute(df)
    detector.fit(grouped)
    return jsonify({'status': 'model trained'})

if __name__ == '__main__':
    app.run(debug=True)