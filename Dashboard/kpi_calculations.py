def calculate_kpis(df):
    total_transactions = len(df)
    total_amount = df["Transaction Amount"].sum()
    successful_transactions = df[df["Transaction Status"] == "Success"].shape[0]
    failed_transactions = df[df["Transaction Status"] == "Failed"].shape[0]
    success_rate = (successful_transactions / total_transactions) * 100
    avg_transaction_amount = df["Transaction Amount"].mean()
    failure_rate = (failed_transactions / total_transactions) * 100
    average_latency = df["Latency (ms)"].mean()
    average_bandwidth = df["Slice Bandwidth (Mbps)"].mean()
    return {
        "Total Transactions": total_transactions,
        "Total Amount": total_amount,
        "Successful Transactions": successful_transactions,
        "Failed Transactions": failed_transactions,
        "Success Rate": success_rate,
        "Average Transaction Amount": avg_transaction_amount,
        "Failure Rate": failure_rate,
        "Average Latency": average_latency,
        "Average Bandwidth": average_bandwidth
    }