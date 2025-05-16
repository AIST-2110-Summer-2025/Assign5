# Leap Year

A **leap year** is a year with 366 days instead of the usual 365, with the extra
day added to February. Leap years exist to keep our calendar in sync with the
Earth's orbit around the Sun, which takes _approximately_ 365.25 days.

To correct for the extra 0.25 days, one extra day is added to years that are
*evenly divisible by 4*...i.e., one extra day every 4 years. However, there’s an
exception: a year *evenly divisible by 100* is not a leap year _**unless**_ it
is also *evenly divisible by 400*. This system ensures our calendar remains
accurate over time.

In this exercise, you will write a program to determine if a given year is a leap year. 

Your task is to prompt the user for a year and print whether it is a leap year or not.

Only accept years greater than `0`. If the user enters a value less than or
equal to 0 or if the value cannot be converted to an `int`, then print `INVALID
YEAR`.

## _Pseudocode_

Since this is your first nested-if problem, let me give you the basic program
flow. This is "pseudocode", or simply the logical program flow written in
plain(ish) English instead of Python.

I've placed this code in comments in the Python script file. It may be helpful
to place put the actual Python code below each bit of pseudocode.

```
as the user to enter a year

if the year isn't greater than 0 or can't be converted to int
    display 'INVALID YEAR' and exit

if the year is not evenly divisible by 4
    display '{year} is not a leap year'
otherwise (i.e., it IS divible by 4)
    if the year is not evenly divisible by 100
        display '{year} is a leap year'
    otherwise (i.e., it IS divisible by 100)
        if the year is divisible by 400 then
            display '{year} is a leap year'
        otherwise (i.e., the year is NOT divisible by 400)
            display '{year} is not a leap year'
```

> _**IMPORTANT NOTE**: there are other ways to do this, but **please** follow
> the above logic and program flow. Partly because I'm pretty confident ChatGPT
> isn't going to give you a solution structured like this. But mostly because it
> reinforces the use of nested if statements._

## Expected Output

When you run your program, the console should display the following text based
on the input provided:

- If you enter `2000`, your program should output: `2000 is a leap year.`
- If you enter `2020`, your program should output: `2020 is a leap year.`
- If you enter `2011`, your program should output: `2011 is not a leap year.`
- If you enter `1800`, your program should output: `1800 is not a leap year.`
- If you enter `0`, your program should output: `INVALID YEAR`
- If you enter `-100`, your program should output: `INVALID YEAR`
- If you enter `jaguar`, your program should output: `INVALID YEAR`

## Hints
  - Recall that the modulo operator (`%`) returns the remainder when one number is
    divided by another. You can use this for many of your above conditionals. For
    example:
    ```
    if value % 3 == 0:
        print(f'{value} is evenly divisible by 3')
    ```
