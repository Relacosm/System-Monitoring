import psutil
import time

def log_system_usage(interval):
    while True:
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        print(f'CPU: {cpu}%, Memory: {memory}%')
        time.sleep(interval)

log_system_usage(5)