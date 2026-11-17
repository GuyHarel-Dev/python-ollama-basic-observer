import json
import pandas as pd

log_dir = "data/log"
def test_write():
    
    record = {
        "prompt": "Hello",
        "response": "Hi! éééé bbb",
        "temperature": 0.7
    }

    lines = [record, record, record]
    with open(f"{log_dir}/test.jsonl", "a") as f:
        f.write(json.dumps(lines, ensure_ascii=False))
        

def test_read():
    df = pd.read_json(f"{log_dir}/test.jsonl", lines=True)
    print(df)
    
if __name__ == "__main__":
    test_read()
    