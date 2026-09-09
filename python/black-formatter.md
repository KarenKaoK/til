# Black Formatter

Today I learned about **Black**, a Python code formatter.

Before I knew about Black, I formatted code manually, line by line. For example, I had to decide where to break long function arguments into multiple lines and how to adjust indentation.

Black can format code automatically based on its own consistent rules, so the same code will be formatted in the same way every time.

It mostly follows PEP 8 conventions, but it also has some of its own rules. For example, Black uses a default line length of 88 characters.

The commands I use most often are:

```
# Format a file
black app.py

# Check formatting without changing files
black --check .

# Preview formatting changes without changing files
black --diff --check .

```

Official documentation:\
[Black](https://black.readthedocs.io/en/stable/index.html)