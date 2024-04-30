import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        planned_task_text.insert(tk.END, task + "\n")
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        start_idx = "sel.first linestart"
        end_idx = "sel.last lineend + 1c"
        planned_task_text.delete(start_idx, end_idx)
    except:
        pass
    try:
        start_idx = "sel.first linestart"
        end_idx = "sel.last lineend + 1c"
        completed_task_text.delete(start_idx, end_idx)
    except:
        pass

def mark_task():
    try:
        start_idx = "sel.first linestart"
        end_idx = "sel.last lineend"
        task = planned_task_text.get(start_idx, end_idx)
        planned_task_text.delete(start_idx, end_idx + "+1c")
        completed_task_text.insert(tk.END, task + "\n")
    except:
        pass

root = tk.Tk()
root.title("Task Tracker")
root.configure(background="black")

text1 = tk.Label(root, text="Опишите задачу:", bg="black", fg="chartreuse")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=70, bg="chartreuse", fg="black")
task_entry.pack(pady=10)

# Фрейм для кнопок
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Добавить", bg="chartreuse2", fg="black", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Удалить", bg="chartreuse2", fg="black", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

mark_button = tk.Button(button_frame, text="Выполнить", bg="chartreuse2", fg="black", command=mark_task)
mark_button.pack(side=tk.LEFT, padx=5)

# Фреймы для текстовых виджетов
left_frame = tk.Frame(root, bg="black")
left_frame.pack(side=tk.LEFT, padx=20, pady=10)
right_frame = tk.Frame(root, bg="black")
right_frame.pack(side=tk.RIGHT, padx=20, pady=10)

# Запланированные задачи
text2 = tk.Label(left_frame, text="Запланированные", bg="black", fg="chartreuse")
text2.pack(pady=5)
planned_task_text = tk.Text(left_frame, height=15, width=40, bg="DarkOrchid", fg="chartreuse", wrap=tk.WORD)
planned_task_text.pack(pady=10)

# Выполненные задачи
text3 = tk.Label(right_frame, text="Выполненные", bg="black", fg="chartreuse")
text3.pack(pady=5)
completed_task_text = tk.Text(right_frame, height=15, width=40, bg="DarkOrchid", fg="chartreuse", wrap=tk.WORD)
completed_task_text.pack(pady=10)

root.mainloop()