import json

def json_to_html(input_file, output_file):
    # Load JSON data
    with open(input_file, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Initialize HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bible Text</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
            }
            .red-letter {
                color: red;
            }
            .chapter {
                margin-top: 20px;
            }
            .verse {
                margin-left: 20px;
            }
        </style>
    </head>
    <body>
    """

    # Add Bible text to HTML
    for book_id, book in data.get('books', {}).items():
        html_content += f"<h1>{book['name']}</h1>\n"  # Book Title
        # Group verses by chapter
        chapters = {}
        for verse in book.get('verses', []):
            chapter = verse['chapter']
            if chapter not in chapters:
                chapters[chapter] = []
            chapters[chapter].append(verse)

        # Render chapters
        for chapter, verses in chapters.items():
            html_content += f"<div class='chapter'><h2>Chapter {chapter}</h2>\n"
            for verse in verses:
                verse_num = verse['verse']
                verse_text = ""
                for segment in verse['segments']:
                    text = segment['text']
                    if segment['is_red_letter']:
                        verse_text += f"<span class='red-letter'>{text}</span>"
                    else:
                        verse_text += text
                html_content += f"<p class='verse'><strong>{verse_num}:</strong> {verse_text}</p>\n"
            html_content += "</div>\n"

    # Close HTML content
    html_content += """
    </body>
    </html>
    """

    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)
    print(f"Converted {input_file} to {output_file}")

# Usage
input_json_file = "kjv-red2.json"  # Replace with your JSON file
output_html_file = "example.html"
json_to_html(input_json_file, output_html_file)
