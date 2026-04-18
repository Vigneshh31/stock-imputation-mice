# Missing Value Imputation in Financial Data using MICE

## 📌 Overview
This project focuses on handling missing values in stock market data.
The column `PortfolioOpen` contained missing values represented as -1.

## 🎯 Objective
To accurately estimate missing values using advanced machine learning techniques.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn

## ⚙️ Method Used
- Replaced -1 with NaN
- Applied **MICE (Multiple Imputation using Chained Equations)** using IterativeImputer
- Used all numerical features to predict missing values iteratively

## 📊 Output
- Missing values were successfully imputed
- Final dataset saved as `output.csv`

## 🚀 How to Run
```bash
pip install -r requirements.txt
python main.py# stock-imputation-mice
