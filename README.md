# 📈 Analysis of Financial Markets Using Machine Learning

> Bachelor Thesis in Quantitative Finance, joint study programme Computer Science & Mathematics 
> Author: Marek Šugár  
> Comenius University in Bratislava, Faculty of Mathematics, Physics and Informatics
> Year: 2026  
> Supervisor: Mgr. Samuel Rosa, PhD. (Department of Applied Mathematics and Statistics)

---

## 🔍 Project Overview

This project investigates predictability of the IT segment (65 stocks) across the index S&P 500. Among these stocks, we implemented list of various ML frameworks,
using the modified rolling window data-preparatory approach constructed prediction pipeline which predicts next-day closing price of the analyzed stocks.

On top of that, these predictions are used as a foundation for mean-variance portfolio (MVP) optimization.

The objective of this thesis is to:

- Analyze predictability of IT stocks segment
- Implement and compare statistical and machine learning models
- Evaluate out-of-sample forecasting performance
- Assess applied significance of results by constructing Markowitz MVP

This work provides a fully reproducible quantitative research pipeline (the only determining element is the database of stocks) suitable for academic applications.

---

## 🧠 Models Implemented

- ARIMA  
- k-Nearest Neighbors (kNN)  
- Lasso
- Ridge
- Linear regression
- Random Forest 
- Random Walk (NAÏVE)

---

## 📊 Data

- **Source:** Yahoo Finance
- **Frequency:** Daily
- **Time Period:** September 2017 – January 2026 (training+validation 2017 - 2022; testing 2023-2026)
- **Assets:** 65 stocks of IT segment across S&P 500 index

### Preprocessing Steps

- Matrix of features construction  
- Handling EU/US markets differences yielding missing values   
- Feature variables accumulation  
- Rolling window split

---

## 🏗 Methodology

1. Data collection and cleaning  
2. Exploratory data analysis  
3. Feature accumulation  
4. Model estimation  
5. Hyperparameter tuning (on rolling window)
6. Rolling-window forecasting  
7. Out-of-sample evaluation  

---

## 📈 Results of predictions (Test)

| Model         | MAPE (%)  | Dominance (%) |
|--------------|--------|--------|
| ARIMA  | 1.923 | 56.68 |
| Ridge (SM)        | 1.918 | 42.57 |
| Ridge (GM)          | 1.904 | 43.48 |
| Linear regression          | 1.903 | 43.89 |
| Lasso (GM)          | 2.18 | 39.12 |
| Lasso (SM)          | 2.36 | 36.55 |
| Benchmark (Naïve, k-NN, RFA)          | 1.69 |  |

## 📈 Results of predictions (Test)

| Model         | CAGR (%)  | AV (%)   | Sharpe ratio   |
|--------------|--------|--------| --------|
| Naïve  | 16.48 | 25.20 | 0.65   |
| ARIMA        | 15.67 | 25.48 | 0.62   |
| Ridge (SM)          | 15.39 | 25.28 | 0.61   |
| Ridge (GM)          | 15.20 | 25.29 | 0.6   |
| Lasso (SM)          | 17.11 | 25.51 | 0.67   |
| Lasso (GM)          | 16.88 | 25.53 | 0.66   |
|--------------|--------|--------| --------|
| S&P 500        | 8.35 | 23.1 | 0.36   |
| NASDAQ Composite         | 18.51 | 25.15 | 0.74   |


### Key Findings

- Machine learning models cannot out-perform naïve benchmark on this segment. Naïve (random-walk) model remains difficult to statistically outperform.
- Forecasting performance deteriorates with longer training windows.
- To construct profitable and risk-averse portfolio, predictions are not really important; risk management is more
- Many sources in literature do not apply predictions on portfolio management AND/OR Do not evaluate predictions to the proper naïve method or benchmark it to something worse, to make the predictions look robust.

---

## 🚀 How to Run?

### 1. Clone Repository

```bash
git clone https://github.com/sugy-w/Bachelor-Thesis/
cd your-repo-name
```

### 2. Install Dependencies

```bash
pip3 install -r requirements.txt
```

---

## 🛠 Technologies Used

- Python 3.13  
- NumPy  
- pandas  
- statsmodels  
- scikit-learn  
- matplotlib  
- seaborn
- SQL/SQLite3  

---

## 🔬 Reproducibility

- Explicit train/test split  
- Documented preprocessing (see the Thesis) 
- Modular model pipeline (replace StockData.db up to the desire) 

All results can be reproduced using the provided scripts and data.

---

## 📜 Thesis Abstract

Here will be abstract, when done!

---

## 📌 Key Contributions

- Implementation of a rolling-window evaluation framework  
- Direct comparison of econometric and machine learning models  
- Robust out-of-sample forecasting evaluation  
- Clean and modular research code structure  

---

## ⚠ Disclaimer

This project was developed for academic purposes as part of a bachelor thesis.  
It does not constitute financial or investment advice.

---
