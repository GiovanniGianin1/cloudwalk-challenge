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
│── README.md                        # Project documentation (this file)
│ 
│ 
│── 3.1 - Anomaly Behavior Analysis/ 
│   ├── data/ 
│   │   ├── checkout_1.csv              # Raw dataset 1 
│   │   ├── checkout_2.csv              # Raw dataset 2 
│   │ 
│   ├── analysis/ 
│   │   ├── analysis.ipynb              # Jupyter Notebook with SQL queries & visualizations 
│   │ 
│   ├── conclusion/ 
│   │   ├── conclusion.pdf              # Executive summary of findings 
│   │ 
│   │── README.md                        # Project documentation 
│   │── requirements.txt                 # Requirements to run this project 
│ 
│ 
│── 3.2 - Real-Time Monitoring & Alerts/ 
│   ├── monitoring/ 
│   │   ├── app.py                      # Alert system implementation 
│   │   ├── model.py                    # Anomaly detection logic 
│   │   ├── dashboard.ipynb             # Real-time visualization 
│   │   ├── README.md                   # Documentation for Task 3.2 
│   │ 
│   │── README.md                       # Project documentation 
│   │── requirements.txt                 # Requirements to run this project 

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

📄 [Download Full Report (PDF)](https://github.com/GiovanniGianin1/cloudwalk-challenge/blob/main/3.2%20-%20Real-Time%20Monitoring%20%26%20Alerts/README.md)

---

Prepared by: Giovanni Gianini
Date: September 3, 2025
