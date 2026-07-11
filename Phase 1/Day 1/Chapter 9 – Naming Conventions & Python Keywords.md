# 📘 Chapter 9 – Naming Conventions & Python Keywords

<div align="center">

# 🏷️ Naming Conventions & Python Keywords

### "Good code is not just correct—it is easy to read."

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What are Identifiers?
- Rules for Naming Variables
- Naming Conventions
- Snake Case
- Camel Case
- Pascal Case
- Constants
- Reserved Keywords
- Keyword Module
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Questions
- Cheat Sheet
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Understand Identifiers

✅ Name variables correctly

✅ Follow Python naming conventions

✅ Understand Python Keywords

✅ Write clean and readable code

---

# 🤔 What is an Identifier?

An **Identifier** is simply a name given to something in Python.

Identifiers are used to name

- Variables
- Functions
- Classes
- Objects
- Modules

Example

```python
name = "Rahul"
```

Here,

```
name
```

is an Identifier.

---

# 🌍 Real-Life Example

Imagine a school.

Every student has a unique name.

```
Rahul

Priya

Aman
```

Instead of saying

```
Student Number 125
```

we simply call

```
Rahul
```

Similarly,

Computers use identifiers to identify data.

---

# Examples of Identifiers

```python
age = 20

student_name = "Rahul"

marks = 95

calculate_sum()

Student()

```

All highlighted names are identifiers.

---

# Rules for Naming Identifiers

Python has some important rules.

---

# Rule 1

An identifier can contain

- Letters (A-Z, a-z)
- Numbers (0-9)
- Underscore (_)

Correct

```python
age

student1

_roll

total_marks
```

---

# Rule 2

Identifier **cannot start with a number**

Wrong ❌

```python
1age = 20
```

Correct ✅

```python
age1 = 20
```

---

# Rule 3

No Spaces

Wrong

```python
student name
```

Correct

```python
student_name
```

---

# Rule 4

No Special Characters

Wrong

```python
age@

marks%

salary$
```

Correct

```python
age

marks

salary
```

---

# Rule 5

Identifiers are Case Sensitive

```python
age = 20

Age = 30

AGE = 40
```

All three are different variables.

---

# Rule 6

Keywords cannot be used as identifiers.

Wrong

```python
class = 10
```

Python will show

```
SyntaxError
```

---

# 🌍 Real-Life Example

Imagine every classroom has a teacher.

Can two teachers have exactly the same employee ID?

No.

Identifiers should also be unique within the same scope.

---

# Naming Conventions

Python has official naming conventions.

These conventions make code easier to understand.

---

# 1️⃣ snake_case ✅ (Recommended)

Words are separated using underscores.

Example

```python
student_name

total_marks

employee_salary

mobile_number

college_name
```

This is the official Python style.

---

# 🌍 Real-Life Example

Imagine a road.

```
Student_Name
```

The underscore acts like a bridge joining words.

---

# 2️⃣ camelCase

The first word starts with a lowercase letter.

The remaining words start with a capital letter.

Example

```python
studentName

employeeSalary

collegeName
```

Mostly used in

- Java
- JavaScript

Not recommended in Python.

---

# 3️⃣ PascalCase

Every word starts with a capital letter.

Example

```python
StudentName

EmployeeSalary

CollegeName
```

Used mainly for

- Classes

Example

```python
class Student:
    pass
```

---

# 4️⃣ UPPER_CASE

Used for Constants.

Example

```python
PI = 3.14159

MAX_SPEED = 120

COLLEGE_NAME = "XYZ"
```

Python cannot stop you from changing them,

but programmers understand they should not be modified.

---

# Variable Naming Examples

Good

```python
student_name

age

height

weight

total_marks
```

Bad

```python
a

x

abc

temp1

xyz123
```

Meaningful names make code easier to understand.

---

# Python Keywords

Keywords are **reserved words**.

They already have a special meaning in Python.

You cannot use them as variable names.

---

# Examples of Keywords

Some common keywords are

```text
False

True

None

if

else

elif

for

while

break

continue

pass

return

def

class

try

except

finally

import

from

lambda

global

nonlocal

with

yield

async

await

is

in

not

and

or
```

---

# Example

Wrong

```python
for = 10
```

Output

```
SyntaxError
```

Correct

```python
count = 10
```

---

# How to View All Keywords?

Python provides the

```
keyword
```

module.

Example

```python
import keyword

print(keyword.kwlist)
```

Output

```
['False',
 'None',
 'True',
 'and',
 'as',
 'assert',
 ...
]
```

---

# Check Whether a Word is a Keyword

```python
import keyword

print(keyword.iskeyword("for"))
```

Output

```
True
```

---

```python
print(keyword.iskeyword("student"))
```

Output

```
False
```

---

# Best Practices

## ✅ Use Meaningful Names

Bad

```python
x = 50000
```

Good

```python
employee_salary = 50000
```

---

## ✅ Keep Names Short but Clear

Bad

```python
the_total_salary_of_all_employees_in_company
```

Good

```python
total_salary
```

---

## ✅ Follow snake_case

Good

```python
student_name
```

Bad

```python
StudentName
```

---

## ✅ Use PascalCase for Classes

```python
class Student:
    pass
```

---

## ✅ Use UPPER_CASE for Constants

```python
PI = 3.14159

MAX_USERS = 100
```

---

# Common Mistakes

## Mistake 1

Starting with numbers

```python
1name = "Rahul"
```

Wrong

---

## Mistake 2

Using spaces

```python
student age
```

Wrong

---

## Mistake 3

Using Keywords

```python
if = 20
```

Wrong

---

## Mistake 4

Using meaningless names

```python
x = 20
```

Better

```python
student_age = 20
```

---

## Mistake 5

Ignoring Case Sensitivity

```python
age = 20

Age = 25
```

These are different variables.

---

# Interview Questions

### Q1. What is an Identifier?

### Q2. What are Python Keywords?

### Q3. Can keywords be used as variable names?

### Q4. What is snake_case?

### Q5. Difference between snake_case and camelCase?

### Q6. Why are meaningful variable names important?

### Q7. Which naming style does Python recommend?

### Q8. How do you check whether a word is a keyword?

---

# Practice Questions

## Easy

1. Create variables using snake_case.

2. Create a class using PascalCase.

3. Create a constant using UPPER_CASE.

4. Check whether `for` is a keyword.

5. Check whether `college` is a keyword.

---

## Medium

Rename the following variables using proper naming conventions.

```python
x = "Rahul"

A = 20

abc = 95

stnm = "Python"

num = 50000
```

---

# Cheat Sheet

```python
# snake_case

student_name = "Rahul"

total_marks = 95

# PascalCase

class Student:
    pass

# UPPER_CASE

PI = 3.14159

# Keywords

import keyword

print(keyword.kwlist)

print(keyword.iskeyword("for"))
```

---

# Summary

✅ An Identifier is the name of a variable, function, class, or object.

✅ Identifiers can contain letters, numbers, and underscores.

✅ Identifiers cannot start with a number.

✅ Identifiers cannot contain spaces or special characters.

✅ Python is case-sensitive.

✅ Keywords are reserved words and cannot be used as variable names.

✅ Use **snake_case** for variables and functions.

✅ Use **PascalCase** for classes.

✅ Use **UPPER_CASE** for constants.

---

# 🎯 Mini Assignment

Create a Python program that

- Creates five variables using **snake_case**
- Creates one class using **PascalCase**
- Creates three constants using **UPPER_CASE**
- Uses the `keyword` module to:
  - Print all Python keywords
  - Check whether `while`, `student`, and `class` are keywords

Expected Output

```
Is 'while' a keyword? True

Is 'student' a keyword? False

Is 'class' a keyword? True
```

---

# 🎉 Congratulations!

You have completed **Chapter 9 – Naming Conventions & Python Keywords**.

You now know how to write clean, professional, and Pythonic code by following proper naming conventions and avoiding reserved keywords.

---

# 🚀 What's Next?

## Chapter 10 – Python Operators

In the next chapter, you'll learn:

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Identity Operators
- Membership Operators
- Bitwise Operators
- Operator Precedence
- Real-life Examples
- Practice Questions
- Interview Questions
- Cheat Sheet

This chapter is essential because operators are used in **every Python program** and almost every **DSA problem**.