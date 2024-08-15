#!/usr/bin/python3
"""
Reads from stdin, parses logs, and computes metrics:
- Total file size.
- Count of specific HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500).
Prints stats every 10 lines or on keyboard interruption.
"""

import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints total file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) > 6:
            status_code = parts[-2]
            file_size = parts[-1]

            try:
                total_size += int(file_size)
            except ValueError:
                continue

            try:
                if int(status_code) in status_codes:
                    status_codes[int(status_code)] += 1
            except ValueError:
                continue

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
