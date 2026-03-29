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