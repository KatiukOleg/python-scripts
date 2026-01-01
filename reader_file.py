import os
import sys
import argparse
import json
from rich.console import Console


def analyze_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    cleaned_lines = [line.strip() for line in lines]
    word_count = sum(len(line.split()) for line in cleaned_lines)

    return {
        "lines": len(cleaned_lines),
        "words": word_count,
        "content": cleaned_lines
    }

def read_data(file_path):
    ext = os.path.splitext(file_path)[1]
    if ext == ".txt":
        return analyze_txt(file_path)
    if ext == ".json":
        return analyze_json(file_path)
    raise ValueError("Unsupported format")

if __name__ == "__main__":
    console = Console()
    parser = argparse.ArgumentParser(description="Simple script for reading files")
    parser.add_argument("--file", "-f", required=True, help="Name of file")
    arguments = parser.parse_args()
    result = read_data(arguments.file)
    console.print("Python version:" + sys.version)
    console.print(result)