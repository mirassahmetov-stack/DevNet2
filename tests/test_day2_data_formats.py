import pytest
import json
import os
from pathlib import Path

def test_artifacts_exist():
    """Проверяем, что все 8 файлов на месте"""
    base_path = Path("artifacts/day2")
    required_files = [
        "conflict_log.txt", "git_log.txt", "pr_link.txt",
        "normalized.json", "normalized.yaml", "normalized.xml", 
        "normalized.csv", "summary.json"
    ]
    for file_name in required_files:
        assert (base_path / file_name).exists(), f"Файл {file_name} не найден!"

def test_summary_content():
    """Проверяем содержимое summary.json"""
    with open("artifacts/day2/summary.json", "r") as f:
        data = json.load(f)
    
    assert data["student"]["name"] == "Akhmetov Miras"
    assert data["student"]["group"] == "ib-23-5b"
    assert "outputs" in data