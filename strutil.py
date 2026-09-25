def truncate(text, width):
    """Return text cut to at most `width` characters, with an ellipsis if cut."""
    if width < 1:
        raise ValueError("width must be positive")
    if len(text) <= width:
        return text
    return text[: width - 1] + "…"
