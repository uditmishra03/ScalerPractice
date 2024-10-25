#!/bin/bash
#
prepare_system_report(){
    timestamp=$(date +'%Y_%m_%d_%H_%M_%S')
    echo "$timestamp:: System Health Report"
    echo -e "Uptime: $(uptime)"
    echo -e "CPU and Memory Usage: "
    total_idle=$(mpstat -P ALL | grep 'all' | awk '{print $12}')
    echo "100 - $total_idle" | bc -l
    echo "$(free -h | grep 'Mem' | awk '{print $3}')"
    echo "Disk Usage:"
    echo "$(df -h)"
    echo "Recently Installed Security Patches"
    echo "$(apt list --installed)" 

}

test_email_delivery() {
    recipient="janedoe"
    mailbox_path="/var/mail/$recipient"
    echo "Running Test 3: Email Delivery Check..."

    if [ -f "$mailbox_path" ]; then
        keywords=("System Health Report" "Uptime" "CPU and Memory Usage" "Disk Usage")
    
        if grep -q "System Health Report" "$mailbox_path"; then
            echo "PASS: Email containing the system health report was sent to $recipient."
    
            for keyword in "${keywords[@]}"; do
                if grep -q "$keyword" "$mailbox_path"; then
				    echo "PASS: Email contains the keyword '$keyword'."
                else
                    echo "FAIL: Email is missing the keyword '$keyword'."
                fi
            done
        else
            echo "FAIL: No system health report email found in $mailbox_path."
        fi
    else
        echo "FAIL: Mailbox for $recipient does not exist."
    fi
}

send_email() {
    recipient="janedoe"
    
    # Send the email using mailx or sendmail
    if [ -f "$system_report" ]; then
        echo "Sending system health report to $recipient..."
        cat "$system_report" | mail -s "System Health Report" "$recipient"
        echo "Email sent."
    else
        echo "Error: Report file $system_report does not exist."
        exit 1
    fi
}

system_report='/var/log/system_health_report.html'
if [[ -f $system_report ]]; then

        echo "$system_report exists. Continue."
		prepare_system_report > $system_report  # Generate report
        send_email                              # Send the email
        test_email_delivery                     # Check if email was delivered
else
        echo "[ERROR]: $system_report does not exists. Continue."
        exit 1
fi