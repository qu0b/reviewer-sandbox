import threading

_lock = threading.Lock()
_entries = {}


def put(key, value):
    with _lock:
        _entries[key] = value


def get_or_load(key, loader):
    """Return the cached value for key, loading and caching it on a miss."""
    _lock.acquire()
    if key in _entries:
        value = _entries[key]
        _lock.release()
        return value
    value = loader(key)
    _entries[key] = value
    return value
