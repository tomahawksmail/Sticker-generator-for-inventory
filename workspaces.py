from reportlab.lib.pagesizes import inch
from reportlab.pdfgen import canvas

font = "Helvetica-Bold"
hostname = "Workplace"

def generate_pdf(names, output_file):
    page_width = 4 * inch
    page_height = 3 * inch

    number_font_size = 52   # BIG numbers
    label_font_size = 14

    c = canvas.Canvas(output_file, pagesize=(page_width, page_height))

    for i in range(0, len(names), 2):
        margin = 0.25 * inch
        half_height = page_height / 2

        # Border
        c.rect(margin, margin, page_width - 2 * margin, page_height - 2 * margin)

        # Split line
        c.setLineWidth(2)
        c.line(
            margin,
            half_height,
            page_width - margin,
            half_height
        )

        # ========== TOP (normal) ==========
        c.setFont("Helvetica", label_font_size)
        c.drawString(margin + 5, page_height - margin - 20, hostname)

        c.setFont(font, number_font_size)
        name_top = names[i]
        text_width = c.stringWidth(name_top, font, number_font_size)

        c.drawString(
            (page_width - text_width) / 2,
            half_height + 20,
            name_top
        )

        c.setLineWidth(5)
        c.line(
            (page_width - text_width) / 2,
            half_height + 10,
            (page_width + text_width) / 2,
            half_height + 10
        )

        # ========== BOTTOM (reversed) ==========
        if i + 1 < len(names):
            name_bottom = names[i + 1]

            c.saveState()
            c.translate(page_width / 2, half_height / 2)
            c.rotate(180)

            # Workplace (top-left of reversed half)
            c.setFont("Helvetica", label_font_size)
            c.drawString(
                -page_width / 2 + margin + 5,
                half_height / 2 - margin - 20,
                hostname
            )

            # Number
            c.setFont(font, number_font_size)
            text_width = c.stringWidth(name_bottom, font, number_font_size)

            c.drawString(
                -text_width / 2,
                -number_font_size / 2,
                name_bottom
            )

            c.setLineWidth(5)
            c.line(
                -text_width / 2,
                -number_font_size / 2 - 10,
                text_width / 2,
                -number_font_size / 2 - 10
            )

            c.restoreState()

        c.showPage()

    c.save()


names = [f"{i:03d}" for i in range(1, 123)]
generate_pdf(names, "stickers_2_per_page_reversed.pdf")
