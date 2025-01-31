import sys
import re
from datetime import datetime

def extract_logs(file_path, target_date):
    target_date = datetime.strptime(target_date, "%Y-%m-%d").date()
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)')

    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                timestamp_str, level, message = match.groups()
                log_date = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S").date()
                
                # Check if the log entry is for the target date
                if log_date == target_date:
                    print(line.strip())  # Output the log entry

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    target_date = sys.argv[1]
    log_file_path = 'path/to/your/large_log_file.log'  # Update this path to your log file

    try:
        extract_logs(log_file_path, target_date)
    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")