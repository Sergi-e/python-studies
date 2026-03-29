# Console Task Manager
# Concepts used:
# - dictionaries
# - functions (add/update/delete/view)
# - exception handling
# - string normalization
# - validation

def add_task(tasks, task_pair):
    name, status = task_pair
    name = name.lower()
    status = status.lower()
    
    if name in tasks:
        return f"Task '{name}' already exists."
    
    if status not in ["pending", "done"]:
        return "Status must be 'pending' or 'done'."

    tasks[name] = status
    return f"Task '{name}' added with status '{status}'."

def update_task(tasks, task_pair):
    name, status = task_pair
    name = name.lower()
    status = status.lower()
    
    if name not in tasks:
        return f"Task '{name}' does not exist."
    
    if status not in ["pending", "done"]:
        return "Status must be 'pending' or 'done'."

    tasks[name] = status
    return f"Task '{name}' updated to '{status}'."

def delete_task(tasks, name):
    name = name.lower()
    
    if name in tasks:
        del tasks[name]
        return f"Task '{name}' deleted."
    
    return "Task not found."