# Resume Analyzer Flow

The **Resume Analyzer Flow** is a LangFlow integration that evaluates how well a candidate's resume matches a job description.
It provides a **structured assessment** with a numerical score and reasoning, making it easy to integrate into HR pipelines, recruitment workflows, or automated evaluation systems.

> **Note:** For production use, it is recommended to use a web crawler (e.g., the Firecrawl bundle supported by LangFlow) to automatically retrieve job descriptions instead of providing static files.
> Also, ensure that your **OpenAI API key** is set either through the flow's Language Model components or via the environment configuration in the user settings of the LangFlow UI.


---

## 🔹 Key Features

* **Evaluation Score**: Provides a 0–10 rating of how well the resume fits the job description.
* **Reasoning**: Offers bullet-point explanations covering skills, experience, education, and any gaps.
* **Flexible Use**: Works for any career field, not limited to tech or AI roles.
* **Ready-to-Use**: Comes with an exported `flow.json` that can be imported directly into LangFlow.
* **Visual Preview**: Includes a screenshot of the flow to help you understand its structure and logic ![Resume Analyzer Flow Screenshot](assets/resume-analyzer-flow.png).

---

## 📁 Repository Structure

```
resume-analyzer/
├── README.md
├── flow.json              # LangFlow exported flow
└── assets/                # Optional images, PDFs, and screenshots
    ├── fake-job-description.pdf
    ├── fake-resume.pdf
    └── resume-analyzer-flow.png
```

---

## 🚀 Getting Started

1. Open your LangFlow application
2. Navigate to **Import Flow**
3. Select `flow.json` from this folder
4. Input your **Job Description** and **Resume**
5. The flow will output:

```
Evaluation: X/10

Reasoning:
- [Reason 1]
- [Reason 2]
- [Reason 3]
```

---

## ⚡ Use Case

This flow is perfect for:

* Quickly screening resumes against job descriptions
* Automating preliminary candidate evaluation
* Integrating with HR systems for consistent assessments