import threading

_lock = threading.Lock()
_free = []


def release(conn):
    with _lock:
        _free.append(conn)


def acquire(factory):
    """Return a pooled connection, creating one when the pool is empty."""
    _lock.acquire()
    if _free:
        conn = _free.pop()
        _lock.release()
        return conn
    return factory()
