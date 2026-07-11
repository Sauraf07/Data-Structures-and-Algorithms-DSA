

# 🖥️ Chapter 3 - Your First Python Program

> "Every expert programmer once wrote their first program."

---

# 📚 Table of Contents

- What is a Program?
- What is Source Code?
- What is Code?
- Understanding the print() Function
- Writing Your First Python Program
- Running Your Program
- How Python Executes Your Code
- Understanding Errors
- Types of Errors
- Multiple print() Statements
- Printing Numbers
- Printing Strings
- Printing Special Characters
- Escape Sequences
- Comments
- Real-Life Examples
- Practice Questions
- Mini Assignment
- Interview Questions
- Summary

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

✅ Write your first Python program

✅ Run a Python file

✅ Understand how Python works

✅ Use the print() function

✅ Understand comments

✅ Understand errors

---

# 🤔 What is a Program?

A **program** is simply a collection of instructions given to a computer.

Think of it like a recipe.

---

## 🌍 Real-Life Example

Imagine your mother gives you these instructions:

```
1. Wash the rice
2. Add water
3. Put it in the cooker
4. Turn the cooker on
5. Wait for 15 minutes
```

These are instructions.

Similarly,

A computer also needs instructions.

Those instructions together form a **Program**.

---

# 💻 What is Code?

The instructions we write are called **Code**.

Example

```python
print("Hello World")
```

This single line is called **code**.

Many lines together become a **program**.

---

# 📄 What is Source Code?

The file in which we write our Python code is called the **Source Code**.

Example

```
hello.py
```

The `.py` extension tells the computer:

> "This is a Python file."

---

# 🐍 Your First Python Program

Create a new file.

```
hello.py
```

Write:

```python
print("Hello World")
```

Save the file.

Run it.

Output:

```
Hello World
```

🎉 Congratulations!

You have written your first Python program.

---

# 🧠 Understanding print()

The most commonly used function in Python is:

```python
print()
```

It displays information on the screen.

---

## Real-Life Example

Imagine a teacher writing on the classroom board.

Students can see it.

Similarly,

```
print()
```

shows information on the computer screen.

---

# Syntax

```python
print("Anything")
```

---

# Example 1

```python
print("Hello")
```

Output

```
Hello
```

---

# Example 2

```python
print("Python")
```

Output

```
Python
```

---

# Example 3

```python
print("I love programming")
```

Output

```
I love programming
```

---

# What Happens Internally?

Let's understand step by step.

You write:

```python
print("Hello")
```

↓

Python reads the code.

↓

Python understands it.

↓

Python sends the text to the screen.

↓

You see

```
Hello
```

---

## Diagram

```
You

↓

Write Code

↓

Python Interpreter

↓

Computer

↓

Output Screen
```

---

# What is an Interpreter?

Python is an **Interpreted Language**.

It reads your code

One line

↓

Executes it

↓

Moves to the next line.

---

## Real-Life Example

Imagine a translator.

You speak English.

Your friend understands Japanese.

The translator listens

↓

Converts

↓

Speaks Japanese.

Similarly,

Python Interpreter converts your code into machine language.

---

# Another Example

```python
print("Apple")
print("Banana")
print("Orange")
```

Output

```
Apple
Banana
Orange
```

Python executes one line at a time.

---

# Multiple print() Statements

You can use print many times.

Example

```python
print("Python")
print("Java")
print("C++")
```

Output

```
Python
Java
C++
```

---

# Printing Numbers

You can print numbers too.

```python
print(10)
```

Output

```
10
```

---

```python
print(100)
```

Output

```
100
```

---

```python
print(3.14)
```

Output

```
3.14
```

---

# Printing Text

Text must be inside quotes.

Correct

```python
print("Python")
```

Wrong

```python
print(Python)
```

This gives an error because Python thinks `Python` is a variable.

---

# Single Quotes vs Double Quotes

Both are correct.

```python
print("Hello")
```

```python
print('Hello')
```

Output

```
Hello
```

---

# Printing Special Characters

Suppose you write

```python
print("I'm learning Python")
```

Python becomes confused because the apostrophe closes the string.

Correct way:

```python
print("I'm learning Python")
```

or

```python
print('I\\'m learning Python')
```

---

# Escape Sequences

Escape sequences allow special formatting.

---

## New Line

```python
print("Hello\nWorld")
```

Output

```
Hello
World
```

---

## Tab Space

```python
print("Python\tJava\tC++")
```

Output

```
Python    Java    C++
```

---

## Double Quote

```python
print("He said \"Hello\"")
```

Output

```
He said "Hello"
```

---

## Backslash

```python
print("C:\\Users\\Boss")
```

Output

```
C:\Users\Boss
```

---

# Comments

Comments are notes written for humans.

Python ignores them.

---

Example

```python
# This is my first program

print("Hello")
```

Output

```
Hello
```

The comment is ignored.

---

# Why Use Comments?

Imagine reading a book.

The chapter title tells you what the chapter is about.

Similarly,

Comments explain your code.

---

Example

```python
# Print Welcome Message

print("Welcome")
```

---

# Common Beginner Mistakes

❌ Forgetting quotes

```python
print(Hello)
```

---

❌ Missing bracket

```python
print("Hello"
```

---

❌ Wrong spelling

```python
prit("Hello")
```

Correct

```python
print("Hello")
```

---

# Types of Errors

## Syntax Error

Wrong grammar.

Example

```python
print("Hello"
```

---

## Name Error

Using something that doesn't exist.

```python
print(name)
```

---

## Indentation Error

Wrong spacing.

```python
if True:
print("Hello")
```

Python requires indentation.

---

# Real-Life Example

Imagine giving your address.

Correct

```
House 10

Street 5

City
```

Wrong

```
House

City

Street
```

The delivery person gets confused.

Similarly,

Computers need properly written instructions.

---

# Interview Questions

### Q1

What is a program?

---

### Q2

What is source code?

---

### Q3

What does print() do?

---

### Q4

What is an interpreter?

---

### Q5

Difference between Compiler and Interpreter?

---

### Q6

Why are comments useful?

---

### Q7

Difference between single and double quotes?

---

# Practice Questions

### Easy

1. Print your name.

2. Print your age.

3. Print your city.

4. Print your college name.

5. Print your favorite programming language.

---

### Medium

6.

```
Python

Java

C++
```

---

7.

```
*****
```

---

8.

```
Hello

World
```

using `\n`

---

9.

Print

```
He said "Python is awesome"
```

---

10.

Print

```
C:\Users\Boss\Desktop
```

---

# Mini Assignment

Create a Python file called

```
introduction.py
```

Print the following:

```
My Name is ______

I am learning Python.

I want to become an AI Engineer.

Python is fun.
```

Add comments before every print statement.

---

# Cheat Sheet

```python
print("Hello")

print(100)

print(3.14)

print('Hello')

print("Hello\nWorld")

print("Python\tJava")

print("He said \"Hi\"")

print("C:\\Users\\Boss")

# This is a comment
```

---

# 📝 Chapter Summary

✅ A program is a collection of instructions.

✅ Code is written in a source file (`.py`).

✅ `print()` displays output on the screen.

✅ Python executes code line by line using an interpreter.

✅ Strings should be inside quotes.

✅ Escape sequences help format output.

✅ Comments improve readability and are ignored by Python.

🎉 Excellent! You have now written and understood your first Python programs. In the next chapter, we'll dive into **Variables**, where you'll learn how computers store and remember information.
