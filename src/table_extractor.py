import tabula


# Extracting tables from PDF using tabula-py
def extract_tables_from_pdf(pdf_path, pages='all'):
    # Read all tables from the PDF
    dfs = tabula.read_pdf(pdf_path, pages=pages)
    return dfs


    