# 🐚 Linux Shell Scripts Collection

## Project Overview

This repository contains a collection of Bash shell scripts designed to automate common system administration and utility tasks on Linux systems. The scripts focus on reliability, simplicity, and error handling, making them suitable for personal use or integration into larger automation workflows. All scripts are authored by Harsh Dev Jha and include features such as logging, timestamping, and user-friendly error messages.

---

## 📁 Contents

- 🔄 [A) Backup a Directory](#-a-backup-a-directory)
- 📊 [B) CPU & Memory Monitoring](#-b-cpu--memory-monitoring)
- 🌐 [C) Automated Download Task](#-c-automated-download-task)

---

## Instructions for Running the Scripts

### Prerequisites
- Ensure you have Bash installed on your Linux system (most distributions include it by default).
- Make the scripts executable by running `chmod +x <script_name>.sh` for each script.
- Ensure you have appropriate permissions to read/write to the directories used by the scripts (e.g., `/home/harsh/backup`, `/home/harsh/monitoring_logs`, `/home/harsh/downloads`).
- For the download script, `wget` must be installed (`sudo apt install wget` on Debian-based systems).

### General Usage
- Run scripts from the command line in a terminal.
- Provide required arguments as specified in each script's section.
- Scripts will output status messages to the console and may create log files.

---

## 🔄 A) Backup a Directory

**Description:**  
This script creates a timestamped backup of a specified directory, preserving its structure and contents. It recursively copies all files and subdirectories to a designated backup location.

**Features:**
- Automatically generates a backup folder name using the current date and time.
- Verifies the existence of the target directory before proceeding.
- Outputs success messages and the path to the backup folder.

**Usage:**
```bash
./Scripts/a_Backup_Directory.sh <target_directory>
```

**Example:**
```bash
./Scripts/a_Backup_Directory.sh /home/user/documents
```
This will create a backup in `/home/harsh/backup/directories/backup_YYYY-MM-DD_HH:MM:SS/`.

**Sample Output:**

<br>

<img width="817" height="583" alt="image" src="https://github.com/user-attachments/assets/4d87e98a-19aa-475c-a15e-6caf8e4e36ba" />


---

## 📊 B) CPU & Memory Monitoring

**Description:**  
This script continuously monitors and logs CPU and memory usage to a file at regular intervals. It runs indefinitely until manually stopped, making it ideal for long-term system monitoring.

**Features:**
- Logs timestamp, CPU usage percentage, and memory usage percentage.
- Uses a 5-second interval between log entries.
- Creates the log directory and file if they do not exist.
- Appends data to the log file in CSV format.
- Displays real-time logs on the console.

**Usage:**
```bash
./Scripts/b_Usage_Log.sh
```

**Example:**
Run the script in the background:
```bash
./Scripts/b_Usage_Log.sh &
```
Stop it by finding the process ID and using `kill <PID>`. Logs are saved to `/home/harsh/monitoring_logs/sys_monitoring.log`.

**Sample Output:**

<br>

<img width="1679" height="555" alt="image" src="https://github.com/user-attachments/assets/cf2f081f-e239-43cb-8f4b-c5ad52b1adf9" />


---

## 🌐 C) Automated Download Task

**Description:**  
This script automates the download of files from a specified URL using `wget`. It saves the file to a predefined directory and logs the outcome for tracking purposes.

**Features:**
- Extracts the filename from the URL automatically.
- Logs successful downloads and failures with timestamps.
- Provides console feedback on download status.

**Usage:**
```bash
./Scripts/c_Download_Automation.sh <target_url>
```

**Example:**
```bash
./Scripts/c_Download_Automation.sh https://example.com/file.zip
```
This will download `file.zip` to `/home/harsh/downloads/` and log the result to `/home/harsh/downloads/download_log.txt`.

**Sample Output:**

<br>

<img width="1919" height="1022" alt="image" src="https://github.com/user-attachments/assets/0990671c-3a64-4d1e-b83f-478ea8721d65" />


