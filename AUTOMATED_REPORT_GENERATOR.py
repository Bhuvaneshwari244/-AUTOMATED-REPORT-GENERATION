import pandas as pd
from fpdf import FPDF
import os

def analyze_data(file_path):
    """Reads CSV data and returns a statistical summary."""
    try:
        df = pd.read_csv(file_path)
        summary = df.describe()
        return summary
    except Exception as e:
        print(f"❌ Error reading the file: {e}")
        return None

def generate_pdf(summary, output_file):
    """Generates a PDF report with the statistical summary."""
    if summary is None:
        print("❌ No summary available to generate PDF.")
        return
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "Automated Data Analysis Report", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    for col in summary.columns:
        pdf.cell(200, 10, f"Summary for {col}", ln=True, align='L')
        pdf.set_font("Arial", size=10)
        for index, value in summary[col].items():
            pdf.cell(200, 6, f"{index}: {value:.2f}", ln=True, align='L')
        pdf.ln(5)
        pdf.set_font("Arial", size=12)
    
    try:
        pdf.output(output_file)
        print(f"✅ Report generated successfully: {output_file}")
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")

if __name__ == "__main__":
    file_path = "clean_data.csv"  # Replace with your actual data file
    output_file = "report.pdf"
    
    if not os.path.exists(file_path):
        print(f"❌ Error: The file '{file_path}' does not exist.")
    else:
        summary = analyze_data(file_path)
        generate_pdf(summary, output_file)
    
    input("\nPress Enter to exit...")  # Prevents window from closing immediately
