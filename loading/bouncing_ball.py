def bouncing_ball(duration=3):
    line = [' '] * 20
    ball = '●'
    direction = 1
    pos = 0
    import time
    end_time = time.time() + duration

    while time.time() < end_time:
        line[pos] = ' '
        pos += direction
        if pos == 0 or pos == len(line) - 1:
            direction *= -1
        line[pos] = ball
        import sys
        sys.stdout.write('\r' + ''.join(line))
        sys.stdout.flush()
        time.sleep(0.05)
    print()
