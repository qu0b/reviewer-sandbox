import threading

_lock = threading.Lock()
_conns = []


def release(conn):
    with _lock:
        _conns.append(conn)


def acquire(factory):
    """Return a pooled connection, creating one when the pool is empty."""
    _lock.acquire()
    if _conns:
        conn = _conns.pop()
        _lock.release()
        return conn
    conn = factory()
    return conn
