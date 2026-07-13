# 📘 DSA in Python - Phase 1: Arrays
# Chapter 1 - Introduction to Arrays

> **Learning Goal**
>
> By the end of this chapter, you will understand:
>
> - What an Array is
> - Why Arrays are needed
> - Real-life applications
> - Advantages and disadvantages
> - Arrays vs Variables
> - Arrays in Python
> - Important Terminology
> - Time & Space Complexity Basics
> - Interview Questions
> - Practice Exercises

---

# 📖 What is an Array?

An **Array** is one of the most fundamental data structures in Computer Science.

It is used to store **multiple values** inside a single variable.

Instead of creating many separate variables, we store everything together in one collection.

---

## Example Without Array

```python
student1 = "Rahul"
student2 = "Aman"
student3 = "Priya"
student4 = "Neha"
student5 = "Karan"
```

Imagine storing **10,000 students** like this.

Impossible.

---

## Example Using Array (Python List)

```python
students = [
    "Rahul",
    "Aman",
    "Priya",
    "Neha",
    "Karan"
]
```

Everything is stored inside one variable.

This is much easier to manage.

---

# 🌍 Real-Life Analogy

Imagine a train.

```
+---------+---------+---------+---------+
| Coach 1 | Coach 2 | Coach 3 | Coach 4 |
+---------+---------+---------+---------+
```

Every coach has a position.

Similarly,

An array stores elements in continuous order.

Every element has a position called an **Index**.

---

# 🏫 Another Example

Suppose your classroom attendance register is:

```
Roll No     Student

1           Rahul
2           Aman
3           Priya
4           Neha
```

If teacher asks,

> "Call Roll Number 3."

You immediately know the answer.

Arrays work exactly like this.

Instead of Roll Number,

Computers use **Index**.

---

# 🧠 Definition

An Array is

> A linear data structure that stores multiple elements in sequential order.

Each element can be accessed using its **Index**.

---

# 📦 Visual Representation

```
Index

0      1      2      3      4

+----+----+----+----+----+
|10  |20  |30  |40  |50  |
+----+----+----+----+----+
```

Value **10** is stored at Index **0**

Value **20** is stored at Index **1**

Value **30** is stored at Index **2**

---

# 📌 Important Terminology

## 1. Element

The data stored inside an array.

Example

```
[10,20,30]
```

10 is an element

20 is an element

30 is an element

---

## 2. Index

The position of an element.

```
Value      Index

10          0
20          1
30          2
40          3
```

---

## 3. Length

Total number of elements inside an array.

Example

```python
numbers = [10,20,30,40]
```

Length = 4

---

# 🤔 Why Does Index Start From 0?

This is one of the most common interview questions.

Computers store data in memory.

Suppose

```
Base Address = 1000
```

Each integer takes 4 bytes.

Index 0

```
1000 + (0 × 4)

=1000
```

Index 1

```
1000 + (1 × 4)

=1004
```

Index 2

```
1000 + (2 × 4)

=1008
```

The formula is

```
Address = Base Address + (Index × Size)
```

That's why indexing starts from **0**.

---

# 🎯 Why Do We Need Arrays?

Suppose you are storing marks of students.

Without Array

```python
mark1 = 90
mark2 = 80
mark3 = 70
mark4 = 95
```

With Array

```python
marks = [90,80,70,95]
```

Much simpler.

Now imagine storing marks of 1 lakh students.

Arrays make this possible.

---

# 💻 Arrays in Python

Python does not have a traditional array like C.

Instead,

Python uses **List**.

For DSA,

List is treated as an Array.

Example

```python
numbers = [10,20,30,40]
```

---

# 📝 Creating Arrays

Integer Array

```python
numbers = [1,2,3,4,5]
```

String Array

```python
names = [
    "Rahul",
    "Aman",
    "Neha"
]
```

Float Array

```python
prices = [
    25.5,
    10.2,
    99.8
]
```

Mixed Data Types

```python
data = [
    10,
    "Python",
    99.5,
    True
]
```

---

# 🌎 Real-Life Applications

Arrays are everywhere.

## Instagram

Posts

```
Post1

Post2

Post3
```

---

## YouTube

Recommended Videos

```
Video1

Video2

Video3
```

---

## Amazon

Products

```
Product1

Product2

Product3
```

---

## Netflix

Movies

```
Movie1

Movie2

Movie3
```

---

## Cricket Score

Runs

```
[10,25,40,60,80]
```

---

## Student Marks

```
[90,88,75,60]
```

---

# ✅ Advantages

- Easy to store multiple values
- Fast indexing
- Memory efficient
- Simple traversal
- Easy sorting
- Easy searching

---

# ❌ Disadvantages

- Fixed size in many languages
- Insertion in middle is costly
- Deletion is costly
- Search is slow in unsorted arrays

---

# 📊 Time Complexity (Overview)

| Operation | Complexity |
|------------|------------|
| Access | O(1) |
| Search | O(n) |
| Update | O(1) |
| Insert End | O(1)* |
| Insert Beginning | O(n) |
| Delete | O(n) |

(*Amortized for Python List)

---

# 📌 Array vs Variable

| Variable | Array |
|-----------|-------|
| Stores one value | Stores multiple values |
| Many variables required | Single variable required |
| Difficult to manage | Easy to manage |
| No indexing | Indexing available |

---

# 📌 Array vs Python List

| Array | Python List |
|--------|-------------|
| Same data type | Mixed data types allowed |
| Less flexible | Highly flexible |
| Used in C/Java | Used in Python |

---

# 💻 Python Example

```python
numbers = [10,20,30,40,50]

print(numbers)
```

Output

```
[10,20,30,40,50]
```

---

# 🎯 Interview Questions

### Q1 What is an Array?

### Q2 Why do indexes start from 0?

### Q3 Difference between Variable and Array?

### Q4 Difference between Array and Python List?

### Q5 Advantages of Arrays?

### Q6 Disadvantages of Arrays?

---

# 🧠 Summary

✔ Array stores multiple values.

✔ Every element has an index.

✔ Index starts from 0.

✔ Python uses Lists as Arrays.

✔ Arrays are linear data structures.

✔ Arrays allow fast access using indexes.

---

# 📝 Practice Questions

## Basic

1. What is an Array?
2. What is an Index?
3. What is an Element?
4. Why do indexes start from 0?
5. Difference between Array and Variable?

---

## Coding

### Question 1

Create an array of 5 numbers.

### Question 2

Create an array of 5 fruits.

### Question 3

Create an array of 5 cities.

### Question 4

Create an array of student names.

### Question 5

Create a mixed array.

---

# 🏆 Assignment

Write Python programs to create:

- Integer Array
- Float Array
- String Array
- Boolean Array
- Mixed Data Type Array

---

# 📚 What's Next?

➡️ **Chapter 2 – Creating Arrays & Memory Representation**

Topics Covered:

- Creating Arrays
- Memory Layout
- Contiguous Memory
- Indexing
- Positive Indexing
- Accessing Elements
- Practice Problems
- Interview Questions