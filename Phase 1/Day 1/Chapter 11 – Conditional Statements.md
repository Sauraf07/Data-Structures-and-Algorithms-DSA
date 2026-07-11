# 📘 Chapter 11 – Conditional Statements in Python

<div align="center">

# 🤔 Conditional Statements in Python

### "A computer can make decisions based on conditions."

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What are Conditional Statements?
- Why Do We Need Conditions?
- Flow of Decision Making
- if Statement
- if-else Statement
- if-elif-else Statement
- Nested if Statement
- Match Case (Python 3.10+)
- Common Mistakes
- Interview Questions
- Practice Questions
- Cheat Sheet
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Understand Decision Making

✅ Use if Statements

✅ Use if-else Statements

✅ Use elif Statements

✅ Write Nested if Statements

✅ Use match-case (Python 3.10+)

---

# 🤔 What is a Conditional Statement?

A **Conditional Statement** allows a program to make decisions.

Instead of executing every line of code, Python checks a condition first.

If the condition is **True**, one block of code runs.

If the condition is **False**, another block may run.

---

# 🌍 Real-Life Example

Imagine a traffic signal.

```
Is the light Green?

↓

Yes

↓

Go

----------------

No

↓

Stop
```

The decision depends on the condition.

Python works in exactly the same way.

---

# Why Do We Need Conditional Statements?

Suppose a website asks

```
Age = 20
```

Can the user vote?

Python checks

```
Age >= 18
```

If True

```
Allowed to Vote
```

Else

```
Not Allowed
```

Without conditions,

computers cannot make decisions.

---

# Flow of Decision Making

```
Start

↓

Condition

↓

True ---------> Execute Block

↓

False --------> Skip Block

↓

End
```

---

# 1️⃣ if Statement

The `if` statement executes code **only if the condition is True**.

### Syntax

```python
if condition:
    # code
```

Notice the **colon (`:`)** and **indentation**.

---

# Example

```python
age = 20

if age >= 18:
    print("You can vote.")
```

Output

```
You can vote.
```

---

# Example

```python
marks = 90

if marks >= 40:
    print("Pass")
```

Output

```
Pass
```

---

# Example

```python
temperature = 35

if temperature > 30:
    print("It's Hot!")
```

Output

```
It's Hot!
```

---

# 🌍 Real-Life Example

ATM Machine

```
Balance > 0

↓

Yes

↓

Allow Withdrawal
```

If balance is not greater than 0,

the withdrawal does not happen.

---

# 2️⃣ if-else Statement

Sometimes,

we want one action if the condition is True,

and another action if it is False.

### Syntax

```python
if condition:
    # True Block
else:
    # False Block
```

---

# Example

```python
age = 16

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")
```

Output

```
Not Eligible
```

---

# Example

```python
number = 10

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

Output

```
Even Number
```

---

# 🌍 Real-Life Example

Movie Ticket

```
Age >= 18

↓

Yes

↓

Adult Ticket

---------------

No

↓

Child Ticket
```

---

# 3️⃣ if-elif-else Statement

When there are **multiple conditions**, use `elif`.

### Syntax

```python
if condition1:
    # Block 1

elif condition2:
    # Block 2

elif condition3:
    # Block 3

else:
    # Default Block
```

---

# Example

```python
marks = 85

if marks >= 90:
    print("Grade A+")

elif marks >= 75:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

elif marks >= 40:
    print("Grade C")

else:
    print("Fail")
```

Output

```
Grade A
```

---

# 🌍 Real-Life Example

Restaurant Menu

```
Choose

1

↓

Pizza

---------------

2

↓

Burger

---------------

3

↓

Pasta

---------------

Anything Else

↓

Invalid Choice
```

Only one option is selected.

---

# 4️⃣ Nested if Statement

A **Nested if** means an `if` statement inside another `if` statement.

### Syntax

```python
if condition1:
    if condition2:
        # Code
```

---

# Example

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
```

Output

```
Eligible to Vote
```

---

# 🌍 Real-Life Example

Driving License

```
Age >= 18

↓

Yes

↓

Has Driving Test Passed?

↓

Yes

↓

License Approved

---------------

No

↓

Rejected
```

More than one condition is checked.

---

# 5️⃣ Match Case (Python 3.10+)

Python 3.10 introduced the `match-case` statement.

It works like a switch statement in other languages.

### Syntax

```python
match value:
    case option1:
        # code

    case option2:
        # code

    case _:
        # default
```

---

# Example

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")
```

Output

```
Wednesday
```

---

# if vs match-case

| if-elif | match-case |
|----------|------------|
| Good for conditions | Good for fixed values |
| Can use comparisons | Matches exact values |
| More flexible | Cleaner for menus |

---

# Indentation

Python uses **indentation** instead of `{}`.

Correct

```python
if age >= 18:
    print("Adult")
```

Wrong

```python
if age >= 18:
print("Adult")
```

This causes

```
IndentationError
```

---

# Common Mistakes

## Mistake 1

Using `=` instead of `==`

Wrong

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

## Mistake 2

Forgetting the colon

Wrong

```python
if age > 18
```

Correct

```python
if age > 18:
```

---

## Mistake 3

Wrong indentation

```python
if age > 18:
print("Adult")
```

Always indent the block.

---

## Mistake 4

Writing unnecessary nested if statements.

Keep your code simple whenever possible.

---

# Interview Questions

### Q1. What is a Conditional Statement?

### Q2. Difference between if and if-else?

### Q3. What is elif?

### Q4. What is Nested if?

### Q5. What is match-case?

### Q6. Why is indentation important in Python?

### Q7. Difference between match-case and if-elif?

---

# Practice Questions

## Easy

1. Check whether a number is positive or negative.

2. Check whether a number is even or odd.

3. Check voting eligibility.

4. Check whether a student passed.

5. Find the larger of two numbers.

---

## Medium

1. Grade Calculator

2. Simple Calculator using if-elif

3. Check Leap Year

4. Check Greatest of Three Numbers

5. Check whether a character is a vowel or consonant.

---

## Challenge

Write a Login System.

Input

```
Username

Password
```

Expected Output

```
Login Successful
```

or

```
Invalid Username or Password
```

---

# Mini Project

## Student Result System

```python
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A+")

elif marks >= 75:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

elif marks >= 40:
    print("Grade C")

else:
    print("Fail")
```

---

# Cheat Sheet

```python
# if

if condition:
    pass

# if-else

if condition:
    pass
else:
    pass

# if-elif-else

if condition:
    pass
elif condition:
    pass
else:
    pass

# Nested if

if condition:
    if another_condition:
        pass

# Match Case

match value:
    case 1:
        pass
    case _:
        pass
```

---

# Summary

✅ Conditional Statements help Python make decisions.

✅ `if` executes code only when a condition is True.

✅ `if-else` chooses between two blocks.

✅ `if-elif-else` handles multiple conditions.

✅ Nested `if` is used when one condition depends on another.

✅ `match-case` is useful for matching fixed values.

✅ Indentation is mandatory in Python.

---

# 🎯 Mini Assignment

Create a **Student Admission Checker**.

Input

- Name
- Age
- Marks

Rules

- Age must be **17 or above**
- Marks must be **60 or above**

If both conditions are satisfied,

Display

```
Admission Approved
```

Otherwise

```
Admission Rejected
```

---

# 🎉 Congratulations!

You have completed **Chapter 11 – Conditional Statements**.

You can now make your Python programs think and make decisions based on different situations. This is one of the most important concepts because almost every DSA problem and real-world application uses conditional logic.