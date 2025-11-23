from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ---------- Fake Job Description ----------
job_title = "Data Scientist - AI & ML"
company = "TechNova Solutions"
location = "San Francisco, CA"
description = """Responsibilities:
- Design and implement machine learning models for predictive analytics
- Collaborate with cross-functional teams to deploy AI solutions
- Perform data cleaning, feature engineering, and analysis
- Present insights to stakeholders and make data-driven recommendations

Qualifications:
- BS/MS in Computer Science, Statistics, or related field
- Strong Python skills (pandas, scikit-learn, TensorFlow/PyTorch)
- Experience with SQL and cloud platforms (AWS, GCP)
- Excellent communication and teamwork skills
"""

job_pdf_file = "fake_job_description.pdf"
c = canvas.Canvas(job_pdf_file, pagesize=letter)
width, height = letter

c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 50, job_title)

c.setFont("Helvetica", 12)
c.drawString(50, height - 80, f"Company: {company}")
c.drawString(50, height - 100, f"Location: {location}")

text = c.beginText(50, height - 130)
text.setFont("Helvetica", 12)
for line in description.splitlines():
    text.textLine(line)
c.drawText(text)
c.save()

# ---------- Fake Resume ----------
name = "John Doe"
resume_title = "Data Scientist"
contact_info = "Email: john.doe@example.com | Phone: 555-123-4567 | LinkedIn: linkedin.com/in/johndoe"
summary = """Summary:
Data Scientist with 3+ years of experience in machine learning, data analysis, and predictive modeling. Proficient in Python, SQL, and cloud platforms."""

experience = """Experience:
Data Scientist | AI Labs | 2021 - Present
- Built ML models to predict customer churn, improving retention by 15%
- Automated data preprocessing pipelines using Python
- Collaborated with engineering to deploy models in production

Junior Data Scientist | DataWorks | 2019 - 2021
- Performed exploratory data analysis and visualization
- Assisted in model training and evaluation
"""

education = """Education:
MS in Computer Science | Stanford University | 2017 - 2019
BS in Statistics | University of California, Berkeley | 2013 - 2017
"""

resume_pdf_file = "fake_resume.pdf"
c = canvas.Canvas(resume_pdf_file, pagesize=letter)
c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 50, name)

c.setFont("Helvetica-Bold", 12)
c.drawString(50, height - 80, resume_title)
c.setFont("Helvetica", 10)
c.drawString(50, height - 100, contact_info)

y = height - 130
for section in [summary, experience, education]:
    text = c.beginText(50, y)
    text.setFont("Helvetica", 10)
    for line in section.splitlines():
        text.textLine(line)
    c.drawText(text)
    y -= (len(section.splitlines()) * 14 + 20)

c.save()

print(f"Generated PDFs: {job_pdf_file}, {resume_pdf_file}")
