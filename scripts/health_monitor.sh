#!/bin/bash

CPU_THRESHOLD=80
MEM_THRESHOLD=80
DISK_THRESHOLD=80

CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
MEM_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
DISK_USAGE=$(df -h / | grep / | awk '{ print $5 }' | sed 's/%//g')

if (( $(echo "$CPU_USAGE > $CPU_THRESHOLD" | bc -l) )); then
  echo "CPU usage is above $CPU_THRESHOLD%: Current usage: $CPU_USAGE%" | tee -a /var/log/sys_health.log
fi

if (( $(echo "$MEM_USAGE > $MEM_THRESHOLD" | bc -l) )); then
  echo "Memory usage is above $MEM_THRESHOLD%: Current usage: $MEM_USAGE%" | tee -a /var/log/sys_health.log
fi

if (( $DISK_USAGE > $DISK_THRESHOLD )); then
  echo "Disk usage is above $DISK_THRESHOLD%: Current usage: $DISK_USAGE%" | tee -a /var/log/sys_health.log
fi

