# YET-to-JSON Converter

YET-to-JSON Converter is a Python tool designed to parse and convert `.yet` Bible files into structured `.json` files. It processes the hierarchical data from YET files and organizes it into a JSON format where:

- Each **book** contains its respective chapters.
- Each **chapter** contains its verses as properties.
- Verses are split into segments, marking portions as "red-letter text" (e.g., words of Jesus) when applicable.

## Key Features

- **Structured Output**: Books, chapters, and verses are neatly organized for better usability.
- **Red-Letter Text**: Words of Jesus are preserved and marked within the JSON structure.
- **Footnote Removal**: Automatically removes footnotes for cleaner output.
- **Customizable**: Easily adaptable for other parsing needs or output formats.

## Example Output

A `.yet` file with:

```plaintext
book_name    1    Genesis
verse        1    1    1    @@In the beginning @6God created the heavens and the earth.@5
verse        1    1    2    @@The earth was formless and empty.
```

Will generate the following JSON:
```
{
    "info": {},
    "books": {
        "1": {
            "id": 1,
            "name": "Genesis",
            "chapters": {
                "1": {
                    "1": [
                        {
                            "text": "In the beginning",
                            "is_red_letter": false
                        },
                        {
                            "text": "God created the heavens and the earth.",
                            "is_red_letter": true
                        }
                    ],
                    "2": [
                        {
                            "text": "The earth was formless and empty.",
                            "is_red_letter": false
                        }
                    ]
                }
            }
        }
    }
}
```
## Requirements
- Python 3.7+
## Installation
Clone this repository:

```
git clone https://github.com/your-username/yet-to-json-converter.git
cd yet-to-json-converter
```

## Usage
To convert a .yet file to .json, run:
```
python converter.py input_file.yet output_file.json
```
Replace input_file.yet with the path to your .yet file, and output_file.json with the desired output path.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements or new features.

Enjoy using the YET-to-JSON Converter! Feel free to report any issues or request new features.
