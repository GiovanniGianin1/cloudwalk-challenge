from flask import Flask, request, jsonify
import pandas as pd
from model import detect_anomaly

app = Flask(__name__)

@app.route('/monitor', methods=['POST'])
def monitor():
    data = request.get_json()
    df = pd.DataFrame(data)

    # Agrupa por status
    grouped = df.groupby('status')['count'].sum().to_dict()

    # Detecta anomalias
    result = detect_anomaly(grouped)

    return jsonify({
        'status': 'processed',
        'alerts': result
    })

if __name__ == '__main__':
    app.run(debug=True)