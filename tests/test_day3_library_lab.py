import os, pytest, json
from pathlib import Path
def test_simple_check():
    assert os.getenv("STUDENT_TOKEN") is not None
    assert Path("artifacts/day3/summary.json").exists()
