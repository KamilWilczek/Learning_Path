import os
import datetime

BASE_DIR = os.path.dirname(__file__)
log_dir = os.path.join(BASE_DIR, "logs")
os.makedirs(log_dir, exist_ok=True)


def trigger_log_save():
    # filename = f'{datetime.datetime.now()}.txt' - nie działa format na windowsie
    filename = f'{datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")}.txt'
    filepath = os.path.join(log_dir, filename)
    with open(filepath, "w+") as f:
        f.write("")
