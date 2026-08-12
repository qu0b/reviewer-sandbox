import threading

_lock = threading.Lock()
_items = []


def put(item):
    with _lock:
        _items.append(item)


def take():
    """Pop the next item, or None when the queue is empty."""
    _lock.acquire()
    if not _items:
        return None
    item = _items.pop(0)
    _lock.release()
    return item
