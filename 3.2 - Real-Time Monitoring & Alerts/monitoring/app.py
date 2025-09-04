from flask import Flask, request, jsonify
import pandas as pd
from model import AnomalyDetector
from utils import aggregate_by_minute

app = Flask(__name__)
detector = AnomalyDetector()

@app.route('/train', methods=['POST'])
def train_model():
    data = request.get_json()
    df = pd.DataFrame(data)
    grouped = aggregate_by_minute(df)
    detector.fit(grouped)
    return jsonify({'status': 'model trained'})

@app.route('/monitor', methods=['POST'])
def monitor():
    data = request.get_json()
    df = pd.DataFrame(data)
    grouped = aggregate_by_minute(df)
    anomalies = detector.predict(grouped)
    alert_flag = 'alert' if not anomalies.empty else 'ok'
    return jsonify({'status': 'processed', 'alert': alert_flag})
    
if __name__ == '__main__':
    app.run(debug=True)