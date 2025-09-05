# CloudWalk Challenge — Monitoring Intelligence Analyst (Night Shift)

This repository contains the solution for the technical challenge proposed by CloudWalk for the Monitoring Intelligence Analyst (Night Shift) position.

---

## Challenge Overview

The challenge is divided into two main tasks:

### Task 3.1 — Anomaly Behavior Analysis
Analyze hourly transaction data from two checkout points and identify anomaly patterns by comparing today's sales volume with historical data (yesterday, same weekday last week, weekly average, and monthly average).

### Task 3.2 — Real-Time Monitoring & Alert System
Build a simple real-time monitoring system that receives transaction data and triggers alerts when anomalies are detected (e.g., spikes in failed, denied, or reversed transactions).

---

## Project Structure

```
cloudwalk-challenge/
│
├── README.md                      # Root documentation for the entire challenge (this file)
├── .gitignore                     # Git ignore rules for Python, logs, data, etc.
│
├── 3.1 - Anomaly Behavior Analysis/
│   ├── analysis/
│   │   ├── analysis.ipynb         # Jupyter Notebook with SQL queries and visualizations
│   │
│   ├── conclusion/
│   │   ├── conclusion.pdf         # Executive summary of findings and insights
│   │
│   ├── data/
│   │   ├── checkout_1.csv         # Raw dataset 1 used for SQL analysis
│   │   ├── checkout_2.csv         # Raw dataset 2 used for SQL analysis
│   │
│   ├── README.md                  # Documentation for the anomaly behavior analysis
│   ├── requirements.txt           # Python dependencies for running the notebook
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
│   │   ├── deshboard.ipynb         # Dashboard with anomaly visualization
│   │   ├── model.py                # Isolation Forest model for anomaly detection
│   │   ├── test_monitor.py         # Script to simulate transactions and test alerts
│   │   ├── utils.py                # Data loading and aggregation functions
│   │
│   ├── README.md                   # Documentation for the monitoring system
│   ├── requirements.txt            # Python dependencies for running the alert system

```

---

## Technologies Used

- Python (Pandas, Matplotlib, Seaborn)
- SQLite (for SQL query simulation)
- Jupyter Notebook
- Markdown & PDF for documentation

---

## Executive Summary (Task 3.1)

📄 [Download Full Report (PDF)](https://github.com/GiovanniGianin1/cloudwalk-challenge/blob/main/3.1%20-%20Anomaly%20Behavior%20Analysis/README.md)

---

## Executive Summary (Task 3.2)

📄 [View Full Technical Documentation](https://github.com/GiovanniGianin1/cloudwalk-challenge/blob/main/3.2%20-%20Real-Time%20Monitoring%20%26%20Alerts/README.md)

--- 

Prepared by: Giovanni Gianini
Date: September 3, 2025
