import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)

def list_tasks(tasks):
    return tasks

def main():
    tasks = load_tasks()
    tasks.add_task("playing")

    print(list_tasks(tasks))

if __name__ == "__main__":
    main()
