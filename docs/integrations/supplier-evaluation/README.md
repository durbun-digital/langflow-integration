# Supplier Evaluation Flow

The **Supplier Evaluation Flow** is a LangFlow integration that assesses suppliers based on performance, risk, and overall reliability.
It provides a **structured, numerical evaluation** with reasoning, allowing teams to make informed sourcing and procurement decisions.

> **Note:** For production use, provide updated supplier data in CSV or JSON format. If using Excel or PDF files, convert them to a parseable format first.
> Ensure that your **OpenAI API key** is configured through the flow’s LLM components or via LangFlow’s environment settings.

---

## 🔹 Key Features

* **Supplier Metrics**: Calculates normalized scores for key metrics such as on-time delivery, quality defect rate, financial stability, and responsiveness.
* **Composite Indices**: Generates weighted indices including Supplier Performance Index (SPI), Supplier Risk Index (SRI), and Overall Supplier Score (OSS).
* **Reasoning**: Provides explanations for each metric and index to justify the scoring.
* **Flexible Input**: Works with CSV, JSON, or parsed PDF/Excel data.
* **Ready-to-Use**: Comes with an exported `flow.json` that can be imported directly into LangFlow.

**Visual Preview:**
![Supplier Evaluation Flow Screenshot](assets/supplier-evaluation-flow.png)

---

## 📁 Repository Structure

```
supplier-evaluation/
├── README.md
├── flow.json                 # LangFlow exported flow
├── supplier_metrics.csv      # Sample supplier metrics input
├── custom_weights.csv        # Optional custom weights
└── assets/                   # Optional screenshots and example files
    └── supplier-evaluation-flow.png
```

---

## 🚀 Getting Started

1. Open LangFlow and navigate to **Import Flow**
2. Select `flow.json` from this folder
3. Upload supplier data (CSV or JSON) and optionally custom weights
4. The flow will output:

---

### Example Output

Here is the computed composite supplier indices based on the provided metrics and weights:

```json
{
  "indices": {
    "Supplier Performance Index (SPI)": {
      "value": 80.25,
      "weights": {
        "on_time_delivery": 25,
        "order_accuracy": 20,
        "lead_time_reliability": 20,
        "quality_defect_rate": 20,
        "responsiveness": 15
      },
      "reason": "The SPI reflects the supplier's strong performance in on-time delivery and order accuracy, with a solid overall score."
    },
    "Supplier Risk Index (SRI)": {
      "value": 61.0,
      "weights": {
        "risk_exposure": 50,
        "financial_stability": 30,
        "sustainability_score": 20
      },
      "reason": "The SRI indicates moderate risk exposure and financial stability, with room for improvement in sustainability efforts."
    },
    "Overall Supplier Score (OSS)": {
      "value": 73.15,
      "weights": {
        "SPI_contribution": 60,
        "risk_adjustment": 40
      },
      "formula": "OSS = (SPI * 0.6) + ((100 - SRI) * 0.4)",
      "reason": "The OSS combines the SPI and adjusts for risk exposure, providing a balanced view of supplier performance and risk."
    }
  }
}
```

---

### Explanation of Weights Used

**Supplier Performance Index (SPI) Weights:**

* On-time Delivery: 25%
* Order Accuracy: 20%
* Lead Time Reliability: 20%
* Quality Defect Rate: 20%
* Responsiveness: 15%

**Supplier Risk Index (SRI) Weights:**

* Risk Exposure: 50%
* Financial Stability: 30%
* Sustainability Score: 20%

**Overall Supplier Score (OSS) Weights:**

* SPI Contribution: 60% (weighted contribution of SPI)
* Risk Adjustment: 40% (adjustment based on risk exposure)

---

### Calculation Details

* **SPI Calculation:**
  `SPI = (85 × 0.25) + (90 × 0.20) + (75 × 0.20) + (80 × 0.20) + (65 × 0.15) = 80.25`

* **SRI Calculation:**
  `SRI = (50 × 0.50) + (70 × 0.30) + (60 × 0.20) = 61.0`

* **OSS Calculation:**
  `OSS = (80.25 × 0.6) + ((100 - 61.0) × 0.4) = 73.15`

These indices provide a comprehensive view of the supplier's performance and risk profile, aiding in strategic decision-making.

---

## ⚡ Use Case

This flow is ideal for:

* Evaluating supplier reliability and performance consistently
* Supporting procurement decisions with data-driven insights
* Integrating supplier scoring into supply chain dashboards or ERP systems
