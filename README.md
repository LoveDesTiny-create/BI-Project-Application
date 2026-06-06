# Transaction Analystics Dashboard

## Project Overview
The Transaction Analystics Dashboard is a Business Intelligence (BI) application developed using Python, SQL, Plotly, and Streamlit.

---

## Project Objective

The objective of this project is to monitor transaction performance and provide stakeholders with real-time insights into:

- Transaction volume
-Transaction value
-Success and failure rates
-Fraudulent activities
-Network performance metrics
-Transaction trends

---

## Technologies Used

-Python
-SQL
-Pandas
-Numpy
-Ipykernel
-Matplotlib
-Seaborn
-Scikit-learn
-Sqlalchemy
-Mysql-connector-python
-Python-dotenv
-Nbformat
-Plotly
-Streamlit
-Git
-Github

---

## Features

### Data Engineering

-SQL Database Connection
-Data Cleaning Pipeline
-Data Transformation Process

### KPI Monitoring

-Total Transactions
-Total Transaction Amount
-Success Rate
-Failed Transactions

### Interactive Dashboard

-Data Range Filter
-Transaction Type Filter
-Searchable Transaction Table
-Interactive Charts

---

## Project Structure

```plaintext
BI_PROJECT/
│

├── .streamlit/
    │   └── config.toml

│   
  ├── Config/
    │   └── database.py
│
  ├── Dashboard/
    │   ├── kpi_calculation.py
    │   ├── charts.py
    │   └── test_app.py
│
  ├── data_transformation(ETL)/
    │   └── clean_data.py
│
  ├── Pipeline/
    │   └── run_pipeline.py
│
  ├── .gitignore
  ├── app.py
  ├── README.md
  ├── python
  └── requirements.txt

---

## How to Run the Project

### Install Dependencies

``bash
pip install -r requirements.txt
---

### Run Data Pipeline

```bash
python -m Pipeline.run_pipeline
---

### Launch Dashboard

```bash
streamlit run app.py
```

---

## Author

Name: Ivoke Destiny

Role: Financial Analyst

Github: LoveDesTiny-create