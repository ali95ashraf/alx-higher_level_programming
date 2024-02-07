#!/usr/bin/python3
import sys
from collections import defaultdict

# Initialize variables to store metrics
total_file_size = 0
status_code_count = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        try:
            # Split the input line into its components
            _, _, _, _, _, status_code, file_size = line.strip().split(" ")

            # Update total file size
            total_file_size += int(file_size)

            # Update status code count
            status_code_count[status_code] += 1

            # Update line count
            line_count += 1

            # If 10 lines are processed, print statistics
            if line_count % 10 == 0:
                print("File size: {}".format(total_file_size))
                for code in sorted(status_code_count.keys()):
                    print("{}: {}".format(code, status_code_count[code]))
                print()

        except ValueError:
            # If the line does not match the expected format, skip it
            continue

except KeyboardInterrupt:
    # If interrupted by Ctrl+C, print final statistics
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_count.keys()):
        print("{}: {}".format(code, status_code_count[code]))
