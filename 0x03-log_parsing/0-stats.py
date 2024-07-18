#!/usr/bin/env python3
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
