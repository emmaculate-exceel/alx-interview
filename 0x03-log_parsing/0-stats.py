#!/usr/bin/python3
""" Log parsing program for stdin """


import sys
import signal
import collections
import re


# initilizing variables to store metrics
file_size = 0
line_count = 0
status_code = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}


def handle_sig(sig, interface):
    """ handling signal interuption """
    print_statistic()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_sig)


def parse_line(line):
    """ parsing the line of """
    global status_code, line_count, file_size
    line_count = +1
    pattern = r'^\S+ - \[[^\]]+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'

    match = re.match(pattern, line)
    if match:
        status_code = int(match.group(1))
        file_s = int(match.group(2))

        if status in status_code:
            status_code[status] += 1

        file_size += file_s


def print_statistic():
    """ this function print sys.stdin line statistic """
    print(f"Total file size: {total_size}")
    for code in sorted(status_code.keys()):
        if status_code[code] > 0:
            print(f"{code}: {status_code[code]}")


def main():
    """ main function """
    global line_count

    for line in sys.stdin:
        line = line.strip()

        if line:
            parse_line(line)

        if line_count % 10 == 0:
            print_statistic()

    print_statistics()
