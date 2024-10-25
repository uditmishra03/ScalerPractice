#!/bin/bash

alert_log='/home/user/health_reports/alert.log'
log_file='/home/user/health_reports/server_health.log'

# Function to get VMRSS for a given PID
get_vm_info() {
    VmRSS=$(grep -ie "vmrss" "/proc/$1/status" | awk '{print $2}')
    mem=$(( VmRSS/1024 ))
    if [[ "$mem" -ge 20 ]]; then
        echo "$1 ${mem}MB" >> $alert_log
    else
         echo "$1 ${mem}MB"
    fi
}

monitor_pid() {
    # Get all PIDs from ps aux
    pids=$(ps haux | awk '{print $2}')

    # Iterate over each PID and log the information
    for pid in $pids; do
        ps -p $pid &> /dev/null
        if [[ "$?" -eq 0 ]]; then
            info=$(get_vm_info $pid)
            echo "$info" >> $log_file
        fi
    done
}

# Continuously monitor and log process information every 2 seconds
while true; do
    monitor_pid
    sleep 5
done