# Monitoring Analyst Challenge – Data Analysis (Part 3.1)

This repository contains my solution for the **Monitoring Intelligence Analyst Challenge – Task 3.1**.  
The goal of this task is to analyze checkout sales data, detect anomalies, and visualize patterns compared to historical behavior.

---

## 📂 Repository Structure
```
cloudwalk-challenge/
│── data/
│   ├── checkout_1.csv              # Raw dataset 1
│   ├── checkout_2.csv              # Raw dataset 2
│
│── analysis/
│   ├── analysis.ipynb              # Jupyter Notebook with SQL queries & visualizations

│── conclusion/
│   ├── c              # Conclusion
│
│── README.md                       # Project documentation
```

---

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/cloudwalk-challenge.git
cd cloudwalk-challenge
```

### 2. Install dependencies
It is recommended to create a virtual environment first.

```bash
pip install -r requirements.txt
```

*(You only need `pandas`, `matplotlib`, `seaborn`, and `jupyter`.)*

### 3. Open the notebook
```bash
cd analysis
jupyter notebook analysis.ipynb
```

---

## 📊 Analysis Overview
- The provided datasets (`checkout_1.csv` and `checkout_2.csv`) contain **sales per hour** with the following fields:
  - `today` – sales for today  
  - `yesterday` – sales for yesterday  
  - `same_day_last_week` – same weekday last week  
  - `avg_last_week` – average from last week  
  - `avg_last_month` – average from last month  

- A SQL-based rule engine was applied to detect anomalies:
  - **Spike Anomaly** → when `today > 2 * avg_last_week`  
  - **Drop Anomaly** → when `today < 0.3 * avg_last_week`  
  - Otherwise → **Normal**  

- Results are stored in:
  - `checkout1_anomalias.csv`  
  - `checkout2_anomalias.csv`  

- Visualization: line charts were generated to compare `today` against historical data.

---

## 📈 Example Results

### Checkout 1
- Spike anomalies detected between **10h–12h** and **15h**.  
- Drop anomaly at **08h**, where sales dropped compared to historical data.  

### Checkout 2
- Strong spikes at **08h–09h**.  
- Severe drops at **15h–17h** (sales dropped to zero, while historical data shows high activity).  

---

## 🛠️ Tech Stack
- **Python 3**  
- **Pandas** for data manipulation  
- **SQLite (in-memory)** for SQL queries  
- **Matplotlib** for visualization  
- **Jupyter Notebook** for interactive analysis  

---

## ✅ Deliverables
- SQL query for anomaly detection.  
- CSV outputs with anomaly flags.  
- Graphical visualization of patterns.  
- Structured explanation of findings.  

---

👉 Next step (Task 3.2) will involve implementing a **real-time monitoring API with alerting system**.  

---

⚡ Author: *Your Name*  
