def words(text):
    """Split text on whitespace into a list of words."""
    return text.split()


def lines(text):
    """Split text into lines without trailing newlines."""
    return text.splitlines()


def first_word(text):
    """Return the first whitespace-separated word, or an empty string."""
    parts = text.split()
    return parts[0] if parts else ""


def last_word(text):
    """Return the last whitespace-separated word, or an empty string."""
    parts = text.split()
    return parts[-1] if parts else ""
