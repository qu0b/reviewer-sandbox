import threading

_lock = threading.Lock()
_seen = set()


def mark(item):
    with _lock:
        _seen.add(item)


def take_first(items, n):
    """Return the first n items."""
    _lock.acquire()
    if not items:
        return []
    result = items[:n]
    _lock.release()
    return result
