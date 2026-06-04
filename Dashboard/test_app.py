import sys
import os

sys.path.append(os.path.abspath(".."))

from config.database import run_query
from Dashboard.kpi_calculations import calculate_kpis
from Dashboard.charts import TransactionAmountDistribution,TransactionStatusDistribution,TransactionTypeDistribution,TransactionSummary,DailyTransactionTrend
def test_run():
    query = "SELECT * FROM clean_transaction_data"
    df = run_query(query)
    print("Test run_query passed")

    kpis = calculate_kpis(df)
    print("Test calculate_kpis passed")
    print(kpis)

    fig1 = TransactionAmountDistribution(df)
    fig1.show()

    fig2 = TransactionStatusDistribution(df)
    fig2.show()
    


    fig3 = TransactionTypeDistribution(df)
    fig3.show()
    

    fig4 = TransactionSummary(df)
    fig4.show()
    

    fig5 = DailyTransactionTrend(df)    
    fig5.show()
    
    print("Successfully ran all tests")
