## Report

- **run_id**: live-1
- **recipe**: code_builder
- **outcome**: running
- **verdict**: 0/8 properties pass · 8/8 fail on the null
- **flagged_decisions**: D-0001, D-0002, D-0003, D-0004, D-0005, D-0006, D-0007, D-0008, D-0009, D-0010, D-0011, D-0012, D-0013, D-0014, D-0015, D-0016, D-0017, D-0018
- **halts**: 0
- **resumed**: 0

### carried

| kind | id | summary | from_step |
|---|---|---|---|
| finding | F-0002 | [major/contract_misread] `K-0001` states the slug must contain only `a-z, 0-9, and hyphens`, but `K-0002` leaves non-ASCII handling open and explicitly allows the tests to be "implement | plan round 2 |
| finding | F-0004 | [major/actionable] `A-0003` says to replace each non-alphanumeric character with a space, but it never defines whether "alphanumeric" is ASCII-only or Unicode-aware. In Python, `s | contract round 2 |
| finding | F-0009 | [major/actionable] C-0024 and C-0025 specify that TypeError should be raised with a message 'indicating type error'. However, P-0013's observe and falsifies fields test only that  | vspec round 2 |
| finding | F-0010 | [major/actionable] C-0021 requires that non-ASCII characters not be transliterated, and C-0013 restricts output to ASCII characters only. These constraints together require non-AS | vspec round 2 |
| property | P-0009 | missing:  | verify |
| property | P-0010 | missing:  | verify |
| property | P-0011 | missing:  | verify |
| property | P-0012 | missing:  | verify |
| property | P-0013 | missing:  | verify |
| property | P-0014 | missing:  | verify |
| property | P-0015 | missing:  | verify |
| property | P-0016 | missing:  | verify |

### waste

| side | calls | turns | tool_calls | refused_answers | input_tokens | output_tokens | seconds |
|---|---|---|---|---|---|---|---|
| author | 10 | 21 | 0 | 1 | 12569 | 75134 | 740.2900000000001 |
| checker | 10 | 10 | 0 | 1 | 155656 | 10726 | 180.73999999999998 |
