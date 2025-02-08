import fitz  # PyMuPDF
import os
import argparse
import fitz
import os

def extract_pdf_content(pdf_path, output_dir):
    """
    Extracts text and images from a PDF.

    Parameters:
        pdf_path (str): Path to the PDF file.
        output_dir (str): Directory where images will be saved.

    Returns:
        tuple: A tuple containing:
            - text_dict (dict): A dictionary where each key is the page number (starting at 1) 
              and the corresponding value is the text from that page.
            - image_dict (dict): A dictionary where each key is the page number (starting at 1) 
              and the corresponding value is a list of paths to images from that page.
    """
    # Open the PDF
    doc = fitz.open(pdf_path)
    text_dict = {}
    image_dict = {}

    # Loop over each page
    for i, page in enumerate(doc):
        page_text = page.get_text("text").strip()
        if page_text:  # Only include pages that have text
            text_dict[i + 1] = page_text

        # Extract images from the page
        image_list = page.get_images(full=True)
        page_images = []

        for img_index, img in enumerate(image_list, start=1):
            try:
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)

                # Determine output file name and path
                image_filename = f"page_{i+1}_img_{img_index}.png"
                output_image_path = os.path.join(output_dir, image_filename)

                # If image is not CMYK (e.g., grayscale or RGB)
                if pix.n < 5:
                    pix.save(output_image_path)
                else:
                    # Convert CMYK to RGB
                    pix_rgb = fitz.Pixmap(fitz.csRGB, pix)
                    pix_rgb.save(output_image_path)
                    pix_rgb = None

                pix = None
                page_images.append(output_image_path)
            except Exception as e:
                print(f"Error processing image on page {i+1}, image {img_index}: {e}")
                continue

        if page_images:  # Only include pages that have images
            image_dict[i + 1] = page_images

    return text_dict, image_dict



# if __name__=="__main__":
#     text_extracted,image_paths=extract_pdf_content("FULLTEXT01.pdf", "output_images")
#     print("text_extracted :",text_extracted)
#     print("image_paths :",image_paths)
