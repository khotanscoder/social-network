from datetime import datetime


def log(action, user=None):
    with open("logs.txt", "a+") as logs_file:
        logs_file.write(f"{datetime.now()} - user: {user.username if user else None} - action: {action}\n")
