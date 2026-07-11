# 📘 Chapter 6 – Input and Output in Python

<div align="center">

# ⌨️ Input & 🖥️ Output in Python

### "A program becomes useful when it can communicate with the user."

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What is Input?
- What is Output?
- Why Input and Output are Important?
- print() Function
- input() Function
- Taking Integer Input
- Taking Float Input
- Taking Multiple Inputs
- Formatting Output
- Common Mistakes
- Interview Questions
- Practice Questions
- Cheat Sheet
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Display output using `print()`

✅ Take user input using `input()`

✅ Convert input into Integer and Float

✅ Take multiple inputs

✅ Format output professionally

---

# 🤔 What is Output?

Output means

> **Displaying information to the user.**

Whenever a program shows something on the screen, it is called **Output**.

---

# 🌍 Real-Life Example

Imagine an ATM.

You insert your card.

The ATM displays

```
Welcome
Enter PIN
```

This message is Output.

---

# 🖥️ print() Function

Python uses the `print()` function to display information.

### Example

```python
print("Hello World")
```

Output

```
Hello World
```

---

### Printing Numbers

```python
print(100)
print(99.5)
```

Output

```
100
99.5
```

---

### Printing Variables

```python
name = "Rahul"
age = 20

print(name)
print(age)
```

Output

```
Rahul
20
```

---

### Printing Multiple Values

```python
name = "Rahul"
age = 20

print(name, age)
```

Output

```
Rahul 20
```

---

# 🤔 What is Input?

Input means

> **Taking information from the user.**

---

# 🌍 Real-Life Example

When you log into Instagram,

the app asks for

- Username
- Password

These are Inputs.

---

# ⌨️ input() Function

Python uses `input()` to take user input.

### Example

```python
name = input("Enter your name: ")

print(name)
```

Output

```
Enter your name: Rahul

Rahul
```

---

# ⚠️ Important Note

The `input()` function **always returns a String**.

Example

```python
age = input("Enter Age: ")

print(type(age))
```

Output

```
<class 'str'>
```

Even if you enter

```
20
```

Python stores it as

```
"20"
```

---

# Taking Integer Input

Use `int()`.

```python
age = int(input("Enter Age: "))

print(age)
print(type(age))
```

Output

```
20
<class 'int'>
```

---

# Taking Float Input

Use `float()`.

```python
height = float(input("Enter Height: "))

print(height)
```

Output

```
5.8
```

---

# Taking String Input

```python
city = input("Enter City: ")

print(city)
```

---

# Taking Multiple Inputs

Suppose the user enters

```
10 20
```

Use `split()`.

```python
a, b = input("Enter two numbers: ").split()

print(a)
print(b)
```

Output

```
10
20
```

---

# Multiple Integer Inputs

```python
a, b = map(int, input("Enter two numbers: ").split())

print(a)
print(b)
```

Example

Input

```
15 25
```

Output

```
15
25
```

---

# Multiple Float Inputs

```python
x, y = map(float, input().split())

print(x)
print(y)
```

---

# Printing with Labels

```python
name = "Rahul"
age = 20

print("Name:", name)
print("Age:", age)
```

Output

```
Name: Rahul
Age: 20
```

---

# f-Strings (Recommended)

Python provides **f-strings** to create clean and readable output.

```python
name = "Rahul"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

Output

```
My name is Rahul and I am 20 years old.
```

---

# Why Use f-Strings?

Without f-string

```python
print("Name:", name, "Age:", age)
```

With f-string

```python
print(f"Name: {name}, Age: {age}")
```

Cleaner and easier to read.

---

# Escape Characters

```python
print("Hello\nWorld")
```

Output

```
Hello
World
```

---

```python
print("Python\tDSA")
```

Output

```
Python    DSA
```

---

# Common Escape Characters

| Escape | Meaning |
|---------|---------|
| `\n` | New Line |
| `\t` | Tab Space |
| `\"` | Double Quote |
| `\'` | Single Quote |
| `\\` | Backslash |

---

# Common Mistakes

## Mistake 1

```python
age = input()

print(age + 5)
```

❌ Error

Because `age` is a String.

---

## Correct

```python
age = int(input())

print(age + 5)
```

---

## Mistake 2

```python
a, b = input()
```

This reads one character at a time.

Use

```python
a, b = input().split()
```

---

## Mistake 3

Forgetting `map()` when taking integer inputs.

Wrong

```python
a, b = input().split()
```

Correct

```python
a, b = map(int, input().split())
```

---

# 🧠 Interview Questions

### Q1. What is Input?

### Q2. What is Output?

### Q3. Difference between `print()` and `input()`?

### Q4. Why does `input()` return a String?

### Q5. Difference between `int(input())` and `input()`?

### Q6. What is an f-string?

### Q7. What is `split()`?

### Q8. What is `map()`?

---

# 💻 Practice Questions

## Easy

1. Take your name and print it.

2. Take your age and print it.

3. Take your city and print it.

4. Take two numbers and print their sum.

5. Take height as Float.

---

## Medium

Create a program that asks for

- Name
- Age
- College
- Branch
- CGPA

Print everything using an f-string.

---

## Challenge

Take three integers from one line.

Example Input

```
10 20 30
```

Output

```
Sum = 60
Average = 20
```

---

# 📋 Cheat Sheet

```python
# Output

print("Hello")

# String Input

name = input()

# Integer Input

age = int(input())

# Float Input

height = float(input())

# Multiple String Input

a, b = input().split()

# Multiple Integer Input

a, b = map(int, input().split())

# f-String

print(f"Age = {age}")
```

---

# 📝 Summary

✅ `print()` displays output.

✅ `input()` takes user input.

✅ `input()` always returns a String.

✅ Use `int()` for Integer input.

✅ Use `float()` for Float input.

✅ Use `split()` for multiple inputs.

✅ Use `map()` to convert multiple values into Integers or Floats.

✅ Use f-strings for clean and professional output.

---

# 🎯 Mini Assignment

Write a Python program that asks the user for:

- Name
- Age
- City
- College
- Branch
- CGPA

Then display the information like this:

```
========== Student Details ==========

Name    : Rahul
Age     : 20
City    : Indore
College : XYZ College
Branch  : BCA
CGPA    : 8.75

=====================================
```

---

# 🎉 Congratulations!

You have completed **Chapter 6 – Input and Output**.

You can now create interactive Python programs that communicate with users. This skill is essential for solving coding problems, building applications, and writing DSA programs.