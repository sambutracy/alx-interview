#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys

# Dictionary to store the count of all status codes
status_count = {
    '200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
    '404': 0, '405': 0, '500': 0
}

total_file_size = 0
line_counter = 0  # Keep track of the number of lines processed

try:
    for log_line in sys.stdin:
        log_parts = log_line.split()

        if len(log_parts) > 6:
            http_status = log_parts[-2]
            file_size_str = log_parts[-1]

            # Check if the status code is in the dictionary and update count
            if http_status in status_count:
                status_count[http_status] += 1

            # Update total file size
            try:
                total_file_size += int(file_size_str)
            except ValueError:
                continue

            # Update line counter
            line_counter += 1

        if line_counter == 10:
            line_counter = 0  # Reset counter after 10 lines
            print('File size: {}'.format(total_file_size))

            # Print out status code counts
            for code in sorted(status_count.keys()):
                if status_count[code] != 0:
                    print('{}: {}'.format(code, status_count[code]))

except KeyboardInterrupt:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for code in sorted(status_count.keys()):
        if status_count[code] != 0:
            print('{}: {}'.format(code, status_count[code]))
