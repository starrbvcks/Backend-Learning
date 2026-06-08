# tasks.py

# دیتابیسِ حافظه-محورِ ما
tasks = [
    {"id": 1, "title": "Finish German Final", "status": "pending"},
    {"id": 2, "title": "Setup GitHub Repository", "status": "completed"}
]

def add_task(title):
    """اضافه کردن یک تسک جدید با شناسه داینامیک"""
    new_id = len(tasks) + 1
    new_task = {"id": new_id, "title": title, "status": "pending"}
    tasks.append(new_task)
    print(f"Task '{title}' added with ID: {new_id}")

def list_tasks():
    """نمایش تمام تسک‌ها در خروجی"""
    print("\n--- Current Task List ---")
    for task in tasks:
        print(f"[{task['id']}] {task['title']} - Status: {task['status']}")
    print("--------------------------\n")

def complete_task(task_id):
    """تغییر وضعیت تسک به انجام شده"""
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "completed"
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task with ID {task_id} not found!")

# اجرایِ تستِ اولیه
if __name__ == "__main__":
    list_tasks()
    add_task("Learn SOLID principles")
    complete_task(1)
    list_tasks()