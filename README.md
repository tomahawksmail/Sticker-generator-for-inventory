# PC Hostname Sticker Generator (3"x4")

This Python script generates 3"x4" PDF stickers for each PC hostname, with each name displayed prominently in bold font, centered on the page. The PDF includes a border around the hostname, an underline, and small text in the bottom-right corner of each page. The tool is useful for creating hostname stickers for labeling physical devices such as laptops, servers, or desktops.

# Features

- Bold Hostnames: Displays hostnames in bold, centered on each page.
- Custom Page Size (3"x4"): Each page is sized 3 inches by 4 inches, making it ideal for smaller sticker labels.
- Borders: A rectangular border around the hostname to give the sticker a professional look.
- Underline: Hostnames are underlined to enhance readability.
- Small Text: Adds small text ("Generated PDF") to the bottom-right corner of each page.

# Requirements
- Python 3.x
- ReportLab: A Python library for generating PDFs. You can install it using:

```bash
pip install reportlab
```

# Usage
- Clone this repository or download the script.
- Prepare a text file (hostnames.txt) that contains one PC hostname per line.
- Run the script with the following command:

```bash
python generate_stickers.py
```
This will generate a PDF file with each PC hostname on a separate 3"x4" page.

# License
This project is licensed under the MIT License.
