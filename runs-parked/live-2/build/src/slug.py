"""URL slug generation module."""

# C-0005: Define valid_characters constant
valid_characters = set('abcdefghijklmnopqrstuvwxyz0123456789-')


def slugify(text: str) -> str:
    """
    Convert text into a URL-safe slug.
    
    A slug contains only lowercase ASCII letters (a-z), digits (0-9), and hyphens (-).
    
    Args:
        text: The input text to convert into a slug.
        
    Returns:
        A URL-safe slug string.
        
    Raises:
        TypeError: If text is not a string.
    """
    # A-0001: step_validate_type
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")
    
    # A-0002: step_remove_non_ascii
    ascii_text = ''.join(char for char in text if ord(char) < 128)
    
    # A-0003: step_normalize_case
    lowercase_text = ascii_text.lower()
    
    # A-0004: step_filter_characters
    # Replace invalid characters with spaces (treating them as word boundaries)
    filtered = ''
    for char in lowercase_text:
        if char in valid_characters:
            filtered += char
        else:
            filtered += ' '
    
    # A-0005: step_form_slug
    # Split on spaces to get word sequences, then join with hyphens
    words = filtered.split()
    slug = '-'.join(words)
    
    # A-0006: step_return
    return slug
