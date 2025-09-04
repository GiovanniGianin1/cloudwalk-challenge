#  Data Analysis (Part 3.1)

This repository contains my solution for the **Task 3.1**.  
The goal of this task is to analyze checkout sales data, detect anomalies, and visualize patterns compared to historical behavior.

---

##  Repository Structure
```
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
```

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/GiovanniGianin1/cloudwalk-challenge.git
cd "cloudwalk-challenge\3.1 - Anomaly Behavior Analysis"
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

## Executive Summary (Task 3.1)

📄 [Download Full Report (PDF)](https://github.com/GiovanniGianin1/cloudwalk-challenge/blob/main/3.1%20-%20Anomaly%20Behavior%20Analysis/README.md)

---


## Tech Stack
- **Python 3**  
- **Pandas** for data manipulation  
- **SQLite (in-memory)** for SQL queries  
- **Matplotlib** for visualization  
- **Jupyter Notebook** for interactive analysis  

---

## Deliverables
- SQL query for anomaly detection.  
- Graphical visualization of patterns.  
- Structured explanation of findings.  

---