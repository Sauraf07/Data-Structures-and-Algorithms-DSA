# 📘 Chapter 10 – Python Operators

<div align="center">

# ➕ Python Operators

### "Operators are symbols that perform operations on values and variables."

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What are Operators?
- Why Do We Need Operators?
- Types of Operators
- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Identity Operators
- Membership Operators
- Bitwise Operators (Introduction)
- Operator Precedence
- Common Mistakes
- Interview Questions
- Practice Questions
- Cheat Sheet
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Understand Operators

✅ Perform Mathematical Operations

✅ Compare Values

✅ Work with Logical Conditions

✅ Understand Identity & Membership Operators

✅ Learn the Basics of Bitwise Operators

---

# 🤔 What is an Operator?

An **Operator** is a symbol that performs an operation on one or more values.

Think of an operator as an **action**.

---

# 🌍 Real-Life Example

Imagine a calculator.

You press

```
5 + 3
```

The calculator performs **Addition**.

Here,

```
+
```

is an **Operator**.

Similarly,

Python uses operators to perform different tasks.

---

# Example

```python
a = 10
b = 5

print(a + b)
```

Output

```
15
```

---

# Types of Operators

Python provides

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Identity Operators
- Membership Operators
- Bitwise Operators

---

# 1️⃣ Arithmetic Operators

Used to perform mathematical calculations.

| Operator | Meaning | Example |
|----------|---------|---------|
| + | Addition | 5 + 2 |
| - | Subtraction | 5 - 2 |
| * | Multiplication | 5 * 2 |
| / | Division | 5 / 2 |
| // | Floor Division | 5 // 2 |
| % | Modulus | 5 % 2 |
| ** | Exponent | 5 ** 2 |

---

# ➕

```python
print(10 + 5)
```

Output

```
15
```

---

# ➖

```python
print(10 - 5)
```

Output

```
5
```

---

# ✖

```python
print(10 * 5)
```

Output

```
50
```

---

# ➗

```python
print(10 / 3)
```

Output

```
3.3333333333
```

Division always returns a Float.

---

# Floor Division //

Returns only the whole number.

```python
print(10 // 3)
```

Output

```
3
```

---

# Modulus %

Returns the remainder.

```python
print(10 % 3)
```

Output

```
1
```

---

# 🌍 Real-Life Example

Suppose

10 chocolates

3 children

Each gets

```
10 // 3 = 3
```

Remaining chocolates

```
10 % 3 = 1
```

---

# Exponent **

Power of a number.

```python
print(2 ** 3)
```

Output

```
8
```

Because

```
2 × 2 × 2
```

---

# 2️⃣ Assignment Operators

Used to assign values.

---

Simple Assignment

```python
x = 10
```

---

Addition Assignment

```python
x = 10

x += 5

print(x)
```

Output

```
15
```

---

Subtraction Assignment

```python
x -= 2
```

---

Multiplication Assignment

```python
x *= 3
```

---

Division Assignment

```python
x /= 2
```

---

Floor Division Assignment

```python
x //= 2
```

---

Modulus Assignment

```python
x %= 3
```

---

Exponent Assignment

```python
x **= 2
```

---

# 🌍 Real-Life Example

Imagine your wallet.

You have

₹100

Your friend gives

₹50

Instead of

```
money = money + 50
```

Write

```
money += 50
```

Cleaner and shorter.

---

# 3️⃣ Comparison Operators

Comparison operators compare two values.

They always return

```
True

or

False
```

| Operator | Meaning |
|----------|---------|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

---

Example

```python
print(10 == 10)
```

Output

```
True
```

---

```python
print(10 != 5)
```

Output

```
True
```

---

```python
print(5 > 10)
```

Output

```
False
```

---

# 🌍 Real-Life Example

Teacher checks

```
Marks >= 40
```

If True

Pass

Else

Fail

---

# 4️⃣ Logical Operators

Used to combine conditions.

| Operator | Meaning |
|----------|---------|
| and | Both must be True |
| or | At least one True |
| not | Reverses the result |

---

AND

```python
print(True and True)
```

Output

```
True
```

---

```python
print(True and False)
```

Output

```
False
```

---

OR

```python
print(True or False)
```

Output

```
True
```

---

NOT

```python
print(not True)
```

Output

```
False
```

---

# 🌍 Real-Life Example

To enter an exam hall,

you need

```
Admit Card

AND

College ID
```

Both are required.

This is `and`.

---

# 5️⃣ Identity Operators

Used to check whether two variables refer to the **same object** in memory.

| Operator | Meaning |
|----------|---------|
| is | Same Object |
| is not | Different Object |

---

Example

```python
a = [1, 2]
b = a

print(a is b)
```

Output

```
True
```

---

Example

```python
a = [1, 2]
b = [1, 2]

print(a is b)
```

Output

```
False
```

Even though values are the same,

they are different objects.

---

# 6️⃣ Membership Operators

Used to check whether an item exists in a sequence.

| Operator | Meaning |
|----------|---------|
| in | Present |
| not in | Not Present |

---

Example

```python
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
```

Output

```
True
```

---

Example

```python
print("Orange" not in fruits)
```

Output

```
True
```

---

# 🌍 Real-Life Example

Guest List

```
Rahul

Priya

Aman
```

Check

```
Rahul in Guest List

↓

True
```

---

# 7️⃣ Bitwise Operators (Introduction)

Bitwise operators work on binary numbers.

| Operator | Meaning |
|----------|---------|
| & | AND |
| \| | OR |
| ^ | XOR |
| ~ | NOT |
| << | Left Shift |
| >> | Right Shift |

Example

```python
print(5 & 3)
```

Output

```
1
```

Don't worry.

You'll study Bit Manipulation in detail later.

---

# Operator Precedence

Python follows a priority order.

```
()

↓

**

↓

* / // %

↓

+ -

↓

Comparison

↓

Logical
```

---

Example

```python
print(2 + 3 * 4)
```

Output

```
14
```

Because

```
3 × 4 = 12

12 + 2 = 14
```

---

# Common Mistakes

### Mistake 1

```python
print(10 / 2)
```

Returns

```
5.0
```

Not

```
5
```

---

### Mistake 2

Using

```python
=
```

instead of

```python
==
```

Wrong

```python
if age = 18
```

Correct

```python
if age == 18
```

---

### Mistake 3

Confusing

```
is

and

==
```

Use

```
==
```

to compare values.

Use

```
is
```

to compare objects.

---

# Interview Questions

### Q1. What is an Operator?

### Q2. Difference between `/` and `//`?

### Q3. Difference between `=` and `==`?

### Q4. Difference between `is` and `==`?

### Q5. Difference between `and` and `or`?

### Q6. What does `%` return?

### Q7. What is Operator Precedence?

---

# Practice Questions

## Easy

1. Add two numbers.

2. Find remainder.

3. Find square of a number.

4. Compare two numbers.

5. Check whether a name exists in a list.

---

## Medium

Take two numbers from the user and print

- Sum
- Difference
- Product
- Division
- Floor Division
- Modulus
- Power

---

## Challenge

Take marks as input.

If

```
marks >= 40

and

attendance >= 75
```

Print

```
Pass
```

Else

```
Fail
```

---

# 📋 Cheat Sheet

```python
# Arithmetic

+

-

*

/

//

%

**

# Assignment

=

+=

-=

*=

/=

# Comparison

==

!=

>

<

>=

<=

# Logical

and

or

not

# Identity

is

is not

# Membership

in

not in
```

---

# 📝 Summary

✅ Operators perform operations on values.

✅ Arithmetic Operators perform calculations.

✅ Assignment Operators assign values.

✅ Comparison Operators return True or False.

✅ Logical Operators combine conditions.

✅ Identity Operators compare memory objects.

✅ Membership Operators check whether an item exists.

✅ Bitwise Operators work with binary numbers.

---

# 🎯 Mini Assignment

Create a calculator program that:

- Takes two numbers as input
- Displays:
  - Addition
  - Subtraction
  - Multiplication
  - Division
  - Floor Division
  - Modulus
  - Power
- Checks:
  - Equality
  - Greater than
  - Less than
- Prints the results using **f-strings**

Example Output

```
========== Calculator ==========

Addition        : 30
Subtraction     : 10
Multiplication  : 200
Division        : 2.0
Floor Division  : 2
Modulus         : 0
Power           : 10000

===============================
```

---

# 🎉 Congratulations!

You have completed **Chapter 10 – Python Operators**.

You now understand all the major operators in Python and how they are used in real-world programs and DSA problems. Mastering operators is essential because they appear in almost every coding interview question.

---

# 🚀 What's Next?

## Chapter 11 – Conditional Statements (`if`, `if-else`, `elif`, Nested if`)

You'll learn:

- `if`
- `if-else`
- `elif`
- Nested `if`
- Match-case (Python 3.10+)
- Real-life decision-making examples
- Flowcharts
- Practice questions
- Interview questions
- Mini projects