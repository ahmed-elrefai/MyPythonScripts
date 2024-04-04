import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import utils
from reportlab.pdfgen import canvas

def images_to_pdf(image_folder, pdf_file):
    """
    Convert images from a folder to a PDF file.
    
    Args:
    - image_folder (str): Path to the folder containing images.
    - pdf_file (str): Path to the output PDF file.
    """
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    # Sort image files by name
    image_files.sort()
    
    c = canvas.Canvas(pdf_file, pagesize=letter)
    
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        
        # Get image dimensions
        img = utils.ImageReader(image_path)
        img_width, img_height = img.getSize()
        
        # Calculate aspect ratio to fit the image on the page
        aspect_ratio = img_width / img_height
        page_width, page_height = letter

        # Draw image on PDF canvas
        c.drawImage(image_path, x=0, y=0, width=page_width, height=page_height)
        c.showPage()
    
    c.save()
    print(f"PDF created: {pdf_file}")

if __name__ == "__main__":
    image_folder = "/path/to/your/dir/"  # Change this to your image folder path
    pdf_file = "output_file_name.pdf"  # Output PDF file path
    images_to_pdf(image_folder, pdf_file)
