# tasks.py

# تغییر ساختار: به جای لیست، از دیکشنری استفاده می‌کنیم
# کلید = ID، مقدار = دیکشنریِ مشخصاتِ تسک
tasks = {
    1: {"title": "Finish German Final", "status": "pending"},
    2: {"title": "Setup GitHub Repository", "status": "completed"}
}

def add_task(title):
    # پیدا کردن ID بعدی (بیشترین ID موجود + ۱)
    new_id = max(tasks.keys()) + 1 if tasks else 1
    tasks[new_id] = {"title": title, "status": "pending"}
    print(f"Task '{title}' added with ID: {new_id}")

def list_tasks():
    print("\n--- Current Task List ---")
    for task_id, info in tasks.items():
        print(f"[{task_id}] {info['title']} - Status: {info['status']}")
    print("--------------------------\n")

def complete_task(task_id):
    # اینجا جادویِ O(1) اتفاق می‌افتد
    if task_id in tasks:
        tasks[task_id]['status'] = "completed"
        print(f"Task {task_id} marked as completed.")
    else:
        print(f"Task with ID {task_id} not found!")

if __name__ == "__main__":
    list_tasks()
    add_task("Learn SOLID principles")
    complete_task(1)
    list_tasks()