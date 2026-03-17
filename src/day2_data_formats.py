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