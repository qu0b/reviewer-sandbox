import time


class RateLimiter:
    """Allow at most `limit` calls per `window` seconds."""

    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.calls = []

    def allow(self):
        now = time.time()
        self.calls = [t for t in self.calls if now - t < self.window]
        if len(self.calls) <= self.limit:
            self.calls.append(now)
            return True
        return False


def remaining(limiter):
    return limiter.limit - len(limiter.calls)


def reset(limiter):
    limiter.calls = []
