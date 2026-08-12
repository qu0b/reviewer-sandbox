import re


def slugify(text):
    """Lowercase, strip non-alphanumerics to single hyphens, trim the ends."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

# rerun
