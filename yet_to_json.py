import json
import re

def parse_yet_file(file_path):
    data = {
        "info": {},
        "books": {}
    }
    
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("\t")
            if not parts:
                continue
            
            # Parse info
            if parts[0] == "info":
                data["info"][parts[1]] = parts[2]
            
            # Parse book names
            elif parts[0] == "book_name":
                book_id = int(parts[1])
                book_name = parts[2]
                book = {"id": book_id, "name": book_name, "verses": []}
                if len(parts) > 3:
                    book["abbreviation"] = parts[3]
                data["books"][book_id] = book
            
            # Parse verses
            elif parts[0] == "verse":
                book_id, chapter, verse, text = int(parts[1]), int(parts[2]), int(parts[3]), parts[4]
                
                # Remove footnote references
                text = re.sub(r"@<f\d+@>@/", "", text)
                
                # Parse red-letter and other text
                segments = []
                last_pos = 0
                for match in re.finditer(r"@6(.*?)@5", text):
                    # Add non-red-letter text before the match
                    if match.start() > last_pos:
                        segments.append({
                            "text": text[last_pos:match.start()],
                            "is_red_letter": False
                        })
                    
                    # Add red-letter text
                    segments.append({
                        "text": match.group(1),
                        "is_red_letter": True
                    })
                    last_pos = match.end()
                
                # Add remaining non-red-letter text
                if last_pos < len(text):
                    segments.append({
                        "text": text[last_pos:],
                        "is_red_letter": False
                    })
                
                # Clean up unwanted formatting tags (@7, @9, @@, and other tags)
                for segment in segments:
                    segment["text"] = re.sub(r"@7|@9|@@|@[^0-9]", "", segment["text"]).strip()
                
                # Add verse data to the corresponding book
                if book_id in data["books"]:
                    data["books"][book_id]["verses"].append({
                        "chapter": chapter,
                        "verse": verse,
                        "segments": segments
                    })
    return data

def convert_to_json(input_file, output_file):
    data = parse_yet_file(input_file)
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Converted {input_file} to {output_file}")

# Usage
input_yet_file = "kjv-red.yet"  # Replace with your .yet file
output_json_file = "kjv-red.json"
convert_to_json(input_yet_file, output_json_file) 
