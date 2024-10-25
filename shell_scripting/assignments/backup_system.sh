#!/bin/bash
#
#1. Inputs are: -d--> directory, -c --> compression method, -r remoteHost
#2. Validate the directory, check if it exists, if not then show the error and exit.
#3. Check the correct compression mode is chosen(zip or tar), if yes then proceed else show the error and exit.
#4. Validate the IP, check if the IP is non empty(-n), if found empty, show error and exit.
#5. Exit.


display_usage(){

    echo "Usage: $0 [-d directory] [-c compression Method (zip| tar)] [-r remotehost]"
    exit 1
}

while getopts ":d:c:r:" opt; do
    case $opt in
        d) directory=$OPTARG ;;
        c) compression=$OPTARG ;;
        r) remotehost=$OPTARG ;;
        /?) display_usage ;;

    esac
done

#Validate the directory exist and valid.
if [[ -z "$directory" ]] || [[ ! -d "$directory" ]]; then
    echo "[ERROR]: Directory $directory does not exist or not specified."
    display_usage
fi

#validate if compression method passed is valid.
if [[ "$compression" != "zip" ]] && [[ "$compression" != "tar" ]]; then
    echo "[ERROR]: Compression method must be 'zip' or 'tar'."
    display_usage
fi

# Generate a timestamp
timestamp=$(date +'%Y_%m_%d_%H_%M_%S')

if [[ "$compression" == "zip" ]]; then
    archive_name="${directory}_${timestamp}.zip"
    zip -r "$archive_name" "$directory"
elif [[ "$compression" == "tar" ]]; then
    archive_name="${directory}_${timestamp}.tar.gz"
    tar -czvf "$archive_name" "$directory"
fi

# Check if compression was successful
if [[ $? -ne 0 ]]; then
    echo "[Error]: Compression failed."
    exit 1
fi

echo "Archive created: $archive_name"

# Transfer to a remote host using scp with the key from /home/ubuntu
if [[ -n "$remotehost" ]]; then
    ssh_key="/home/ubuntu/testing-keypair.pem"

    echo "Transferring the archive to remote host: $remotehost using key at $ssh_key"
    scp -i "$ssh_key" -o ConnectTimeout=10 "$archive_name" "ubuntu@${remotehost}:/home/ubuntu"

    if [[ $? -ne 0 ]]; then
        echo "[Error]: Failed to transfer the file."
        read -p "Do you want to remove the archive file $archive_name (y/N): " response
        response=${response,,}    # tolower
        if [[ "$response" =~ ^(yes|y)$ ]]; then
            echo "Removing the archive file."
            rm -rf $archive_name
        fi
        exit 1
    fi

    echo "Transfer successful."
    echo "Removing the archive file."
    rm -rf $archive_name
fi

echo "Backup process has completed successfully."
exit 0

