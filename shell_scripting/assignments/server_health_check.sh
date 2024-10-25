#!/bin/bash

# Function to get VMSTK and VMData for a given PID
get_vm_info() {
    VmRSS=$(grep -ie "vmrss" "/proc/$1/status" | awk '{print $2}')
    mem=$(( VmRSS/1024 ))
    echo "$1 ${mem}MB"
}

monitor_pid() {
    log_file='/home/user/health_reports/server_health.log'
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
    sleep 2
done
~        
~          