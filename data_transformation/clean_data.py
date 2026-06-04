import sys
import os
sys.path.append(os.path.abspath(".."))

import pandas as pd
from config.database import run_query, save_to_sql

def clean_data():
    query = "SELECT * FROM transaction_data"

    df = run_query(query)
    df.drop_duplicates(inplace=True)
    df["Device Used"] = df["Device Used"].replace({"Mobil": "Mobile", "Deskto": "Desktop"})
    df["Transaction Status"] = df["Transaction Status"].replace({"Faile": "Failed", "Succes": "Success"})

    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["date"] = df["Timestamp"].dt.date
    df["time"] = df["Timestamp"].dt.time

    save_to_sql(df, "clean_transaction_data")
    print("Clean transaction data saved")

if __name__ == "__main__":
    clean_data()