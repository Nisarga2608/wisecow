import psutil

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

cpu_usage = psutil.cpu_percent(interval=1)
mem_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

if cpu_usage > CPU_THRESHOLD:
    print(f"CPU usage is above {CPU_THRESHOLD}%: Current usage: {cpu_usage}%")
    with open("/var/log/sys_health.log", "a") as log_file:
        log_file.write(f"CPU usage is above {CPU_THRESHOLD}%: Current usage: {cpu_usage}%\n")

if mem_usage > MEM_THRESHOLD:
    print(f"Memory usage is above {MEM_THRESHOLD}%: Current usage: {mem_usage}%")
    with open("/var/log/sys_health.log", "a") as log_file:
        log_file.write(f"Memory usage is above {MEM_THRESHOLD}%: Current usage: {mem_usage}%\n")

if disk_usage > DISK_THRESHOLD:
    print(f"Disk usage is above {DISK_THRESHOLD}%: Current usage: {disk_usage}%")
    with open("/var/log/sys_health.log", "a") as log_file:
        log_file.write(f"Disk usage is above {DISK_THRESHOLD}%: Current usage: {disk_usage}%\n")

