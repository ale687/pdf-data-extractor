from src.text_extractor import extract_text_from_pdf
from src.table_extractor import extract_tables_from_pdf
from pathlib import Path


# Define the input directory containing PDF files
input_dir = Path("data/inputs") 

# List all PDF files in the input directory
pdf_files = input_dir.glob("*.pdf")

# Define the output directory for extracted data
output_dir = Path("data/outputs")
output_dir.mkdir(parents=True, exist_ok=True)

# Print the stem (filename without extension) of each PDF file
for pdf_path in pdf_files:
    
    base_name = pdf_path.stem # Use for naming output files
    pages = extract_text_from_pdf(pdf_path)
    tables = extract_tables_from_pdf(pdf_path, pages='all')
    
    # Save extracted text to a .txt file
    text_output_path = output_dir / f"{base_name}_text.txt"
    # Write extracted text to file
    with open(text_output_path, "w", encoding="utf-8") as f:
        # Write each page's text to the file
        for page_text in pages:
            f.write(page_text)
            f.write("\n\n")
            
    # Save extracted tables to CSV files
    for i, df in enumerate(tables):
        # Save each table as a separate CSV file
        table_output_path = output_dir / f"{base_name}_table_{i+1}.csv"
        df.to_csv(table_output_path, sep=";", decimal=",", index=False)
        
    

   





