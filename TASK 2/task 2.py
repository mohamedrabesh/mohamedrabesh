import pandas as pd
from fpdf import FPDF
import os

csv_file = 'data.csv'


if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
    df = pd.DataFrame({
        'Name': ['riaz', 'shakeel', 'misba', 'aqeel', 'hajee'],
        'Score': [85, 90, 78, 92, 88]
    })
    df.to_csv(csv_file, index=False)
    print("Sample data.csv file created!")


data = pd.read_csv(csv_file)


mean_score = data['Score'].mean()
max_score = data['Score'].max()
min_score = data['Score'].min()


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Student Score Report", ln=True, align='C')
pdf.ln(10)

pdf.cell(100, 10, txt="Name", border=1)
pdf.cell(50, 10, txt="Score", border=1)
pdf.ln()

for index, row in data.iterrows():
    pdf.cell(100, 10, txt=str(row['Name']), border=1)
    pdf.cell(50, 10, txt=str(row['Score']), border=1)
    pdf.ln()

pdf.ln(10)
pdf.cell(200, 10, txt=f"Average Score: {mean_score:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Highest Score: {max_score}", ln=True)
pdf.cell(200, 10, txt=f"Lowest Score: {min_score}", ln=True)

pdf.output("report.pdf")
print("PDF Report generated successfully!")
