import plotly.express as px

def TransactionAmountDistribution(df):
     fig = px.histogram(df, x="Transaction Amount", nbins=50, title="Distribution of Transaction Amounts")
     return fig

def TransactionStatusDistribution(df):
     fig = px.pie(df, names="Transaction Status", title="Transaction Status Distribution")
     return fig

def TransactionTypeDistribution(df):
     fig = px.box(df,
                  x="Transaction Type",
                  y="Transaction Amount",
            color="Transaction Type",
            title="Transaction Type Distribution")
     return fig

def TransactionSummary(df):
     transaction_summary = df.groupby("Transaction Type")["Transaction Amount"].sum().reset_index()
     fig = px.bar(transaction_summary, x="Transaction Type", y="Transaction Amount", color="Transaction Type", title="Transaction Type Distribution")
     return fig

def DailyTransactionTrend(df):
     daily_df = df.groupby("date")["Transaction ID"].count().reset_index()
     daily_df.rename(columns={"Transaction ID": "Total Transactions"}, inplace=True)
     fig = px.line(daily_df, x="date", y="Total Transactions", title="Daily Transaction Trend")
     return fig
