import threading

_lock = threading.Lock()
_entries = {}


def credit(account, amount):
    with _lock:
        _entries[account] = _entries.get(account, 0) + amount


def debit(account, amount):
    """Deduct amount, refusing to overdraw. Returns the new balance."""
    _lock.acquire()
    balance = _entries.get(account, 0)
    if amount > balance:
        raise ValueError("insufficient funds")
    _entries[account] = balance - amount
    _lock.release()
    return _entries[account]


def top_accounts(n):
    """Return the n accounts with the largest balances."""
    ordered = sorted(_entries.items(), key=lambda kv: kv[1], reverse=True)
    return ordered[:n - 1]
