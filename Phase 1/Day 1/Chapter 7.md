# 📘 Chapter 7 – Type Casting in Python

<div align="center">

# 🔄 Type Casting in Python

### "Converting one data type into another."

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What is Type Casting?
- Why Do We Need Type Casting?
- Types of Type Casting
- Implicit Type Casting
- Explicit Type Casting
- int()
- float()
- str()
- bool()
- Common Conversion Errors
- Practice Questions
- Interview Questions
- Cheat Sheet
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Understand Type Casting

✅ Convert between different data types

✅ Avoid common conversion mistakes

✅ Use int(), float(), str(), and bool()

---

# 🤔 What is Type Casting?

Type Casting means:

> **Converting one data type into another data type.**

Example

```
"20"

↓

20
```

String becomes Integer.

---

# 🌍 Real-Life Example

Imagine you have ₹100 in cash.

You exchange it for a ₹100 gift card.

The value is the same.

Only the form has changed.

Similarly,

```
"20"

↓

20
```

The value remains 20.

Only the data type changes.

---

# Why Do We Need Type Casting?

Suppose

```python
age = input("Enter Age: ")

print(age + 5)
```

This gives an error because `input()` returns a String.

Correct

```python
age = int(input("Enter Age: "))

print(age + 5)
```

Output

```
25
```

---

# Types of Type Casting

Python supports two types:

1. Implicit Type Casting
2. Explicit Type Casting

---

# 1️⃣ Implicit Type Casting

Python automatically converts one data type into another when it is safe.

Example

```python
x = 10
y = 2.5

print(x + y)
```

Output

```
12.5
```

Python converts

```
10

↓

10.0
```

Automatically.

---

# Memory Representation

```
10 (int)

+

2.5 (float)

↓

10.0

+

2.5

↓

12.5
```

---

# 2️⃣ Explicit Type Casting

Explicit means

**You tell Python to convert the data type.**

Python provides functions for this.

```
int()

float()

str()

bool()
```

---

# 🔢 int()

Converts a value into Integer.

---

## Float to Integer

```python
x = int(5.9)

print(x)
```

Output

```
5
```

Python removes the decimal part.

---

## String to Integer

```python
age = int("20")

print(age)
```

Output

```
20
```

---

## Boolean to Integer

```python
print(int(True))
print(int(False))
```

Output

```
1
0
```

---

# ⚠️ Invalid Conversion

```python
int("Hello")
```

Output

```
ValueError
```

Because "Hello" is not a number.

---

# 🌊 float()

Converts a value into Float.

---

## Integer to Float

```python
x = float(10)

print(x)
```

Output

```
10.0
```

---

## String to Float

```python
price = float("99.99")

print(price)
```

Output

```
99.99
```

---

## Boolean to Float

```python
print(float(True))
print(float(False))
```

Output

```
1.0
0.0
```

---

# ⚠️ Invalid Conversion

```python
float("Python")
```

Output

```
ValueError
```

---

# 🔤 str()

Converts any value into String.

---

## Integer to String

```python
age = str(20)

print(age)
print(type(age))
```

Output

```
20
<class 'str'>
```

---

## Float to String

```python
price = str(99.99)

print(price)
```

Output

```
99.99
```

---

## Boolean to String

```python
print(str(True))
```

Output

```
True
```

---

# Why Convert to String?

Suppose

```python
name = "Rahul"
age = 20
```

Without f-string

```python
print(name + age)
```

Error

Correct

```python
print(name + str(age))
```

Output

```
Rahul20
```

---

# ✅ bool()

Converts values into Boolean.

---

# Rules

```
0

↓

False
```

```
Empty String

↓

False
```

```
Empty List

↓

False
```

Everything else becomes

```
True
```

---

## Examples

```python
print(bool(1))
```

Output

```
True
```

---

```python
print(bool(0))
```

Output

```
False
```

---

```python
print(bool(""))
```

Output

```
False
```

---

```python
print(bool("Python"))
```

Output

```
True
```

---

```python
print(bool([]))
```

Output

```
False
```

---

```python
print(bool([1,2]))
```

Output

```
True
```

---

# Type Conversion Table

| From | To | Result |
|------|----|--------|
| int | float | ✅ |
| float | int | Decimal Removed |
| str("20") | int | ✅ |
| str("99.5") | float | ✅ |
| int | str | ✅ |
| float | str | ✅ |
| bool | int | True→1 False→0 |
| int | bool | 0=False Others=True |

---

# 🌍 Real-Life Example

Suppose you buy a movie ticket.

Age entered by the user:

```
"18"
```

The computer cannot compare text with numbers.

Convert it

```
"18"

↓

18
```

Now Python can check

```
age >= 18
```

---

# Common Mistakes

## Mistake 1

```python
age = input()

print(age + 5)
```

❌ Error

Correct

```python
age = int(input())

print(age + 5)
```

---

## Mistake 2

```python
int("Hello")
```

❌ Error

---

## Mistake 3

```python
float("Python")
```

❌ Error

---

## Mistake 4

```python
name = "Rahul"

print(name + 20)
```

Correct

```python
print(name + str(20))
```

---

# 🧠 Interview Questions

### Q1. What is Type Casting?

### Q2. Difference between Implicit and Explicit Type Casting?

### Q3. Difference between int() and float()?

### Q4. What does bool(0) return?

### Q5. What does bool("") return?

### Q6. Why does int("Hello") fail?

### Q7. What happens when converting float to int?

---

# 💻 Practice Questions

## Easy

1. Convert `"25"` into Integer.

2. Convert `100` into String.

3. Convert `5` into Float.

4. Convert `False` into Integer.

5. Convert `""` into Boolean.

---

## Medium

Write a program that

- Takes age as input
- Converts it into Integer
- Adds 5
- Prints the result

---

## Challenge

Take two numbers from the user.

Convert them into Integers.

Print

- Sum
- Difference
- Product
- Division

---

# 📋 Cheat Sheet

```python
# Integer

int("20")

# Float

float("99.9")

# String

str(100)

# Boolean

bool(1)

bool(0)

# Type

type(value)
```

---

# 📝 Summary

✅ Type Casting means converting one data type into another.

✅ Python supports Implicit and Explicit Type Casting.

✅ Use `int()` to convert values into Integers.

✅ Use `float()` to convert values into Floats.

✅ Use `str()` to convert values into Strings.

✅ Use `bool()` to convert values into Boolean values.

✅ Invalid conversions raise a `ValueError`.

---

# 🎯 Mini Assignment

Create a program that asks the user for:

- Name
- Age
- Height
- Weight

Convert:

- Age → Integer
- Height → Float
- Weight → Float

Then print:

```
========== User Profile ==========

Name   : Rahul
Age    : 20
Height : 5.8
Weight : 62.5

=================================
```

---

# 🎉 Congratulations!

You have completed **Chapter 7 – Type Casting in Python**.

You now understand how to safely convert data between different types, a skill you'll use in almost every Python program and coding interview.