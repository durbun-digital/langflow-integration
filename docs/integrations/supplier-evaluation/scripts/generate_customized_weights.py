import csv

def create_custom_weights_csv(filename="custom_weights.csv"):
    # Header
    header = ["index_name", "metric", "weight_percent", "notes"]

    # Default weight structure
    default_weights = [
        # SPI
        ["SPI", "on_time_delivery", 25, ""],
        ["SPI", "order_accuracy", 20, ""],
        ["SPI", "lead_time_reliability", 20, ""],
        ["SPI", "quality_defect_rate", 20, ""],
        ["SPI", "responsiveness", 15, ""],
        # SRI
        ["SRI", "risk_exposure", 50, ""],
        ["SRI", "financial_stability", 30, ""],
        ["SRI", "sustainability_score", 20, ""],
        # OSS
        ["OSS", "SPI_contribution", 60, "Use SPI * 0.6"],
        ["OSS", "risk_adjustment", 40, "Use (100 - SRI) * 0.4"]
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(default_weights)

    print(f"{filename} created successfully!")

# Run
create_custom_weights_csv()
