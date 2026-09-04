## Contract: ## Contract: Contract: The slug module implementing the slugify(text: str) -> str function that converts any text string into a URL-safe slug containing only lowercase letters, digits, and hyphens. (v1) (v2) (v3)

### 1. Vocabulary

| id | key | term | definition |
|---|---|---|---|
| C-0001 | slug_term | slug | A URL-safe identifier composed of lowercase letters (a-z), digits (0-9), and hyphens, used as the output of the slugify function |
| C-0002 | word_term | word | A maximal sequence of alphanumeric characters separated by whitespace or special characters |
| C-0003 | word_boundary_term | word boundary | A location in text where words are separated by whitespace or non-alphanumeric characters |
| C-0004 | separator_term | separator | Whitespace or non-alphanumeric characters that act as word boundaries and are converted to hyphens in output |

### 2.1 Input

| id | key | name | type | tags |
|---|---|---|---|---|
| C-0005 | text_param | text | str | required, main_input |

### 2.2 Output

| id | key | name | type | tags |
|---|---|---|---|---|
| C-0006 | slug_result | slug | str | main_output |

### 2.3 Units

| id | key | name | kind | params | returns | holds |
|---|---|---|---|---|---|---|
| C-0007 | slugify_func | slugify | function | text: str | str | Returns a URL-safe string containing only lowercase letters, digits, and hyphens, with words in original order and no leading or trailing hyphens |

### 3. Constants

| id | key | name | value | tag |
|---|---|---|---|---|
| C-0008 | valid_charset_const | VALID_SLUG_CHARSET | "abcdefghijklmnopqrstuvwxyz0123456789-" | format |
| C-0009 | hyphen_char_const | HYPHEN | "-" | format |
| C-0010 | python_version_const | PYTHON_VERSION | "3.11" | limit |
| C-0011 | module_name_const | MODULE_NAME | "slug" | format |
| C-0012 | function_name_const | FUNCTION_NAME | "slugify" | format |

### 4. Invariants

| id | key | claim | measurement |
|---|---|---|---|
| C-0013 | inv_output_charset | Output contains only characters from VALID_SLUG_CHARSET: lowercase a-z, digits 0-9, and hyphen |  |
| C-0014 | inv_word_order | Words in output appear in the same relative order as they appear in input |  |
| C-0015 | inv_lowercase_only | All alphabetic characters in output are lowercase (a-z), never uppercase (A-Z) |  |
| C-0016 | inv_no_leading_hyphen | Output does not begin with a hyphen character |  |
| C-0017 | inv_no_trailing_hyphen | Output does not end with a hyphen character |  |
| C-0018 | inv_no_consecutive_hyphens | Output does not contain consecutive hyphen characters (no -- substrings) |  |
| C-0019 | inv_whitespace_separates | Whitespace characters in input act as word boundaries and separate words with hyphens in output |  |
| C-0020 | inv_punctuation_removed | Non-alphanumeric characters and punctuation marks do not appear in output (except hyphen) |  |
| C-0021 | inv_no_transliteration | Non-ASCII input characters are not transliterated or converted to ASCII equivalents |  |

### 5. Negative scope

| id | key | must_not |
|---|---|---|
| C-0022 | neg_no_external_deps | Import or depend on third-party packages; only Python standard library is used |
| C-0023 | neg_no_transliteration | Implement transliteration logic that converts non-ASCII characters to ASCII substitutes |

### 6. Failure policy

| id | key | on | policy | observable |
|---|---|---|---|---|
| C-0024 | fail_none_input | Input argument is None | Raise TypeError | TypeError exception is raised with message indicating type error |
| C-0025 | fail_non_string_input | Input argument is not a string type (int, list, dict, etc.) | Raise TypeError | TypeError exception is raised with message indicating type error |

### 8. Algorithm

**slugify_func**

- A-0008 `A-0001`: Validate that input is a string type; raise TypeError if input is None or not a string -> implements fail_none_input, fail_non_string_input
- A-0009 `A-0002`: Convert input string to lowercase using standard string case conversion -> implements inv_lowercase_only
- A-0010 `A-0003`: Replace each non-alphanumeric character with a space to identify word boundaries; non-ASCII characters are removed or converted to separators without transliteration -> implements inv_punctuation_removed, inv_no_transliteration
- A-0011 `A-0004`: Split the processed string on whitespace characters to extract individual words -> implements inv_whitespace_separates
- A-0012 `A-0005`: Join non-empty words with single hyphen separators, maintaining word order from input -> implements inv_word_order, inv_no_consecutive_hyphens; uses hyphen_char_const, valid_charset_const
- A-0013 `A-0006`: Remove any leading or trailing hyphen characters from the result string -> implements inv_no_leading_hyphen, inv_no_trailing_hyphen; uses hyphen_char_const
- A-0014 `A-0007`: Verify that all characters in output conform to VALID_SLUG_CHARSET -> implements inv_output_charset; uses valid_charset_const

### 10. Retired

A-0001, A-0002, A-0003, A-0004, A-0005, A-0006, A-0007
