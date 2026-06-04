import os
from dotenv import load_dotenv

load_dotenv()
DB_USER = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_DATABASE")

from sqlalchemy import create_engine
engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

import pandas as pd

df = pd.read_sql("SELECT * FROM transaction_data", engine)


def run_query(query):
    return pd.read_sql(query, engine)


def save_to_sql(dataframe, table_name):

    dataframe.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} saved successfully")

print("Database connection established successfully")





    

