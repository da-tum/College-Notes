#!/bin/bash 
# Author: Harsh Dev Jha
# Date: 13/11/25 

# --- Script to automate downloads --- 
# check if target url argument is provided 

if [ -z "$1" ]; then 
echo "Usage: $0 <target_url>" 
exit 1 # exit with an error status of 1 , abnormal termination 
fi 

# Initialise the file URL with the first argument 
url="$1" 

# Predefined directory for downloads 
download_dir="/home/harsh/downloads" 

# Log file 
log_file="/home/harsh/downloads/download_log.txt" 

# Create directory if it doesn’t exist 
mkdir -p "$download_dir" 

# Extract filename from URL 
filename=$(basename "$url") 

# Download using wget 
echo "Downloading $filename ..." 
wget -q -O "$download_dir/$filename" "$url" 

# Check if download was successful 
if [ $? -eq 0 ]; then 
echo "Download successful: $download_dir/$filename" 
echo "$(date): Downloaded $filename from $url" >> "$log_file" 
else 
echo "Download failed!" 
echo "$(date): Failed to download from $url" >> "$log_file" 
fi 