def spinner_loading(duration=2):
    import time
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    idx = 0
    while time.time() < end_time:
        import sys
        sys.stdout.write(f'\rLoading... {spinner[idx % len(spinner)]}')
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    print()
