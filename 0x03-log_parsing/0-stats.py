#!/usr/bin/python3
"""This module parses a log from stdin and computes metrics."""

import sys


def print_statistics(total_size, status_counts):
    """Prints the total file size and status code counts.

    Args:
        total_size (int): Total file size accumulated.
        status_counts (dict): Dictionary with counts of status codes.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 2:
            try:
                status_code = parts[-2]
                file_size = int(parts[-1])

                if status_code in status_counts:
                    status_counts[status_code] += 1

                total_size += file_size
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_counts)

            except ValueError:
                continue

finally:
    print_statistics(total_size, status_counts)
