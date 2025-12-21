import os
import fitz  # PyMuPDF

# Paths
SOURCE_PDF_DIR = r"C:\pdfocr\pdf-chat\PDFs"
FLAT_TEXT_DIR = r"C:\pdfocr\pdf-chat\text"

def extract_to_flat_folder():
    if not os.path.exists(FLAT_TEXT_DIR):
        os.makedirs(FLAT_TEXT_DIR)

    for root, dirs, files in os.walk(SOURCE_PDF_DIR):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                
                # Get the folder structure as a string (e.g., "Court Records/CaseName")
                relative_path = os.path.relpath(root, SOURCE_PDF_DIR)
                
                # Create a unique filename for the flat folder
                # Example: "Court Records__CaseName__001.txt"
                unique_filename = f"{relative_path.replace(os.sep, '__')}__{file.replace('.pdf', '.txt')}"
                output_path = os.path.join(FLAT_TEXT_DIR, unique_filename)

                try:
                    with fitz.open(pdf_path) as doc:
                        text_data = [
                            f"METADATA_SOURCE: {relative_path}",
                            f"METADATA_FILENAME: {file}",
                            "-" * 40
                        ]
                        for page in doc:
                            text_data.append(page.get_text())

                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write("\n".join(text_data))
                    print(f"Flattened & Extracted: {unique_filename}")

                except Exception as e:
                    print(f"Failed {file}: {e}")

if __name__ == "__main__":
    extract_to_flat_folder()