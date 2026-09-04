## Contract: core (v1)

### 1. Vocabulary

| id | key | term | definition |
|---|---|---|---|
| C-0001 | term_slug | slug | A URL-safe string containing only lowercase ASCII letters (a-z), digits (0-9), and hyphens (-) |

### 2.1 Input

| id | key | name | type | tags |
|---|---|---|---|---|
| C-0002 | input_text | text | str | required |

### 2.2 Output

| id | key | name | type | tags |
|---|---|---|---|---|
| C-0003 | output_slug | slug | str | ascii-only, lowercase |

### 2.3 Units

| id | key | name | kind | params | returns | holds |
|---|---|---|---|---|---|---|
| C-0004 | unit_slugify | slugify | function | text: str | str | Returns a URL-safe slug containing only lowercase ASCII letters, digits, and hyphens |

### 3. Constants

| id | key | name | value | tag |
|---|---|---|---|---|
| C-0005 | const_valid_characters | valid_characters | a-z, 0-9, - | format |

### 4. Invariants

| id | key | claim | measurement |
|---|---|---|---|
| C-0006 | inv_valid_characters_only | Output contains only lowercase ASCII letters (a-z), digits (0-9), and hyphens (-) |  |
| C-0007 | inv_order_preserved | Alphanumeric content from input appears in the output in the same relative order |  |

### 5. Negative scope

| id | key | must_not |
|---|---|---|
| C-0008 | neg_no_uppercase | Output contain any uppercase letters |
| C-0009 | neg_no_transliteration | Non-ASCII characters be transliterated to ASCII equivalents; they must be removed instead |

### 6. Failure policy

| id | key | on | policy | observable |
|---|---|---|---|---|
| C-0010 | fail_type_error | text parameter is not a string (including None) | raise TypeError | TypeError is raised when non-string input is passed to slugify() |

### 8. Algorithm

**unit_slugify**

- A-0001 `step_validate_type`: Raise TypeError if text is not a string -> implements fail_type_error
- A-0002 `step_remove_non_ascii`: Remove all non-ASCII characters from the text -> implements neg_no_transliteration, inv_valid_characters_only
- A-0003 `step_normalize_case`: Convert all ASCII letters to lowercase -> implements inv_valid_characters_only
- A-0004 `step_filter_characters`: Remove or process characters not in the valid character set, treating removed characters as word boundaries -> implements inv_valid_characters_only; uses const_valid_characters
- A-0005 `step_form_slug`: Arrange remaining alphanumeric sequences separated by hyphens while maintaining their original relative order -> implements inv_order_preserved, inv_valid_characters_only; uses const_valid_characters
- A-0006 `step_return`: Return the resulting slug -> implements
