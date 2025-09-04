import requests
import json
from datetime import datetime
import random

# URL do seu servidor Flask
URL = "http://127.0.0.1:5000/monitor"

# Status disponíveis para simulação
status_types = ["approved", "denied", "refunded", "backend_reversed", "failed", "reversed"]

# Função para gerar uma transação aleatória
def generate_transaction(timestamp):
    return [
        {
            "timestamp": timestamp,
            "status": status,
            "count": random.randint(0, 5) if status != "approved" else random.randint(100, 130)
        }
        for status in status_types
    ]

# Função para enviar e registrar o resultado
def send_test():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = generate_transaction(timestamp)

    try:
        response = requests.post(URL, json=payload)
        result = response.json()
        print(f"[{timestamp}] → Alert: {result['alert']}")
        
        # Salva em log
        with open("alert_log.txt", "a") as f:
            f.write(f"{timestamp} | Alert: {result['alert']} | Payload: {json.dumps(payload)}\n")

    except Exception as e:
        print(f"❌ Error: {e}")

# Executa o teste
if __name__ == "__main__":
    send_test()