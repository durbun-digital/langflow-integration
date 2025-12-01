import csv

def create_supplier_metrics_csv(filename="supplier_metrics.csv"):
    # Header
    header = ["metric", "value", "unit", "notes"]

    # Example supplier metrics
    data = [
        ["on_time_delivery", 92, "percent", "Based on last 12 months"],
        ["order_accuracy", 96, "percent", "From ERP accuracy logs"],
        ["quality_defect_rate", 1.8, "percent", "Lower is better"],
        ["lead_time_reliability", 88, "percent", "Measured vs promised dates"],
        ["financial_stability", 78, "score", "Based on credit reports"],
        ["responsiveness", 90, "score", "Average response time SLAs"],
        ["sustainability_score", 70, "score", "ESG audit results"],
        ["risk_exposure", 22, "score", "Lower is better"]
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    print(f"{filename} created successfully!")

# Run
create_supplier_metrics_csv()
