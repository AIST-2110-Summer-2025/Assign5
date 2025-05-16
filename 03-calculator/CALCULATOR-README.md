# Basic RPN Calculator

Back when electronic calculators first came out, there was debate on how best to
perform calculations. The familiar "1 + 1 =" (num operator num go) and a
competing "1 1 +" (num num operator). The first obviously won out in terms of
popularity, but the second is still a thing. It's called Reverse Polish Notation
or RPN.

In this exercise, you'll implement a basic RPN calculator. Why RPN? Well because:

- it's more logical from a programming perspective (you need the two values
  before you can add/subtract/multipl/divide them), and
- it's fun to shake things up a bit.

## Inputs

Prompt the user to enter the following information:

- Enter the first number (float)
- Enter the second number (float)
- Enter the operator ( + , - , x , / )

## Input Validation

If ANY of the validation checks fails, then print `INVALID NUMBER` or 'INVALID
OPERATOR' and exit immediately.

- Both numbers must currectly convert to float
- The operator must be `+`, `-`, `x`, or `/`
   + Note `x`, not `*` since we're talking to normal humans

## Expected Output

This one is pretty easy. Simply display the full calculation in the form:

`{num1} {operator} {num2} = {result}`

Note the spaces between each part. For example:

`1.0 + 1.0 = 2.0`

> _**NOTE:** removing that trailing `.0` in Python in a relaible way is pretty
> tricky without doing addtional work outside of the f-string.  So we won't try.
> Yet. Just use f-strings without supplying any additional format
> specifications._

**IMPORTANT**: Use the `round()` function to round both numbers **and** the
result to at most 4 decimal places. Make sure to round the two inputs sometime
before you do the calculations.

### Special Case : Division by Zero

If the user enters `0` for the second number and `/` for the operator, then
obviously you'll get an exception. Use exception handling for this one scenario.
Set the anser to `ERROR` when you catch this exception. For example:

`8.0 / 0.0 = ERROR`


## Input + Output Examples

| number 1 | number 2 | operator | output
|:--------:|:--------:|:--------:|-------------------
| 5        | 6        | +        | 5.0 + 6.0 = 11
| 10       | 2        | /        | 10.0 / 2.0 = 5.0
| 5        | 6        | x        | 5.0 x 6.0 = 30.0
| 1.1      | .2       | -        | 1.1 - 0.2 = 0.9
| 3.0      | 2.0      | +        | 3.0 + 2.0 = 5.0
| 4        | 3        | /        | 4.0 / 3.0 = 1.3333
| 2.02468  | 2.00000  | /        | 2.0247 / 2.0 = 1.0124
| -4       | 3        | x        | -4.0 x 3.0 = -12.0
| 8        | -10      | +        | 8.0 + -10.0 = -2.0
| -6.6     | -3       | /        | -6.6 / -3 = 2.2
| 4        | 0        | x        | 4.0 * 0.0 = 0.0
| 4        | 0        | /        | 4.0 / 0.0 = ERROR
| ten      |          |          | INVALID NUMBER
| 10       | two      |          | INVALID NUMBER
| 3.5      | 2.0      | *        | INVALID OPERATOR
| 175      | 232      | times    | INVALID OPERATOR
