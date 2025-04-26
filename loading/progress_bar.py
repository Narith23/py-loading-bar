import time
import sys

def loading_bar():
    bar_length = 40
    for i in range(bar_length + 1):
        percent = int(100 * i / bar_length)
        bar = '█' * i + '-' * (bar_length - i)
        sys.stdout.write(f'\r{bar} {percent}%')
        sys.stdout.flush()
        time.sleep(0.05)
    print()  # Move to the next line
