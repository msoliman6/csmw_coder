from slug import slugify


def test_P_0009_charset():
    # falsifies: any uppercase letter, underscore, space, or other disallowed character appears in the result, or the result is not a string
    text = "Hello123"
    result = slugify(text)
    assert isinstance(result, str)
    assert result != text
    assert result
    assert all(ch in "abcdefghijklmnopqrstuvwxyz0123456789-" for ch in result)
    assert result.lower() == result


def test_P_0010_no_edge_or_double_hyphens():
    # falsifies: the result begins with '-', ends with '-', or contains '--'
    text = "...hello world..."
    result = slugify(text)
    assert isinstance(result, str)
    assert result
    assert "hello" in result and "world" in result
    assert not result.startswith("-")
    assert not result.endswith("-")
    assert "--" not in result


def test_P_0011_preserves_word_order():
    # falsifies: word groups appear out of order, merge incorrectly, or are separated by anything other than single hyphens
    text = "red   green\tblue"
    result = slugify(text)
    assert result == "red-green-blue"


def test_P_0012_removes_punctuation_and_symbols():
    # falsifies: any punctuation mark, symbol, or whitespace survives in the slug
    cases = [
        ("rock&roll, 24/7!", ["rock", "roll", "24", "7"]),
        ("email@example.com", ["email", "example", "com"]),
        ("go+fast#now", ["go", "fast", "now"]),
    ]
    for text, expected_words in cases:
        result = slugify(text)
        assert isinstance(result, str)
        assert result
        for word in expected_words:
            assert word in result
        assert all(ch.islower() or ch.isdigit() or ch == "-" for ch in result)
        assert all(ch not in result for ch in " !@#$%^&*()_+=[]{}|;:'\",.<>/?\\")


def test_P_0013_non_string_inputs_raise_typeerror():
    # falsifies: the call returns normally or raises a different exception type
    for value in [None, 1, [], {}]:
        try:
            slugify(value)  # type: ignore[arg-type]
        except TypeError:
            pass
        else:
            raise AssertionError(f"slugify({value!r}) did not raise TypeError")


def test_P_0014_no_ascii_transliteration_of_non_ascii():
    # falsifies: a non-ASCII character is converted into an ASCII spelling equivalent rather than being removed or otherwise not transliterated
    text = "naïve approach"
    result = slugify(text)
    assert isinstance(result, str)
    assert result
    assert "approach" in result
    assert "naive" not in result
    assert "ï" not in result
    assert all(ord(ch) < 128 for ch in result)
    assert all(ch in "abcdefghijklmnopqrstuvwxyz0123456789-" for ch in result)


def test_P_0015_stable_and_no_extra_separator_artifacts():
    # falsifies: two calls on the same input produce different strings, or repeated separators create malformed hyphen runs
    text = "alpha   -- beta \t\t gamma"
    first = slugify(text)
    second = slugify(text)
    assert first == second
    assert first == "alpha-beta-gamma"
    assert "--" not in first


def test_P_0016_valid_charset_for_simple_token():
    # falsifies: the output contains characters outside of abcdefghijklmnopqrstuvwxyz0123456789- or is not a string
    text = "token123"
    result = slugify(text)
    assert isinstance(result, str)
    assert result == "token123"
    assert all(ch in "abcdefghijklmnopqrstuvwxyz0123456789-" for ch in result)
