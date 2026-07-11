# 📘 Chapter 8 – Comments in Python

<div align="center">

# 💬 Comments in Python

### "Write code for computers, but comments for humans."

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What are Comments?
- Why Do We Need Comments?
- Types of Comments
- Single-Line Comments
- Multi-Line Comments
- Docstrings
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Questions
- Cheat Sheet
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Understand what comments are

✅ Write single-line and multi-line comments

✅ Understand docstrings

✅ Know when to use comments

✅ Write clean and readable code

---

# 🤔 What are Comments?

A **Comment** is a note written inside your code.

It is written **for humans**, not for Python.

Python completely ignores comments while running the program.

---

# 🌍 Real-Life Example

Imagine you buy a new book.

You use a sticky note to write:

```
Read this chapter before exam.
```

The sticky note is **for you**, not part of the book.

Similarly,

Comments are notes for programmers.

---

# Why Do We Need Comments?

Comments help us to

- Explain code
- Remember logic
- Make code easy to understand
- Help teammates understand our program
- Debug programs

---

# 🌍 Another Real-Life Example

Imagine a road.

Without signboards

```
❌ Confusing
```

With signboards

```
➡ Airport

⬅ Railway Station

⬆ City Center
```

Travel becomes easier.

Comments are like **road signs** for your code.

---

# Types of Comments

Python supports

1. Single-Line Comments
2. Multi-Line Comments
3. Docstrings

---

# 1️⃣ Single-Line Comments

Single-line comments start with

```python
#
```

Everything after `#` is ignored by Python.

---

# Example

```python
# This program prints Hello World

print("Hello World")
```

Output

```
Hello World
```

---

# Another Example

```python
# Store age
age = 20

# Print age
print(age)
```

Output

```
20
```

---

# Inline Comments

Comments can also be written at the end of a line.

```python
age = 20  # Student's age

print(age)
```

Output

```
20
```

---

# 2️⃣ Multi-Line Comments

Python does not have a special syntax for multi-line comments.

Most programmers use multiple `#` symbols.

Example

```python
# This program
# calculates the
# area of a rectangle

length = 10
width = 5

print(length * width)
```

---

# Another Way

Some programmers use triple quotes.

```python
"""
This is a
multi-line comment.
"""
```

Technically, this is a **multi-line string**, not a true comment.

If it is not assigned to a variable, Python ignores it.

---

# 3️⃣ Docstrings

A **Docstring** is used to explain

- Functions
- Classes
- Modules

It is written using triple quotes.

---

# Example

```python
def greet():
    """
    This function prints
    a welcome message.
    """
    print("Welcome!")

greet()
```

Output

```
Welcome!
```

---

# Why are Docstrings Important?

They help other programmers understand

- What a function does
- What parameters it takes
- What it returns

Professional Python projects use docstrings everywhere.

---

# 🌍 Real-Life Example

Imagine buying a medicine.

The medicine packet contains

```
Uses

Dosage

Side Effects
```

This information helps users.

Similarly,

Docstrings explain how code should be used.

---

# Best Practices

## ✅ Write Meaningful Comments

Bad

```python
# Variable

age = 20
```

Good

```python
# Store student's age

age = 20
```

---

## ✅ Explain Why, Not What

Bad

```python
# Increase x by 1

x = x + 1
```

Good

```python
# Increase score after correct answer

score += 1
```

---

## ✅ Keep Comments Updated

If code changes,

update the comments too.

Wrong comments are worse than no comments.

---

## ✅ Use Docstrings for Functions

```python
def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b
```

---

# When Should You Use Comments?

Use comments when

- Explaining complex logic
- Describing functions
- Giving important notes
- Warning about special cases

---

# When Should You Avoid Comments?

Avoid comments for obvious code.

Bad

```python
# Print Hello

print("Hello")
```

The code is already clear.

---

# Common Mistakes

## Mistake 1

Writing unnecessary comments.

```python
# Create variable

age = 20
```

Not needed.

---

## Mistake 2

Writing outdated comments.

```python
# Age is 18

age = 20
```

Comment is incorrect.

---

## Mistake 3

Using comments instead of meaningful variable names.

Bad

```python
# Student age

x = 20
```

Better

```python
student_age = 20
```

---

# Interview Questions

### Q1. What is a comment?

### Q2. Why do we use comments?

### Q3. What is the difference between comments and docstrings?

### Q4. Does Python execute comments?

### Q5. Which symbol is used for single-line comments?

### Q6. What are docstrings used for?

---

# Practice Questions

## Easy

1. Write a program with a single-line comment.

2. Add inline comments.

3. Write a multi-line comment.

4. Create a function with a docstring.

---

## Medium

Create a calculator program.

Add comments explaining

- Input
- Calculation
- Output

---

# Cheat Sheet

```python
# Single-line comment

print("Hello")

# Multi-line comment

# Line 1
# Line 2
# Line 3

"""
Docstring Example
"""

def greet():
    """
    Prints a welcome message.
    """
    print("Welcome!")
```

---

# Summary

✅ Comments are ignored by Python.

✅ Comments help humans understand code.

✅ Single-line comments use `#`.

✅ Multi-line comments are usually written using multiple `#`.

✅ Docstrings explain functions, classes, and modules.

✅ Good comments explain **why**, not **what**.

---

# Mini Assignment

Create a Python program that

- Stores your name, age, and city
- Uses single-line comments
- Uses inline comments
- Creates a function with a docstring
- Prints all the information

Example Output

```
Name : Rahul
Age  : 20
City : Indore
```

---

# 🎉 Congratulations!

You have completed **Chapter 8 – Comments in Python**.

You now know how to write clean, readable, and well-documented Python code. Good commenting habits will help you in team projects, open-source contributions, and technical interviews.