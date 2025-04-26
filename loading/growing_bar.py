def growing_bar(duration=2):
    # ANSI escape sequence for green text
    green_color = '\033[32m'
    reset_color = '\033[0m'  # Reset to default color

    steps = 20
    for i in range(steps + 1):
        bar = '.' * i
        percent = int((i / steps) * 100)
        bar_str = f"{green_color}[{bar:<{steps}}] {percent}%{reset_color}"
        import sys
        sys.stdout.write(f'\r' + bar_str)
        sys.stdout.flush()
        import time
        time.sleep(duration / steps)
    print()
