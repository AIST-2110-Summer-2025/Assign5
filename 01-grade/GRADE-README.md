# Grade Calculator

We are revisiting this exercise from last time. The basic operation remains
unchanged. But you are going to add input validation to make sure the program
cannot blow up.

This program will help you determine your grade for a quiz. Simply provide the
number of questions, how many you got right. The program will then calculate the
score as a percent and assign a letter grade. The letter grade will be based on
the following table:

| Score   | Grade |
|:-------:|:-----:|
| >= 90%  |   A   |
| >= 80%  |   B   |
| >= 70%  |   C   |
| >= 60%  |   D   |
|  < 60%  |   F   |

## Inputs

Prompt the user to enter the following information:

- Total number of questions (int)
- Number of correct answers (int)

## Input Validation

If ANY of the validation checks fails, then print `INVALID INPUT` and exit
immediately.

- Both numbers must currectly convert to ints
- Number of questions must be between 1 and 100 (inclusive)
- Number correct must be between 0 and the total number of questions (inclusive)

## Expected Output

> NOTE: Expected output is unchanged EXCEPT that you are formatting the grade to
> exactly 1 decimal place.

- You should calculate and print the score and letter grade in the format:

  `CORRECT out of TOTAL is SCORE% (LETTER)`

  > _Remember that the score will be correct divided by total. But that to get
  > the percent formatted correctly you must also multiply this by 100._

  GRADE should be displayed with exactly one decimal place.

- Examples:

    - If you enter `10` for total and `10` for correct, the program should print:

      `10 out of 10 is 100.0% (A)`

    - If you enter `20` for total and `16` for correct, the program should print:

      `16 out of 20 is 80.0% (B)`

    - If you enter `12` for total and `9` for correct, the program should print:

      `9 out of 12 is 75.0% (C)`

    - If you enter `13` for total and `8` for correct, the program should print:

      `8 out of 13 is 61.5% (D)`

    - If you enter `5` for total and `0` for correct, the program should print:

      `0 out of 5 is 0.0% (F)`

## This Program Now Stinks _Less_

Input validation really helped! And string formatting makes thing much prettier.
But we can do better. We'll likely revisit this one again in a future
assignment, so do your best to get this version solid.

## Source
- Adapted from PY4E
