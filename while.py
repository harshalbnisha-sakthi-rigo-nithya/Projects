import time
from datetime import datetime


def task():
    with open("while_sd.txt", "a") as f:
        f.write(f"Script ran at: {datetime.now()}\n")
    print(f"Task ran at: {datetime.now()}\n")

while True:
    task()
    time.sleep(10)