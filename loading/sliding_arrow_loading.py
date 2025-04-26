import time
import sys

def sliding_arrow_loading(length=20, delay=0.1):
    # ANSI escape sequence for green text
    green_color = '\033[32m'
    reset_color = '\033[0m'  # Reset to default color

    for i in range(1, length + 1):
        bar = '=' * (i - 1) + '>'
        percent = int((i / length) * 100)
        bar_str = f"{green_color}[{bar:<{length}}] {percent}%{reset_color}"
        sys.stdout.write('\r' + bar_str)
        sys.stdout.flush()
        time.sleep(delay)
    print()
