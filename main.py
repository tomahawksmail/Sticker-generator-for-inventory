############################################################
### Script generates pdf file for stickers with PC names ###
### Designed by Maksym Tsybulskyi, 2024 ###
############################################################

from reportlab.lib.pagesizes import inch
from reportlab.pdfgen import canvas
font = "Helvetica-Bold"
hostname = "Workplace"

def generate_pdf(names, output_file):
    # Set page size to 6"x4"
    page_width = 4 * inch
    page_height = 3 * inch
    pagesize = 40
    year = "2024"
    # Create a PDF canvas
    c = canvas.Canvas(output_file, pagesize=(page_width, page_height))

    for name in names:
        # Set the font on each page to ensure consistency
        c.setFont(font, pagesize)  # Adjust the font size as needed


        # Draw the border around the page
        margin = 0.25 * inch
        c.rect(margin, margin, page_width - 2 * margin, page_height - 2 * margin)

        # Set the position for writing the name in the center of the page
        text_width = c.stringWidth(name, font, pagesize)
        x_position = (page_width - text_width) / 2  # Center horizontally
        y_position = (page_height / 2)  # Center vertically

        # Draw the name on the page
        c.drawString(x_position, y_position, name)

        # Set a different line width for the underline
        c.setLineWidth(5)  # Adjust the line width for the underline

        # Draw an underline below the text
        underline_y = y_position - 10  # Adjust spacing for the underline
        c.line(x_position, underline_y, x_position + text_width, underline_y)

        # Add small text in the bottom-right corner
        c.setFont("Helvetica", 12)  # Smaller font size for small text
        small_text_width = c.stringWidth(year, "Helvetica", 12)
        c.drawString(page_width - small_text_width - 1.5 * margin, margin * 1.5 , year)

        # Add small text in the bottom-right corner
        c.setFont("Helvetica", 12)  # Smaller font size for small text
        small_text_width = c.stringWidth(hostname, "Helvetica", 12)
        c.drawString(25, 170, hostname)

        # Add a new page for the next name
        c.showPage()
    # Save the PDF
    c.save()


# Example usage:
names = []
template = "00"
for i in range(1, 122):  # 122 so 121 is included
    name = f"{i:03d}"
    print(name)
    names.append(name)



generate_pdf(names, "names_list_per_page_4x6.pdf")
