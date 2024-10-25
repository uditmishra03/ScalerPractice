#!/bin/bash

log_file="/home/user/logs/log_file.log"
option="$1"


if [[ -e $log_file && -f $log_file ]]; then
        echo "$log_file exist, lets proceed"
else
        echo "$log_file does not exist, Exiting..."
        exit 0
fi

case $option in
    -h) 
        echo "Usage: $0 [-h] [-i] [log_file_path]

Analyze system logs to identify and summarize error messages.

Options:
-h Display this help message.
-i Interactive mode.
log_file_path Specify the path to the log file. Default is /var/log/syslog."
        ;;
    -i) 
        echo "Select the type of log analysis to perform:
1. Count Errors
2. List Errors
3. Search Errors"
        read -p "Enter your choice: " choice
        if [[ "$choice" == 1 ]]; then
            echo "Total number of errors: `cat $log_file | grep error | wc -l`"
        fi
        if [[ "$choice" == 2 ]]; then
                echo "List of unique error messages and their frequencies:"
                echo "`cat $log_file | grep ".error" |  awk '{$1=$2=$3="";print "error:" $0}' | sort -dr| uniq -c| sed 's/^[ \t]*//'| tr -s " "`"
				# grep -io 'error.*' $log_file | sort | uniq -c |tr -s " " | sed 's/^[ \t]*//'
        fi
        if [[ "$choice" == 3 ]]; then
                read -p "Enter a keyword to search for specific errors:" keyword
                echo "Searching for errors containing the keyword '$keyword':"
                echo "`cat $log_file | grep --color "$keyword"`"
        fi
        ;;
    *)
        echo "Invalid option! Try again."
        ;;
esac