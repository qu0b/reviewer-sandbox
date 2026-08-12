import threading

_lock = threading.Lock()
_box = {}


def store(key, value):
    with _lock:
        _box[key] = value


def fetch(key, loader):
    """Return the cached value, loading it on a miss."""
    _lock.acquire()
    if key in _box:
        value = _box[key]
        _lock.release()
        return value
    return loader(key)

# tweak
