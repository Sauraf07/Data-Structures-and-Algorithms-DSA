# 📘 Chapter 4 - Variables in Python

<div align="center">

# 📦 Variables in Python

### Store Information Like a Pro!

*"A Variable is a container that stores data in memory."*

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What is a Variable?
- Why Do We Need Variables?
- Real-Life Examples
- How Variables Work
- Creating Variables
- Variable Naming Rules
- Naming Conventions
- Dynamic Typing
- Multiple Variable Assignment
- Variable Swapping
- Memory Representation
- Variables vs Constants
- Common Mistakes
- Interview Questions
- Practice Problems
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

✅ Understand what variables are

✅ Create variables in Python

✅ Name variables correctly

✅ Understand how Python stores data

✅ Swap variables without using a third variable

✅ Avoid beginner mistakes

---

# 🤔 What is a Variable?

Imagine you have a box.

You can put anything inside it.

```
+----------------+
|      📦        |
|    Chocolate   |
+----------------+
```

Tomorrow you remove the chocolate and keep a toy.

```
+----------------+
|      📦        |
|      Toy       |
+----------------+
```

The **box** is still the same.

Only the **content changes**.

A variable works exactly like that.

It is simply a **named container** that stores information.

---

# 🌍 Real-Life Example 1 – School Bag

Suppose you have a school bag.

Today it contains

- Notebook
- Pencil

Tomorrow

- Laptop
- Charger

The bag didn't change.

Only its contents changed.

```
Bag
 │
 ├── Notebook
 ├── Pencil
```

Later

```
Bag
 │
 ├── Laptop
 ├── Charger
```

Variables behave in the same way.

---

# 🌍 Real-Life Example 2 – Water Bottle

Bottle

```
Bottle

↓

Water
```

Later

```
Bottle

↓

Juice
```

The bottle remains the same.

Only the value changes.

Variable = Bottle

Value = Water / Juice

---

# 🌍 Real-Life Example 3 – Student Roll Number

Teacher says

```
Roll Number 15

↓

Rahul
```

Tomorrow

```
Roll Number 15

↓

Aman
```

Roll Number = Variable

Student Name = Value

---

# 📦 Variable Definition

A variable is a name given to a memory location where data is stored.

Simple definition:

> Variable = Name + Value

---

# 🧠 Think Like This

```
age = 20
```

means

```
Variable Name

age

↓

Stored Value

20
```

---

# First Variable

```python
name = "Rahul"

print(name)
```

Output

```
Rahul
```

---

# Another Example

```python
city = "Indore"

print(city)
```

Output

```
Indore
```

---

# Storing Numbers

```python
age = 21

print(age)
```

Output

```
21
```

---

# Storing Decimal Numbers

```python
height = 5.8

print(height)
```

Output

```
5.8
```

---

# Storing True or False

```python
is_student = True

print(is_student)
```

Output

```
True
```

---

# One Variable Can Store Different Data

```python
x = 10

print(x)

x = "Python"

print(x)
```

Output

```
10
Python
```

Python allows this because it is **dynamically typed**.

---

# 🧠 Dynamic Typing

Some programming languages require you to tell the computer what type of data a variable will hold.

Example (Java)

```java
int age = 20;
```

Python is different.

You simply write

```python
age = 20
```

Python automatically understands that **20 is an integer**.

This is called **Dynamic Typing**.

---

# Memory Representation

Suppose we write

```python
age = 20
```

Python internally stores it like this:

```
Variable

age

↓

Memory Address

0x100

↓

20
```

You don't need to manage memory yourself.

Python handles it automatically.

---

# Changing Variable Values

```python
score = 50

print(score)

score = 80

print(score)
```

Output

```
50
80
```

The old value is replaced with the new one.

---

# Multiple Variables

```python
name = "Rahul"
age = 20
city = "Indore"

print(name)
print(age)
print(city)
```

Output

```
Rahul
20
Indore
```

---

# Multiple Assignment

Instead of writing

```python
x = 10
y = 20
z = 30
```

Python allows

```python
x, y, z = 10, 20, 30
```

Output

```python
print(x)
print(y)
print(z)
```

```
10
20
30
```

---

# Assign Same Value

```python
a = b = c = 100

print(a)
print(b)
print(c)
```

Output

```
100
100
100
```

---

# Swapping Variables

Normally

```
Glass A

↓

Water

Glass B

↓

Juice
```

You want

```
Glass A

↓

Juice

Glass B

↓

Water
```

Python makes it easy.

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output

```
20
10
```

No temporary variable is needed.

---

# Variable Naming Rules

Python has some rules.

## Rule 1

Variable names can contain

- Letters
- Numbers
- Underscore (_)

Example

```python
student1

roll_no

age
```

Correct ✅

---

## Rule 2

Cannot start with a number

Wrong ❌

```python
1age = 20
```

Correct ✅

```python
age1 = 20
```

---

## Rule 3

No spaces

Wrong

```python
student name
```

Correct

```python
student_name
```

---

## Rule 4

No special characters

Wrong

```python
age@
```

Correct

```python
age
```

---

## Rule 5

Python is Case Sensitive

```python
age = 20

Age = 30
```

These are two different variables.

```
age ≠ Age
```

---

# Naming Conventions

Good names make code readable.

Bad

```python
a = 20
```

Good

```python
student_age = 20
```

Bad

```python
x = "Rahul"
```

Good

```python
student_name = "Rahul"
```

---

# Snake Case

Python follows **snake_case**.

Example

```python
student_name

employee_salary

total_marks
```

Not

```python
StudentName

studentName
```

---

# Constants

Python doesn't have true constants.

By convention, constants are written in uppercase.

```python
PI = 3.14159

MAX_SPEED = 120
```

This tells other programmers that these values should not be changed.

---

# Common Mistakes

❌ Using spaces

```python
student name = "Rahul"
```

---

❌ Starting with numbers

```python
2student = "Rahul"
```

---

❌ Using keywords

```python
class = 10
```

---

❌ Confusing Age and age

```python
Age = 20
age = 30
```

They are different variables.

---

# 🧠 Interview Questions

### Q1. What is a variable?

### Q2. Why do we use variables?

### Q3. What is dynamic typing?

### Q4. Explain snake_case.

### Q5. Can Python change the data type of a variable?

### Q6. What is multiple assignment?

### Q7. How do you swap two variables in Python?

---

# 💻 Practice Questions

## Easy

1. Create a variable called `name` and store your name.

2. Store your age in a variable.

3. Store your college name.

4. Print all variables.

5. Change your age.

---

## Medium

6. Swap two numbers.

7. Store three variables in one line.

8. Assign one value to three variables.

9. Create variables for:

- Name
- Age
- City
- College
- CGPA

10. Print them using `print()`.

---

# 🎯 Mini Challenge

Create variables for yourself.

```
Name

Age

College

Branch

Semester

City

Dream Company
```

Print them like this:

```
Name : Rahul

Age : 20

College : XYZ

City : Indore

Dream Company : Google
```

---

# 📋 Cheat Sheet

```python
name = "Rahul"

age = 20

height = 5.8

is_student = True

x, y = 10, 20

a = b = c = 100

a, b = b, a
```

---

# 📝 Summary

✅ A variable is a named container that stores data.

✅ Variables can store numbers, text, decimal values, and Boolean values.

✅ Python uses dynamic typing, so you don't need to declare the data type.

✅ Variable names should be meaningful and follow snake_case.

✅ Python allows multiple assignment and easy variable swapping.

✅ Python is case-sensitive, so `age` and `Age` are different variables.

---

# 🎉 Congratulations!

You have completed **Chapter 4 – Variables**.

You now know how to create, use, rename, and manage variables in Python. These are the building blocks for every Python program and every DSA problem you'll solve.