#!/usr/bin/python3
"""Module containing a script that reads stdin line by line and computes,
metrics
Each 10 lines and after a keyboard interruption (CTRL + C), prints those,
statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""


import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
i = 0
try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            a = i
            if tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
                i += 1
            try:
                file_size += int(tokens[-1])
                if a == i:
                    i += 1
            except Exception:
                if a == i:
                    continue
        if i % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
