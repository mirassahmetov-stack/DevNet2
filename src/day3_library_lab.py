import os, json, hashlib
from pathlib import Path

def main():
    token = os.getenv("STUDENT_TOKEN", "D1-IB-23-5b-01-abcd")
    name = os.getenv("STUDENT_NAME", "Miras")
    group = os.getenv("STUDENT_GROUP", "IS31")
    th8 = hashlib.sha256(token.encode()).hexdigest()[:8]
    out = Path("artifacts/day3")
    out.mkdir(parents=True, exist_ok=True)
    summary = {
        "schema_version": "3.1",
        "student": {"token": token, "token_hash8": th8, "name": name, "group": group},
        "validation": {"must_have_added_100": True, "must_have_mybook_title_contains_token_hash8": True}
    }
    with open(out / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Готово! summary.json создан для {name}.")

if __name__ == "__main__":
    main()
