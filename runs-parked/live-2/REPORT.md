## Report

- **run_id**: live-2
- **recipe**: code_builder
- **outcome**: running
- **verdict**: 0/3 properties pass · 3/3 fail on the null
- **flagged_decisions**: D-0001, D-0002, D-0003, D-0004, D-0005, D-0006, D-0007, D-0008, D-0009, D-0010, D-0011, D-0012, D-0013, D-0014, D-0015
- **halts**: 0
- **resumed**: 0

### carried

| kind | id | summary | from_step |
|---|---|---|---|
| finding | F-0002 | [major/actionable] K-0001 still leaves the slug normalization contract underspecified even after the type check was clarified: the plan explicitly lists word-boundary detection, h | plan round 2 |
| finding | F-0004 | [major/actionable] P-0006's falsifying condition tests for transliteration and reordering but not for removal of ASCII alphanumerics. C-0007 requires 'Alphanumeric content from in | vspec round 2 |
| property | P-0004 | missing:  | verify |
| property | P-0005 | missing:  | verify |
| property | P-0006 | missing:  | verify |
| gap | C-0004 | clause not cited by any property | coverage |
| gap | C-0008 | clause not cited by any property | coverage |

### waste

| side | calls | turns | tool_calls | refused_answers | input_tokens | output_tokens | seconds |
|---|---|---|---|---|---|---|---|
| author | 8 | 18 | 0 | 1 | 22170 | 85520 | 741.29 |
| checker | 7 | 7 | 0 | 0 | 91777 | 4152 | 87.16 |
