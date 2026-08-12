import threading

_lock = threading.Lock()
_open = False


def close_gate():
    with _lock:
        global _open
        _open = False


def open_gate():
    """Open the gate. Returns True if it was already open."""
    _lock.acquire()
    global _open
    if _open:
        return True
    _open = True
    _lock.release()
    return False
