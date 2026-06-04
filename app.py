import sys
import os
import streamlit as st

sys.path.append(os.path.abspath("."))

from config.database import run_query
from Dashboard.kpi_calculations import calculate_kpis
from Dashboard.charts import TransactionAmountDistribution,TransactionStatusDistribution,TransactionTypeDistribution,TransactionSummary,DailyTransactionTrend

st.set_page_config(page_title="Transaction Dashboard", layout="wide", page_icon="🏦")

st.sidebar.image("C:\\Users\\HP\\Downloads\\ChatGPT Image Jun 3, 2026, 10_05_03 PM.png", width=200)
page = st.sidebar.selectbox("Select page", ["Dashboard", "Transactions Overview"])

query = "SELECT * FROM clean_transaction_data"
df = run_query(query)


def filter_transactions(data):
    st.sidebar.header("Dashboard Filters")
    start_date = st.sidebar.date_input("Start Date", value=data["date"].min(), key="start_date")
    end_date = st.sidebar.date_input("End Date", value=data["date"].max(), key="end_date")
    transaction_types = st.sidebar.selectbox(
        "Transaction Type",
        ["All"] + list(data["Transaction Type"].unique()),
        key="transaction_type"
    )

    filtered = data[(data["date"] >= start_date) & (data["date"] <= end_date)]
    if transaction_types != "All":
        filtered = filtered[filtered["Transaction Type"] == transaction_types]
    return filtered


def render_dashboard(data):
    st.title("VTAPP FINTECH Dashboard")
    filtered_df = filter_transactions(data)

    kpis = calculate_kpis(filtered_df)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Total Transactions", kpis["Total Transactions"])
    col2.metric("Total Amount", f"${kpis["Total Amount"]:.2f}")
    col3.metric("Success Rate", f"{kpis["Success Rate"]:.2f}%")
    col4.metric("Successful Transactions", kpis["Successful Transactions"])
    col5.metric("Failed Transactions", kpis["Failed Transactions"])
    col6.metric("Average Transaction Amount", f"${kpis["Average Transaction Amount"]:.2f}")

    st.subheader("Transaction Status Distribution")
    fig1 = TransactionStatusDistribution(filtered_df)
    st.plotly_chart(fig1, width='stretch')

    st.subheader("Transaction Amount Distribution")
    fig2 = TransactionAmountDistribution(filtered_df)
    st.plotly_chart(fig2, width='stretch')

    

    st.subheader("Transaction Summary by Type")
    fig4 = TransactionSummary(filtered_df)
    st.plotly_chart(fig4, width ='stretch')

    st.subheader("Daily Transaction Trend")
    fig5 = DailyTransactionTrend(filtered_df)
    st.plotly_chart(fig5, width ='stretch')

    st.subheader("Transaction Data Table")
    search_term = st.text_input("Search by Transaction ID", key="search_term")
    table_df = filtered_df.copy()
    if search_term:
        table_df = table_df[table_df["Transaction ID"].str.contains(search_term, case=False)]
    st.dataframe(table_df)


def render_overview(data):
    st.title("Transactions Overview")
    st.markdown("Raw transaction data and summary metrics.")

    filtered_df = filter_transactions(data)
    if filtered_df.empty:
        st.warning("No transactions match the selected filters.")
        return

    total_transactions = len(filtered_df)
    total_amount = filtered_df["Transaction Amount"].sum()
    success_rate = (
        filtered_df[filtered_df["Transaction Status"] == "Success"].shape[0] / total_transactions
    ) * 100

    st.metric("Total Transactions", total_transactions)
    st.metric("Total Amount", f"${total_amount:,.2f}")
    st.metric("Success Rate", f"{success_rate:.2f}%")

    st.markdown("### Top 10 Transactions by Amount")
    top_transactions = filtered_df.sort_values("Transaction Amount", ascending=False).head(10)
    st.dataframe(top_transactions)

    st.markdown("### Raw Transaction Data")
    st.dataframe(filtered_df)


if page == "Dashboard":
    render_dashboard(df)
else:
    render_overview(df)










