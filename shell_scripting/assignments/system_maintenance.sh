#!/bin/bash
#

pkg_update(){
    echo -e "Updating the installed packages...\n"
    apt update
    apt upgrade -y
    echo -e "Updating completed!\n"
}

cleanup() {
    echo -e "\nPerforming Cleanup Task\n"
    apt purge
    apt autoremove
    dpkg --list | grep linux-image | awk '{ print $2 }' | sort -V | sed -n '/'`uname -r`'/q;p' | xargs apt-get -y purge
    echo -e "\nCompleted Cleanup Task.\n"
}

timestamp=$(date +'%Y_%m_%d_%H_%M_%S')
log_file="system_maintenance_$timestamp.log"

if [[ ! -f "$log_file" ]]; then
        echo "$log_file does not exist. Creating $log_file."
        touch $log_file
else
        echo "$log_file already exist."
fi

pkg_update | tee -a $log_file
cleanup | tee -a  $log_file
