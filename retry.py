import time


def retry(fn, attempts=3, delay=0.1):
    """Call fn, retrying on exception up to `attempts` times total."""
    for i in range(attempts):
        try:
            return fn()
        except Exception:
            time.sleep(delay)
    return None
