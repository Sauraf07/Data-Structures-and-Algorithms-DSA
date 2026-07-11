


# 📘 Chapter 5 - Data Types in Python (Part 1)

<div align="center">

# 📦 Data Types in Python

### "Everything stored in a computer has a type."

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What is Data?
- What is a Data Type?
- Why Do We Need Data Types?
- Real-Life Examples
- Memory Representation
- Python Data Types
- Numeric Data Types
- Integer (int)
- Float (float)
- Difference Between int and float
- Practice Questions
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Understand what data is

✅ Understand what a data type is

✅ Know why computers need data types

✅ Use Integer

✅ Use Float

✅ Differentiate between Integer and Float

---

# 🤔 Before Learning Data Types...

Let's first understand one question.

## What is Data?

Data is simply **information**.

Everything you see around you is data.

Examples

```
Your Name

Your Age

Your Height

Your Mobile Number

Your Marks

Your Salary

Temperature

Rainfall

Address
```

All of these are data.

---

# 🌍 Real-Life Example

Imagine you own a supermarket.

Inside your shop you have

🥛 Milk

🍎 Apples

🥤 Cold Drinks

🍫 Chocolates

🧼 Soap

All these are different products.

Can you keep milk inside the freezer?

Yes.

Can you keep soap inside the refrigerator?

Not necessary.

Every item has its own category.

Similarly,

Computers also divide information into categories.

These categories are called

# Data Types

---

# 🤔 What is a Data Type?

A Data Type tells Python

"What kind of data is stored?"

Think of it like labels on containers.

```
+-------------------+
| Apples            |
+-------------------+

+-------------------+
| Rice              |
+-------------------+

+-------------------+
| Sugar             |
+-------------------+
```

Without labels,

everything becomes confusing.

Computers also need labels.

---

# 🌍 Real-Life Example

Imagine a hospital.

Patients have files.

Every file contains

```
Name

Age

Blood Group

Weight

Phone Number
```

Can we store

```
Blood Group = 75
```

No.

Blood Group should be

```
A+

O-

AB+
```

Similarly,

Age should be a number.

Name should be text.

Weight should be decimal.

Every information has its own type.

---

# Why Do We Need Data Types?

Suppose you write

```python
age = 20
```

Python knows

```
20

↓

Number
```

Now suppose

```python
name = "Rahul"
```

Python knows

```
Rahul

↓

Text
```

Now suppose

```python
is_student = True
```

Python knows

```
True

↓

Boolean
```

Because of Data Types,

Python knows how to work with data correctly.

---

# 🌍 Another Real-Life Example

Imagine a classroom.

Teacher asks

"What is your age?"

Correct answer

```
20
```

Wrong answer

```
Blue
```

Teacher asks

"What is your name?"

Correct

```
Rahul
```

Wrong

```
105
```

Different questions expect different types of answers.

Programming is exactly the same.

---

# Memory Representation

Suppose

```python
age = 20
```

Internally

```
Variable

age

↓

Memory

0x100

↓

20

↓

Type

Integer
```

Another example

```python
name = "Rahul"
```

```
Variable

name

↓

Memory

0x220

↓

Rahul

↓

Type

String
```

Python stores

✔ Value

✔ Type

✔ Memory Address

---

# Python Built-in Data Types

Python has many data types.

The most important ones are

```
Numeric Types

Integer

Float

Complex

------------------

Text Type

String

------------------

Boolean Type

True

False

------------------

None Type

None

------------------

Collection Types

List

Tuple

Set

Dictionary
```

Don't worry.

Today we'll learn only

✔ Integer

✔ Float

The remaining types will be covered in the next parts.

---

# 📌 Numeric Data Types

Numbers are divided into three categories.

```
Integer

Float

Complex
```

Let's understand them one by one.

---

# 🔢 Integer (int)

An Integer is a whole number.

It has

✔ No decimal point

Examples

```
0

1

5

10

25

100

500

1000

-10

-200
```

All of these are Integers.

---

# 🌍 Real-Life Example

Imagine counting students.

```
1 Student

2 Students

3 Students

50 Students
```

Can you have

```
5.7 Students
```

No.

Students are counted in whole numbers.

Hence

Student Count = Integer

---

# Integer Example

```python
age = 20

print(age)
```

Output

```
20
```

---

Another Example

```python
marks = 95

print(marks)
```

Output

```
95
```

---

Negative Integer

```python
temperature = -5

print(temperature)
```

Output

```
-5
```

---

Zero is also an Integer

```python
score = 0

print(score)
```

Output

```
0
```

---

# Float (float)

Float means

A number having a decimal point.

Examples

```
2.5

10.8

5.75

99.99

0.25

-3.14
```

All are Float values.

---

# 🌍 Real-Life Example

Suppose your height is

```
175.5 cm
```

Can we write

```
175
```

Not exactly.

Height usually contains decimal values.

Therefore

Height = Float

---

Another Example

Petrol

```
2.5 Litres
```

Milk

```
1.5 Litres
```

Weight

```
58.6 kg
```

Money

```
₹99.50
```

All these use decimal numbers.

Hence,

they are Float values.

---

# Float Example

```python
height = 5.9

print(height)
```

Output

```
5.9
```

---

Another Example

```python
price = 499.99

print(price)
```

Output

```
499.99
```

---

Negative Float

```python
temperature = -7.8

print(temperature)
```

Output

```
-7.8
```

---

# Difference Between Integer and Float

| Integer | Float |
|----------|--------|
| Whole Number | Decimal Number |
| No decimal point | Decimal point present |
| Example: 10 | Example: 10.5 |
| Uses less memory | Uses more memory |
| Used for counting | Used for measurements |

---

# 🌍 Real-Life Comparison

Imagine buying fruits.

Number of Apples

```
5 Apples
```

Integer

Weight of Apples

```
2.75 kg
```

Float

One is counting.

The other is measuring.

---

# Practice Questions

## Easy

1. Create a variable storing your age.

2. Create a variable storing your marks.

3. Store today's temperature.

4. Store the price of a laptop.

5. Store the number of books.

---

## Medium

Create variables for

```
Height

Weight

Salary

Bank Balance

Petrol

Milk Quantity
```

Identify whether each one is Integer or Float.

---

# 🧠 Interview Questions

### Q1 What is a Data Type?

### Q2 Why do computers need Data Types?

### Q3 Difference between Integer and Float?

### Q4 Give three real-life examples of Integer.

### Q5 Give three real-life examples of Float.

---

# 📋 Cheat Sheet

```python
age = 20

marks = 95

temperature = -5

height = 5.9

price = 499.99

weight = 62.5
```

---

# 📝 Summary

✅ Data is information.

✅ Data Types tell Python what kind of information is stored.

✅ Integers store whole numbers.

✅ Floats store decimal numbers.

✅ Every value stored in memory has a type.

✅ Choosing the correct data type makes programs accurate and efficient.

---

# 🎉 Congratulations!

You have completed **Chapter 5 – Part 1**.

In the next part, you'll learn:

- 🔢 Complex Numbers
- ✅ Boolean (`bool`)
- 🔤 Strings (`str`)
- 🧠 How Python stores text in memory
- 🌍 Real-life examples
- 💻 Lots of coding examples


# 📘 Chapter 5 - Data Types in Python (Part 2)

<div align="center">

# 🔢 Complex Numbers | ✅ Boolean | 🔤 Strings

### "Different types of data solve different types of problems."

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- Complex Data Type
- Boolean Data Type
- String Data Type
- String Indexing
- String Slicing
- String Operations
- Escape Characters
- Multiline Strings
- Real-Life Examples
- Practice Questions
- Interview Questions
- Cheat Sheet
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Understand Complex Numbers

✅ Understand Boolean Values

✅ Work with Strings

✅ Access characters from Strings

✅ Slice Strings

✅ Perform String Operations

---

# 🔢 Complex Data Type

Until now we have learned

```
Integer

↓

10

50

100
```

and

```
Float

↓

10.5

25.8

99.99
```

Now let's learn another numeric type.

```
Complex Number
```

---

# 🤔 What is a Complex Number?

A Complex Number contains

```
Real Part

+

Imaginary Part
```

It is written as

```
a + bj
```

where

```
a = Real Number

b = Imaginary Number
```

Python uses **j** instead of **i**.

---

# 🌍 Real-Life Example

Imagine you are walking.

You move

```
5 steps East

+

3 steps North
```

Your movement has two directions.

Similarly,

Complex Numbers have

```
Real Part

+

Imaginary Part
```

---

# Complex Number Example

```python
number = 3 + 4j

print(number)
```

Output

```
(3+4j)
```

---

Another Example

```python
x = 10 + 5j

print(x)
```

Output

```
(10+5j)
```

---

# Where are Complex Numbers Used?

Complex numbers are mostly used in

- Electrical Engineering

- Physics

- Signal Processing

- Robotics

- Artificial Intelligence

- Scientific Computing

For beginner Python programming and DSA,

you will rarely use them.

---

# Important Note

You do **not** need Complex Numbers for most coding interview questions.

Just know they exist.

---

# ✅ Boolean Data Type

Boolean has only **two values**.

```
True

False
```

Nothing else.

---

# 🌍 Real-Life Example

Imagine a light switch.

```
ON

OFF
```

Only two possibilities.

Similarly,

Boolean also has only two values.

```
True

False
```

---

# Another Example

Door Lock

```
Locked

Unlocked
```

Again,

only two states.

---

# Example

```python
is_student = True

print(is_student)
```

Output

```
True
```

---

Another Example

```python
is_raining = False

print(is_raining)
```

Output

```
False
```

---

# Why Do We Need Boolean?

Suppose

A website asks

```
Are you logged in?
```

Answer

```
Yes

or

No
```

Computer stores this as

```
True

False
```

---

# More Examples

```python
is_married = False

is_online = True

is_admin = False

has_license = True
```

---

# Boolean from Comparison

Boolean values are often created by comparing values.

```python
print(10 > 5)
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

```python
print(20 == 20)
```

Output

```
True
```

---

```python
print(15 != 20)
```

Output

```
True
```

---

# Why Boolean is Important?

Almost every decision in programming depends on Boolean.

Example

```
Login Successful?

↓

True

↓

Open Dashboard
```

or

```
False

↓

Show Error
```

---

# 🔤 String Data Type

String means

```
Text
```

Anything written inside

```
" "

or

' '
```

is a String.

---

# 🌍 Real-Life Example

Suppose your name is

```
Rahul
```

Can Python treat it as a number?

No.

It is text.

Therefore,

it is stored as a String.

---

Examples

```
"Rahul"

"Python"

"Hello"

"India"

"123"

"Good Morning"
```

Notice

```
"123"
```

is also a String.

Because it is inside quotes.

---

# Creating Strings

```python
name = "Rahul"

print(name)
```

Output

```
Rahul
```

---

Using Single Quotes

```python
city = 'Indore'

print(city)
```

Output

```
Indore
```

---

Both are correct.

```python
"Python"

'Python'
```

---

# Empty String

```python
text = ""

print(text)
```

Output

```

```

It contains no characters.

---

# String Memory Representation

Suppose

```python
name = "Python"
```

Python stores

```
P

y

t

h

o

n
```

Every character gets an index.

```
P  y  t  h  o  n

0  1  2  3  4  5
```

---

# Negative Indexing

Python also counts from the end.

```
P  y  t  h  o  n

-6 -5 -4 -3 -2 -1
```

Very useful.

---

# Accessing Characters

```python
name = "Python"

print(name[0])
```

Output

```
P
```

---

```python
print(name[3])
```

Output

```
h
```

---

Negative Index

```python
print(name[-1])
```

Output

```
n
```

---

# String Slicing

General Syntax

```python
string[start:end]
```

Python includes

```
start

but

excludes

end
```

---

Example

```python
name = "Python"

print(name[0:3])
```

Output

```
Pyt
```

---

```python
print(name[2:6])
```

Output

```
thon
```

---

```python
print(name[:4])
```

Output

```
Pyth
```

---

```python
print(name[2:])
```

Output

```
thon
```

---

# Reverse String

```python
name = "Python"

print(name[::-1])
```

Output

```
nohtyP
```

This trick is used frequently in DSA.

---

# String Concatenation

Joining Strings.

```python
first = "Hello"

second = "World"

print(first + second)
```

Output

```
HelloWorld
```

---

Adding Space

```python
print(first + " " + second)
```

Output

```
Hello World
```

---

# String Repetition

```python
print("Python " * 3)
```

Output

```
Python Python Python
```

---

# Length of String

```python
name = "Python"

print(len(name))
```

Output

```
6
```

---

# Escape Characters

Sometimes

we want to print quotes.

Example

Wrong

```python
print("I'm Rahul")
```

Correct

```python
print("I\'m Rahul")
```

---

Another Example

```python
print("He said \"Hello\"")
```

Output

```
He said "Hello"
```

---

# Multiline String

```python
text = """
Python

is

Awesome
"""

print(text)
```

Output

```
Python

is

Awesome
```

---

# Practice Questions

## Easy

1. Store your name.

2. Store your city.

3. Print first character.

4. Print last character.

5. Reverse your name.

---

## Medium

Create variables

```
College Name

Branch

Dream Company

Favourite Language
```

Print

- First Letter
- Last Letter
- Length

---

# 🧠 Interview Questions

### Q1 What is Boolean?

### Q2 How many values does Boolean have?

### Q3 Difference between Integer and String?

### Q4 Explain String Indexing.

### Q5 Explain Negative Indexing.

### Q6 Explain String Slicing.

### Q7 Difference between

```
123

and

"123"
```

---

# 📋 Cheat Sheet

```python
number = 3 + 4j

is_student = True

name = "Rahul"

print(name[0])

print(name[-1])

print(name[1:4])

print(name[::-1])

print(len(name))
```

---

# 📝 Summary

✅ Complex Numbers contain a Real Part and an Imaginary Part.

✅ Boolean has only two values: True and False.

✅ Strings store text.

✅ Every character in a String has an index.

✅ Python supports positive and negative indexing.

✅ String slicing allows us to extract part of a string.

✅ Strings can be joined, repeated, and reversed.

---

# 🎉 Congratulations!

You have completed **Chapter 5 – Part 2**.

You now know three important Python data types:

- 🔢 Complex
- ✅ Boolean
- 🔤 String

These will be used extensively in future Python programs and DSA problems.

# 📘 Chapter 5 - Data Types in Python (Part 3A)

<div align="center">

# 🧠 None | type() | id() | Dynamic Typing | Memory

### "Understanding how Python stores data is the first step toward becoming a great programmer."

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What is None?
- Why do we need None?
- Real-Life Examples
- None vs 0 vs False vs Empty String
- The type() Function
- The id() Function
- Memory Representation
- Dynamic Typing
- Variables and References
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Understand None

✅ Use type()

✅ Use id()

✅ Understand Memory Addresses

✅ Understand Dynamic Typing

✅ Understand Variable References

---

# 🤔 What is None?

Imagine you booked a hotel room.

But...

No one has checked in yet.

```
Room 101

↓

Empty
```

The room exists.

But nothing is inside it.

Python has exactly the same concept.

It is called

```
None
```

---

# Definition

**None** represents

> "No value"

It does **NOT** mean

- Zero
- False
- Empty String

It simply means

"There is nothing here."

---

# Real-Life Example

Imagine your school asks

```
Bus Number
```

You don't use the school bus.

What will you write?

```
None
```

Not

```
0
```

because zero is still a number.

---

# Example

```python
student_id = None

print(student_id)
```

Output

```
None
```

---

Another Example

```python
winner = None

print(winner)
```

Output

```
None
```

No winner has been decided yet.

---

# Another Real-Life Example

Suppose you create an online shopping account.

Initially

```
Coupon Code

↓

None
```

Later

```
Coupon Code

↓

SAVE50
```

The variable first stores **None**.

Later it stores a String.

---

# None vs 0

Many beginners think

```
None == 0
```

❌ Wrong

Example

```python
print(None == 0)
```

Output

```
False
```

---

# None vs False

```python
print(None == False)
```

Output

```
False
```

---

# None vs Empty String

```python
print(None == "")
```

Output

```
False
```

---

# Summary Table

| Value | Meaning |
|--------|---------|
| None | No value exists |
| 0 | Number Zero |
| False | Boolean False |
| "" | Empty Text |

They are all different.

---

# 🔍 type() Function

Now let's learn one of Python's most useful functions.

```
type()
```

---

# What is type()?

Imagine someone gives you a box.

You don't know what's inside.

You ask

```
"What type of thing is this?"
```

Python's `type()` function does exactly that.

It tells you the data type of any value.

---

# Example

```python
age = 20

print(type(age))
```

Output

```
<class 'int'>
```

Python says

"This is an Integer."

---

# Float Example

```python
height = 5.9

print(type(height))
```

Output

```
<class 'float'>
```

---

# String Example

```python
name = "Rahul"

print(type(name))
```

Output

```
<class 'str'>
```

---

# Boolean Example

```python
is_student = True

print(type(is_student))
```

Output

```
<class 'bool'>
```

---

# Complex Example

```python
number = 3 + 4j

print(type(number))
```

Output

```
<class 'complex'>
```

---

# None Example

```python
value = None

print(type(value))
```

Output

```
<class 'NoneType'>
```

---

# Why is type() Useful?

Imagine you're writing a calculator.

The user enters

```
20

or

"Twenty"
```

How will your program know?

Using

```python
type()
```

you can check the data before using it.

---

# 🆔 id() Function

Now let's learn something amazing.

Every object in Python has a memory address.

The function

```
id()
```

shows that address.

---

# Real-Life Example

Every house has

```
House Number
```

Example

```
House 105

House 210

House 501
```

Even if two houses look similar,

their addresses are different.

Python objects are similar.

Every object has a unique memory address.

---

# Example

```python
age = 20

print(id(age))
```

Output

```
140239812312
```

The number will be different on every computer.

Don't worry.

It simply represents the memory location.

---

# Another Example

```python
name = "Python"

print(id(name))
```

Output

```
140239812900
```

Again,

the value will be different on your computer.

---

# Memory Representation

Suppose

```python
age = 20
```

Internally

```
Variable

age

↓

Memory Address

0x100

↓

20
```

Now

```python
name = "Rahul"
```

```
Variable

name

↓

Memory Address

0x250

↓

Rahul
```

Variables store a **reference** to an object in memory.

---

# 🌍 Real-Life Example

Imagine a library.

Books are kept on shelves.

Each shelf has a unique number.

```
Shelf 1

↓

Python Book

-----------------

Shelf 2

↓

Math Book
```

The shelf number helps you find the book.

Similarly,

Python uses memory addresses to locate objects.

---

# Dynamic Typing

Python is called a

```
Dynamically Typed Language
```

But what does that mean?

---

# Definition

Python automatically decides the data type.

You don't need to specify it.

---

# Example

```python
x = 10
```

Python automatically understands

```
Integer
```

---

Now

```python
x = "Python"
```

Python changes it to

```
String
```

Same variable.

Different data type.

---

# Real-Life Example

Imagine a whiteboard.

Morning

```
Math Homework
```

Afternoon

Erase

```
Science Homework
```

Evening

Erase

```
Meeting Notes
```

The whiteboard is the same.

Only the content changes.

Variables behave exactly like this.

---

# Example

```python
data = 100

print(data)

data = "Hello"

print(data)

data = True

print(data)
```

Output

```
100
Hello
True
```

Python automatically changes the type.

---

# Variables and References

This is one of the most important concepts.

When you write

```python
name = "Rahul"
```

Many beginners think

```
Variable

↓

Stores

↓

Rahul
```

Actually,

Python stores a **reference** to the object.

```
name

↓

Reference

↓

Memory

↓

"Rahul"
```

The variable points to the object.

---

# Example

```python
x = 50

y = x
```

Memory Diagram

```
x

↓

50

↑

y
```

Both variables refer to the same object.

---

# Checking Memory Address

```python
x = 50
y = x

print(id(x))
print(id(y))
```

Both addresses are usually the same because both variables refer to the same object.

---

# 📝 Summary

✅ `None` means "no value."

✅ `None` is different from `0`, `False`, and `""`.

✅ `type()` tells us the data type of a value.

✅ `id()` returns the memory address of an object.

✅ Python automatically decides data types (Dynamic Typing).

✅ Variables hold references to objects in memory rather than storing the values directly.

---

# 🎉 Congratulations!

You have completed **Chapter 5 – Part 3A**.

You now understand how Python identifies data, stores objects, and connects variables to memory.

This knowledge will make learning **Lists, Dictionaries, Functions, Classes, and DSA** much easier.

# 📘 Chapter 5 – Data Types in Python (Part 3B)

<div align="center">

# 🔥 Mutable vs Immutable in Python

### Understanding How Python Handles Objects in Memory

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What is Mutable?
- What is Immutable?
- Real-Life Examples
- Mutable vs Immutable
- Memory Representation
- Common Mistakes
- Interview Questions
- Practice Questions
- Cheat Sheet
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Understand Mutable and Immutable Objects

✅ Know which Python data types can change

✅ Understand how memory behaves

✅ Avoid common beginner mistakes

---

# 🤔 What is Mutable?

**Mutable** means:

> **An object whose value can be changed after it is created.**

---

# 🌍 Real-Life Example

Imagine a **Notebook**.

You can

- Erase words
- Write new words
- Add pages

The notebook remains the same.

Only its contents change.

```
Notebook

↓

Math Notes

↓

Erase

↓

Science Notes
```

Notebook = Mutable

---

# Python Mutable Data Types

- List
- Dictionary
- Set

---

# Example

```python
numbers = [10, 20, 30]

numbers[1] = 50

print(numbers)
```

Output

```
[10, 50, 30]
```

The same list changed.

---

# 🤔 What is Immutable?

Immutable means

> **An object cannot be changed after it is created.**

If you want a different value,

Python creates a **new object**.

---

# 🌍 Real-Life Example

Imagine your **Date of Birth Certificate**.

You cannot erase your birth date.

If something changes,

a completely new certificate must be issued.

Birth Certificate = Immutable

---

# Python Immutable Data Types

- Integer
- Float
- Boolean
- String
- Tuple
- Complex

---

# Example

```python
name = "Python"

name = "Java"

print(name)
```

Output

```
Java
```

Did Python change "Python"?

❌ No.

It created a **new String object**.

---

# Memory Representation

Example

```python
name = "Python"
```

```
name

↓

Memory A

↓

"Python"
```

Now

```python
name = "Java"
```

Python creates

```
name

↓

Memory B

↓

"Java"
```

The old object is no longer referenced by `name`.

---

# String Example

```python
text = "Hello"

text = text + " World"

print(text)
```

Output

```
Hello World
```

Python created a **new String**.

The old string was not modified.

---

# List Example

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

Output

```
['Apple', 'Banana', 'Mango']
```

The original list changed.

Lists are Mutable.

---

# Mutable vs Immutable

| Mutable | Immutable |
|----------|-----------|
| Can Change | Cannot Change |
| Same Memory | New Memory Created |
| Faster Modification | Creates New Object |
| List | String |
| Dictionary | Integer |
| Set | Float |
| | Boolean |
| | Tuple |

---

# Real-Life Comparison

## Mutable

```
Whiteboard

↓

Write

↓

Erase

↓

Write Again
```

Same board.

Different content.

---

## Immutable

```
Printed Book

↓

Need changes?

↓

Print New Book
```

The old book remains unchanged.

---

# Why Does This Matter?

Understanding Mutable and Immutable objects helps you

- Write better code
- Avoid bugs
- Understand functions
- Learn DSA faster
- Understand memory optimization

---

# Common Beginner Mistakes

## Mistake 1

Thinking Strings are Mutable

Wrong

```python
name = "Python"

name[0] = "J"
```

Output

```
TypeError
```

Strings cannot be modified.

---

## Mistake 2

Thinking Lists are Immutable

```python
numbers = [1, 2, 3]

numbers[0] = 100
```

Correct ✅

Lists can be modified.

---

## Mistake 3

Confusing Assignment with Modification

```python
x = 10

x = 20
```

Python creates a new object.

It does not change the old integer.

---

# 🧠 Interview Questions

### Q1. What is Mutable?

### Q2. What is Immutable?

### Q3. Is String Mutable?

### Q4. Is List Mutable?

### Q5. Difference between List and Tuple?

### Q6. Why are Strings Immutable?

### Q7. Give examples of Mutable objects.

### Q8. Give examples of Immutable objects.

---

# 💻 Practice Questions

## Easy

1. Create a List and modify it.

2. Create a String and reassign it.

3. Create a Tuple.

4. Create a Dictionary.

5. Create a Set.

---

## Medium

Identify whether each is Mutable or Immutable.

```
10

5.5

"Python"

True

[1,2,3]

(1,2,3)

{"name":"Rahul"}

{1,2,3}
```

---

# 📋 Cheat Sheet

```python
# Mutable

list

dictionary

set

# Immutable

int

float

bool

str

tuple

complex

# Check Data Type

type(value)

# Check Memory Address

id(value)
```

---

# 📝 Chapter 5 Summary

In this chapter, you learned:

✅ Integer (`int`) – Whole Numbers

✅ Float (`float`) – Decimal Numbers

✅ Complex (`complex`) – Real + Imaginary Numbers

✅ Boolean (`bool`) – True or False

✅ String (`str`) – Text Data

✅ None – Represents No Value

✅ `type()` – Checks the Data Type

✅ `id()` – Returns the Memory Address

✅ Dynamic Typing – Python Automatically Detects Data Types

✅ Mutable Objects – Can Be Modified

✅ Immutable Objects – Cannot Be Modified

---

# 🎯 Final Assignment

Create variables for the following:

```python
name = "Rahul"
age = 20
height = 5.8
is_student = True
marks = [90, 85, 95]
address = {
    "city": "Indore",
    "state": "Madhya Pradesh"
}
subjects = ("Python", "DSA")
```

For each variable:

- Print its value
- Print its data type using `type()`
- Print its memory address using `id()`
- Identify whether it is **Mutable** or **Immutable**

---

# 🎉 Congratulations!

You have successfully completed **Chapter 5 – Data Types in Python**.

You now understand:

- ✔ Python's built-in data types
- ✔ How Python stores data
- ✔ Memory addresses
- ✔ Dynamic typing
- ✔ Mutable vs Immutable objects

These concepts form the foundation for learning **Lists, Tuples, Dictionaries, Functions, Object-Oriented Programming, and Data Structures & Algorithms**.

🚀 **Next Chapter:** **Chapter 6 – Input and Output (User Interaction in Python)**

