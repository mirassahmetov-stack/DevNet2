def token_hash8(token: str) -> str:
    # Берем SHA-256 от токена и возвращаем первые 8 символов
    return hashlib.sha256(token.encode("utf-8")).hexdigest()[:8]

def build_model(todo: dict, token: str, name: str, group: str) -> dict:
    title = todo["title"]
    return {
        "student": {
            "token": token,
            "token_hash8": token_hash8(token), # <--- Генерация хеша
            "name": name,
            "group": group,
        },
        # ... остальной код
    }
    import requests
from faker import Faker

fake = Faker()
# Твой токен/имя для фильтрации
MY_TOKEN = "akhmetov_is31" 

for i in range(4, 104):
    book_data = {
        "title": fake.catch_phrase(),
        "author": MY_TOKEN,  # Тот самый "маркер"
        "description": f"Book #{i}: {fake.text(max_nb_chars=100)}",
        "isbn": fake.isbn13()
    }
    
    # Отправка данных на сервер
    response = requests.post("http://<api-url>/books", json=book_data)
    
    if response.status_code == 201:
        print(f"Книга {i} успешно добавлена")