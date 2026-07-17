# tests/test_json_utils.py
from utils.json_utils import extract_json

def test_extract_json_with_markdown():
    # 1. Arrange 
    raw_text = "Here is the output: ```json {\"district\": \"Colombo\"} ```"
    
    # 2. Act 
    result = extract_json(raw_text)
    
    # 3. Assert 
    assert result == "{\"district\": \"Colombo\"}"

def test_extract_json_no_json():
   
    raw_text = "Just a normal text message"
    result = extract_json(raw_text)
    
    assert result is None