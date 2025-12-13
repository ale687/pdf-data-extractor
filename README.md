# PDF Data Extractor 📄➡️📊

This project automates the extraction of **text and tables from multiple PDF files**, transforming unstructured documents into **TXT and CSV files** ready for analysis, reporting, or database ingestion.

The script automatically scans an input directory, processes each PDF found, and generates structured outputs without manual intervention.

---

## 🚀 Features

- 📂 Processes **all PDF files** inside an input folder
- 📝 Extracts text from each page and saves it as a `.txt` file
- 📊 Extracts tables from PDFs and exports them as `.csv` files
- 🔁 Handles multiple PDFs without overwriting outputs
- 🧩 Modular and reusable code structure
- ⚙️ Designed for automation workflows

---

## 🛠️ Technologies Used

- **Python**
- **PyMuPDF (fitz)** – PDF text extraction
- **tabula-py** – PDF table extraction
- **pandas** – tabular data processing
- **pathlib** – file system and path handling

⚠️ **Note:** `tabula-py` requires **Java** to be installed on the system.

---

## 📁 Project Structure

pdf-data-extractor/
│
├── data/
│ ├── inputs/ # Input PDF files
│ └── outputs/ # Generated TXT and CSV files
│
├── src/
│ ├── init.py
│ ├── text_extractor.py
│ └── table_extractor.py
│
├── main.py
├── requirements.txt
└── README.md

yaml
Copiar código

---

## ⚙️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/ale687/pdf-data-extractor.git
cd pdf-data-extractor

---

👤 Author

Claudio Alejandro Ledesma
Information Systems Engineering student (UTN)

Areas of Interest

Backend Development

Data Engineering

Process Automation