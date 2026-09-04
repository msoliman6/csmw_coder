# src/slug.py
"""
Module slug: Convert text to URL-safe slugs.

Implements the slugify function that converts any text string into a URL-safe
slug containing only lowercase letters, digits, and hyphens.
"""

# Constants from section 3
VALID_SLUG_CHARSET = "abcdefghijklmnopqrstuvwxyz0123456789-"
HYPHEN = "-"
PYTHON_VERSION = "3.11"
MODULE_NAME = "slug"
FUNCTION_NAME = "slugify"


def slugify(text: str) -> str:
    """
    Convert text to a URL-safe slug.

    Args:
        text: The input string to convert to a slug

    Returns:
        A URL-safe slug containing only lowercase letters, digits, and hyphens

    Raises:
        TypeError: If text is None or not a string
    """

    # A-0008
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")

    # A-0009
    text = text.lower()

    # A-0010
    result = []
    for char in text:
        if char.isascii() and char.isalnum():
            result.append(char)
        else:
            result.append(' ')
    text = ''.join(result)

    # A-0011
    words = text.split()

    # A-0012
    slug = HYPHEN.join(words)

    # A-0013
    slug = slug.strip(HYPHEN)

    # A-0014
    for char in slug:
        if char not in VALID_SLUG_CHARSET:
            raise RuntimeError(f"Output verification failed: invalid character '{char}'")

    return slug
