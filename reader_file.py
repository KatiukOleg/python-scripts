def analyze_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    cleaned_lines = [line.strip() for line in lines]
    word_count = sum(len(line.split()) for line in cleaned_lines)

    return {
        "lines": len(cleaned_lines),
        "words": word_count,
        "content": cleaned_lines
    }

result = analyze_text("example.txt")
print(result)