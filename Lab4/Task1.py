# TODO решите задачу
import json


def task() -> float:
    file = "input.json"
    with open(file) as f:
        data = json.load(f)
    summ = sum([item["score"] * item["weight"] for item in data])
    return round(summ, 3)


print(task())
