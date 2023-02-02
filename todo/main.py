import csv
import os.path
import tkinter as tk
from datetime import datetime

from task import Task
from messages import TASK_NAME_LABEL, ADD_BTN

window = tk.Tk()
window.title("Todo application")

width, height = 500, 500
window.geometry(f"{width}x{height}")

file_path = "tasks.csv"
def add():
    task = Task(name=task_entry.get(), created_at=datetime.now())

    with open(file_path, "a", newline="\n") as f:
        data = task.get_attrs_as_dict()
        header = ["id", "name", "created_at", "updated_at"]
        dict_writer = csv.DictWriter(f, header)
        if os.path.getsize(file_path) == 0:
            dict_writer.writeheader()
            data.update({"id": 1})
        csv_reader = csv.DictReader(f)
        
        dict_writer.writerow(task.get_attrs_as_dict())


task_name = tk.Label(window, text=TASK_NAME_LABEL)
task_name.place(x=10, y=10)

task_entry = tk.Entry(window, width=15)
task_entry.place(x=100, y=10)

add_btn = tk.Button(text=ADD_BTN, command=add)
add_btn.place(x=250, y=8)

if __name__ == "__main__":
    window.mainloop()