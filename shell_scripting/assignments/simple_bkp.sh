#!/bin/bash

# Function to display usage information
usage() {
    echo "Usage: $0 [-d directory] [-c compression (zip|tar)] [-r remote_host]"
    exit 1
}

# Parse options
while getopts ":d:c:r:" opt; do
  case $opt in
    d) directory=$OPTARG ;;
    c) compression=$OPTARG ;;
    r) remote_host=$OPTARG ;;
    \?) usage ;;
  esac
done

# Check if directory is specified and exists
if [[ -z "$directory" ]] || [[ ! -d "$directory" ]]; then
    echo "Error: Directory is not specified or does not exist."
    usage
fi

# Validate compression method
if [[ "$compression" != "zip" ]] && [[ "$compression" != "tar" ]]; then
    echo "Error: Compression method must be 'zip' or 'tar'."
    usage
fi

# Generate a timestamp
timestamp=$(date +'%Y-%m-%d_%H-%M-%S')

# Set filename based on the chosen compression method
if [[ "$compression" == "zip" ]]; then
    archive_name="${directory}_${timestamp}.zip"
    # Compress directory with zip
    zip -r "$archive_name" "$directory"
elif [[ "$compression" == "tar" ]]; then
    archive_name="${directory}_${timestamp}.tar.gz"
    # Compress directory with tar
    tar -czvf "$archive_name" "$directory"
fi

# Check if compression was successful
if [[ $? -ne 0 ]]; then
    echo "Error: Compression failed."
    exit 1
fi

echo "Archive created: $archive_name"

# Optional: Transfer to a remote host using scp with the key from /home/ubuntu
if [[ -n "$remote_host" ]]; then
    ssh_key="/home/ubuntu/testing-keypair.pem"

    echo "Transferring archive to remote host: $remote_host using key at $ssh_key"
    scp -i "$ssh_key" "$archive_name" "$remote_host:/home/ubuntu"

    if [[ $? -ne 0 ]]; then
        echo "Error: Failed to transfer the file."
        exit 1
    fi
    echo "Transfer successful."
fi

echo "Backup process completed successfully."
exit 0
