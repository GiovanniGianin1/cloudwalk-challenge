# Real-Time Monitoring & Alerts

This project implements a real-time transaction monitoring system capable of detecting anomalies and triggering alerts based on transaction behavior. It uses machine learning to learn patterns from historical data and exposes an API endpoint to evaluate incoming transactions.

---

## Overview

The system receives transaction data in real time and determines whether the behavior is anomalous. It was built using Python and Flask, and trained with historical transaction data provided in CSV format.

### Key Features

- Real-time anomaly detection using Isolation Forest
- `/monitor` endpoint to evaluate incoming transactions
- Automatic model training on startup
- Dashboard with visualizations of transaction behavior and anomalies
- Simulation script to test alerts and generate logs

---

## How It Works

1. **Training**: On startup, the system loads `transactions.csv`, aggregates data per minute and status, and trains an Isolation Forest model.
2. **Monitoring**: New transactions are sent to `/monitor`. The model evaluates them and returns either:
   - `"alert"` → if the behavior is anomalous
   - `"ok"` → if the behavior is within expected patterns
3. **Visualization**: A Jupyter Notebook (`dashboard.ipynb`) shows transaction volumes and highlights anomalies.
4. **Simulation**: The script `test_monitor.py` sends randomized transactions and logs alerts to `alert_log.txt`.

---

## Project Structure

```
cloudwalk-challenge/
│
├── 3.2 - Real-Time Monitoring & Alerts/
│   ├── monitoring/
│   │   ├── data/
│   │   │   ├── transactions.csv               # Main dataset for training the alert system
│   │   │   ├── transactions.json              # JSON version of transaction data
│   │   │   ├── transactions_auth_codes.csv    # Additional transaction metadata
│   │   │
│   │   ├── app.py                  # Flask app with real-time alert endpoint
│   │   ├── convert_to_json.py      # Utility to convert CSV to JSON format
│   │   ├── dashboard.ipynb         # Dashboard with anomaly visualization
│   │   ├── model.py                # Isolation Forest model for anomaly detection
│   │   ├── test_monitor.py         # Script to simulate transactions and test alerts
│   │   ├── utils.py                # Data loading and aggregation functions
│   │
│   ├── README.md                   # Documentation for the monitoring system
│   ├── requirements.txt            # Python dependencies for running the alert system
```

---

## How to Run

### 1. Install dependencies

Make sure you have Python 3.10+ installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### 2. Start the monitoring server

Run the Flask app to start the alert system:

```bash
python app.py
```

This will automatically:
- Load `transactions.csv`
- Aggregate data by minute and status
- Train the Isolation Forest model
- Expose the `/monitor` endpoint at `http://127.0.0.1:5000`

### 3. Send transactions to monitor

You can test the system using `curl`, Postman, or the simulation script.

#### Example using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/monitor -H "Content-Type: application/json" -d "[{\"timestamp\": \"2025-07-15 12:00:00\", \"status\": \"approved\", \"count\": 120}]"
```

#### Example using PowerShell:

```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:5000/monitor" `
  -Method POST `
  -Body '[{"timestamp": "2025-07-15 12:00:00", "status": "approved", "count": 120}]' `
  -ContentType "application/json"
```

### 4. Run the simulation script

To test the alert system with randomized transactions:

```bash
python test_monitor.py
```

This script will:
- Generate synthetic transactions
- Send them to the `/monitor` endpoint
- Print the alert status (`ok` or `alert`)
- Log results to `alert_log.txt`

### 5. Explore the dashboard

Open the Jupyter Notebook to visualize transaction behavior and anomalies:

```bash
jupyter notebook dashboard.ipynb
```

Inside the notebook, you'll find:
- Overview plots of active transaction types
- Individual plots per status
- Anomalies highlighted in red

---

## Dashboard

Open `dashboard.ipynb` to explore:
- Aggregated transaction volumes per status
- Anomalies highlighted in red
- Overview of active transaction types

---

## Notes

- The model is score-based and trained with Isolation Forest.
- Alerts are triggered when `failed`, `denied`, or `reversed` transactions exceed normal behavior.
- You can adjust sensitivity by tuning the `contamination` parameter in `model.py`.

---

## Deliverables

This folder includes:
- ✅ A working alert system with real-time evaluation
- ✅ A trained anomaly detection model
- ✅ A dashboard for visualization
- ✅ A simulation script for testing
- ✅ Documentation for setup and usage

---