import requests
import json
import csv
import yaml
import xml.etree.ElementTree as ET
from faker import Faker
import os

# Инициализация Faker для генерации случайных данных
fake = Faker()

# ПАРАМЕТРЫ - ЗАМЕНИ НА СВОИ
STUDENT_NAME = "Akhmetov Miras"  # Твое имя
TOKEN_HASH8 = "1fa08bd"         # Первые 8 символов твоего последнего коммита

def generate_data():
    # Создаем структуру папок, если их нет
    os.makedirs('artifacts/day2', exist_ok=True)
    
    # 1. Генерируем данные о 100 книгах
    books = []
    for _ in range(100):
        books.append({
            "title": fake.catch_phrase(),
            "author": fake.name(),
            "year": fake.year(),
            "isbn": fake.isbn13()
        })

    # 2. Сохраняем в JSON (normalized.json)
    normalized_data = {
        "student": {
            "name": STUDENT_NAME,
            "token_hash8": TOKEN_HASH8
        },
        "books": books
    }
    with open('artifacts/day2/normalized.json', 'w') as f:
        json.dump(normalized_data, f, indent=4)

    # 3. Сохраняем в CSV (normalized.csv)
    with open('artifacts/day2/normalized.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["token", "token_hash8"])
        writer.writerow([STUDENT_NAME, TOKEN_HASH8])
        writer.writerow([])
        writer.writerow(["title", "author", "year", "isbn"])
        for book in books:
            writer.writerow([book["title"], book["author"], book["year"], book["isbn"]])

    # 4. Сохраняем в YAML (normalized.yaml)
    with open('artifacts/day2/normalized.yaml', 'w') as f:
        yaml.dump(normalized_data, f)

    # 5. Сохраняем в XML (normalized.xml)
    root = ET.Element("library")
    student_el = ET.SubElement(root, "student")
    student_el.set("name", STUDENT_NAME)
    student_el.set("token", TOKEN_HASH8)
    
    for book in books:
        book_el = ET.SubElement(root, "book")
        for key, val in book.items():
            child = ET.SubElement(book_el, key)
            child.text = str(val)
    
    tree = ET.ElementTree(root)
    tree.write("artifacts/day2/normalized.xml")

    # 6. Генерируем и сохраняем summary.json
    summary = {
        "status": "completed",
        "day": 2,
        "files_generated": ["normalized.json", "normalized.csv", "normalized.yaml", "normalized.xml"],
        "student": STUDENT_NAME
    }
    with open('artifacts/day2/summary.json', 'w') as f:
        json.dump(summary, f, indent=4)

    print("Success: All artifacts for Day 2 generated in artifacts/day2/")

if __name__ == "__main__":
    generate_data()