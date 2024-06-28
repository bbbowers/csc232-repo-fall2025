# Input/Output Patterns : Python

(Adapted from https://mwermelinger.github.io/kattis-guide/input.html)

Competitive programming problems require data to be read from *standard input*, and  results to be written to *standard output*. There are different ways to handle the input, depending on the set up of the problem. Most challenge/contest problems fall into one of the following categories. For each category, I'll go over an example problem.



## No input, only output

Without input, all you need is the `print()` function to write to standard output.

- [Hello World!](https://open.kattis.com/problems/hello):
The classic first program. It doesn't get easier than this, and yet over
[40% of the submissions failed](https://open.kattis.com/problems/hello/statistics)!
A sobering reminder than even the most trivial problem demands
attention to details and checking before submitting.

    [Code video](https://youtu.be/2Q-wW0Eb4ds)



## Fixed number of lines (one or more); One datum per line

Problems in this category have a fixed (i.e. always the same) number of lines, given in the problem description, and each line has a single datum, e.g. one number, or one word.

To read a single line from the standard input, use `input()`, which returns a
string. If a string represents a number, use function `int()` or `float()` to
convert it to an integer or floating-point number.

For example, if the problem consists of reading 3 floats from the input, one per line, and produce the smallest of them, the solution would be:
```py
print(min(float(input()), float(input()), float(input())))
```

- [Simple Addition](https://open.kattis.com/problems/simpleaddition):
Add two large integers. Trivial in Python.
    
    [Code video](https://youtu.be/r2ZqgI4ReLk)

- [Time Loop](https://open.kattis.com/problems/timeloop): An example where the input is always one line with one number, but the output is multiple lines.

    [Code video](https://youtu.be/mI5xpG3posw)



## Fixed number of lines; Multiple data per line

In this category, the number of input lines is fixed but some lines may
contain more than one number or string, usually separated by spaces.

For these problems, use the string method `split()` to separate the input line
into a *list* of strings. If the data is separated by anything other than spaces,
give the separator (e.g. `','`) as an argument to `split()`.

For example, if the input is a single line of space-separated integers and the
output is the sum of those integers, one solution is:

```py
total = 0
for number in input().split():
    total += int(number)
print(total)
```

To convert the list from strings to integers all in one go, use `map`:

```py
total = 0
for number in map(int, input().split()):
    total += number
print(total)
```

With comprehensions, a one-line solution is:
```py
print(sum(int(number) for number in input().split()))
```

If the number of items per line is fixed, you can use Python's *tuple assignment* to assign them directly to variables:

```py
(a, b, c) = input().split()  # if the line always has exactly 3 pieces of data
```

- [Moscow Dream](https://open.kattis.com/problems/moscowdream): Always a single line of input with 4 numbers on it.

    [Code video](https://youtu.be/Ii1PizqrEwA)

- [Solving for Carrots](https://open.kattis.com/problems/carrots):
A silly description of a trivial problem that makes
an excellent introduction to ignoring irrelevant details.



## _n_ lines

These problems have a variable number _n_ of lines, but _n_ is given at the
start of the input, and so the lines can be read with a for-loop.

Consider the sum example again, but this time, each integer is on its line, and the first line is the number of lines that follow.
The solution becomes:
```py
total = 0
for _ in range(int(input())):   # can use name _ if the variable isn't needed
    total += int(input())
print(total)
```

- [Oddities](https://open.kattis.com/problems/oddities): Demonstrates the input techniques so far as well as the use of `str()` to explicitly convert data to a string when necessary. 

    [Code video]()



## End marker on input

These problems have a variable number of lines, and their number is unknown at
the start. Instead, there is a marker (also known as a *sentinel* value) signalling the end of input. Processing such inputs requires a repeat-until loop, using a `while` statement.

Imagine the sum example has one integer per line and the last integer is zero.
The solution becomes:

```py
total = 0
number = int(input())
while number != 0:
    total += number
    number = int(input())
print(total)
```

To avoid having to repeat the `input()`, you can use an infinite loop with a `break`:

```py
```py
total = 0
while True:
    number = int(input())
    if number == 0: break   # jumps out of the loop
    total += number
print(total)
```

- [Left Beehind](https://open.kattis.com/problems/leftbeehind):
Make a decision based on two integers.
The input has two integers per line, terminating with two zeros.

    [Code video]()



## Input until end of file

In these problems, there's no extra information at the start or end of the input. You are just supposed to read lines of input until there are no more. If each test case consists of a single line, the most straightforward approach is to loop
over each line of the standard input, which is accessed directly using `sys.stdin`.

Using our running example, if the input is one integer per line
and all integers are to be added, the solution becomes:

```py
from sys import stdin

total = 0
for line in stdin:
    total += int(line)
print(total)
```

or:
```py
from sys import stdin

print(sum(int(line) for line in stdin))
```

When running and testing such code interactively using keyboard input, use the `Ctrl`+`D` key combination on Mac OS X, or `Ctrl`+`Z` followed by `Enter` on Windows, to indicate "end of input." 

NB: The `input()` function returns a string without a newline at the end, but
the lines obtained by iterating over `stdin` do include a newline.
The newline character is removed or ignored by `split()`, `int()` and `float()`,
but for some problems you may need to remove it explicitly with the `rstrip()`
method, which removes all whitespace from the right end of a string.

See the *Statistics* problem under the next section for an example of this style of input.



## Formatted output

Some problems require the output to be formatted in a particular way,
e.g. without a space between values, or with a certain number of digits after the decimal point.

If spaces do not separate output items, or you don't want a new line to start after each `print` statement, you can use `print(..., end='')`. Alternatively, you could use string concatenation to construct the entire output string first and then use a single `print` to write it out. 

However, often an easier way to cope with much of output formatting is to use Python's [f-strings](https://realpython.com/python-f-strings/).

- [Statistics](https://open.kattis.com/problems/statistics):
Compute the maximum, minimum and range of the given values.
One test case per line. Write the case number to the output.

    [Code video]()



## Fast I/O

Some problems have an immense number of lines of inputs or outputs. You may get a 'Time Limit Exceeded' error. In those cases, use `stdin.readline()` instead of `input()` and `stdout.write()` instead of `print()`.

The `readline()` function returns the empty string on the end of input.

The `write()` function takes a string to be written as-is.
You must write all spaces and newlines yourself,
and convert data to strings using the function `str()`.

Here's a final example:
```py
from sys import stdin, stdout

total = 0
line = stdin.readline()
while line:                 # same as while line != '':
    total += int(line)
    line = stdin.readline()
stdout.write(str(total))
stdout.write('\n')
```

- [CD](https://open.kattis.com/problems/cd):
  Given two collections of CDs, which are duplicate? Also demonstrates how it is sometimes necessary (and can be very frustrating) to figure out implicit specifications in the problem description that are not entirely obvious in the given test case(s).

    [Code video]()


