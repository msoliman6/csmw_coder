from slug import slugify


def _ascii_alnum_sequence(text: str) -> str:
    return "".join(ch for ch in text if ch.isascii() and ch.isalnum())


def _slug_alnum_sequence(text: str) -> str:
    return "".join(ch for ch in text if ch.isascii() and ch.isalnum())


def test_P_0004_non_string_inputs_raise_type_error():
    # falsifies: "slugify returns normally or raises a different exception type for any non-string input"
    for value in [None, 1, 1.5, object(), [], {}, b"abc"]:
        try:
            slugify(value)  # type: ignore[arg-type]
        except TypeError:
            continue
        except Exception as exc:  # pragma: no cover - explicit failure path
            raise AssertionError(f"expected TypeError for {value!r}, got {type(exc).__name__}") from exc
        else:
            raise AssertionError(f"expected TypeError for {value!r}")


def test_P_0005_allowed_character_set_only():
    # falsifies: "the output contains any character outside lowercase ASCII letters, digits, or hyphens"
    text = "Ab 1--c!"
    result = slugify(text)
    assert result, "expected a non-empty slug for an input with letters and digits"
    assert any(ch.isalnum() for ch in result), "expected output to account for the input's alphanumeric content"
    assert result == result.lower()
    assert all(ch.isascii() and (ch.islower() or ch.isdigit() or ch == "-") for ch in result)


def test_P_0006_asciialnum_order_is_preserved():
    # falsifies: "the output either introduces ASCII letters or digits not already present in the input’s ASCII alphanumeric order, or preserves the characters but not their relative order; either case would indicate transliteration or order corruption instead of removal"
    text = "aéb"
    result = slugify(text)
    expected = _ascii_alnum_sequence(text)
    observed = _slug_alnum_sequence(result)
    assert expected == "ab"
    assert observed == expected
