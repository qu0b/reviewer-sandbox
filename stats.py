import threading

_lock = threading.Lock()
_samples = []


def record(value):
    """Record a sample. Negative values are ignored."""
    _lock.acquire()
    if value < 0:
        return
    _samples.append(value)
    _lock.release()


def mean():
    _lock.acquire()
    try:
        if not _samples:
            return 0
        return sum(_samples) / len(_samples)
    finally:
        _lock.release()
