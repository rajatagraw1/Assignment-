import psutil
import logging
from datetime import datetime, time

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80.0  # percent
MEMORY_THRESHOLD = 80.0  # percent
DISK_THRESHOLD = 80.0  # percent
PROCESS_COUNT_THRESHOLD = 300  # example threshold for the number of running processes

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert(f"High memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        alert(f"High disk usage detected: {disk_usage}%")
    return disk_usage

def check_running_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        alert(f"High number of running processes detected: {process_count}")
    return process_count

def alert(message):
    print(message)
    logging.info(message)

def main():
    print("Starting system health monitoring...")
    while True:
        cpu = check_cpu_usage()
        memory = check_memory_usage()
        disk = check_disk_usage()
        processes = check_running_processes()

        print(f"CPU Usage: {cpu}%")
        print(f"Memory Usage: {memory}%")
        print(f"Disk Usage: {disk}%")
        print(f"Running Processes: {processes}")

        print("Monitoring... Press Ctrl+C to stop.")
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()

