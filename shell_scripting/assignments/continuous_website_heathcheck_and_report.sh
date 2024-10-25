#!/bin/bash
#
logFile='/home/user/logfile.log'
website_health_log='/home/user/error_reports/website_health.log'
website_report_log='/home/user/error_reports/website_report.log'

create_Report(){
        report_time="Error Report - $(date)"
        total_errors="Total Errors: $(grep -c "ERROR" $website_health_log)"
        latest_error="Latest Error: $(tail -1 $website_health_log)"
        echo -e "$report_time \n$total_errors \n$latest_error"

}

while true; do
    tail -f $logFile | egrep --line-buffered -i 'ERROR' >> $website_health_log
    create_Report >> $website_report_log
    echo '' >> $website_report_log

    sleep 5
done