# TODO решите задачу
import json
INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE) as f:
        json_data = json.load(f)

        list_multiplication = [round(item["score"] * item["weight"], 3) for item in json_data]
        return sum(list_multiplication)

print(task())
