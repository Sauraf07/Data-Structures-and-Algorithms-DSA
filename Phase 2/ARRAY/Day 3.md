# 📘 DSA in Python - Phase 1: Arrays
# Chapter 3 - Array Indexing

> **Learning Goals**
>
> By the end of this chapter, you will understand:
>
> - What is Indexing?
> - Why Indexing is Important
> - Positive Indexing
> - Accessing Elements
> - Updating Elements
> - IndexError
> - Time Complexity
> - Interview Questions
> - Practice Questions

---

# 📖 What is Indexing?

Every element inside an array has a **position**.

This position is called its **Index**.

Think of an index as the **address** of an element.

Instead of searching every element one by one, we can directly access it using its index.

---

# 🌍 Real-Life Example

Imagine a hotel with rooms.

```
Room 0 → Rahul
Room 1 → Aman
Room 2 → Priya
Room 3 → Neha
Room 4 → Karan
```

If someone asks,

> "Who is in Room 2?"

You immediately answer:

```
Priya
```

You don't need to check every room.

Arrays work exactly the same way.

---

# 🧠 Definition

> **Indexing** is the process of accessing an element using its position (index).

---

# 📦 Visual Representation

```
Index

0      1      2      3      4

+----+----+----+----+----+
|10  |20  |30  |40  |50  |
+----+----+----+----+----+
```

| Index | Value |
|------|------|
|0|10|
|1|20|
|2|30|
|3|40|
|4|50|

---

# 📌 Why Does Index Start from 0?

Computers store data in memory.

Suppose

```
Base Address = 1000
```

Each integer occupies 4 bytes.

Formula

```
Address = Base Address + (Index × Size)
```

Example

```
Index 0

1000 + (0 × 4)
=1000
```

```
Index 1

1000 + (1 × 4)
=1004
```

```
Index 2

1000 + (2 × 4)
=1008
```

Since the first element starts exactly at the base address, its offset is **0**.

Therefore, indexing starts from **0**.

---

# 💻 Creating an Array

```python
numbers = [10, 20, 30, 40, 50]
```

---

# 📌 Accessing Elements

Syntax

```python
array[index]
```

Example

```python
numbers = [10,20,30,40,50]

print(numbers[0])
```

Output

```
10
```

---

Second Element

```python
print(numbers[1])
```

Output

```
20
```

---

Third Element

```python
print(numbers[2])
```

Output

```
30
```

---

Last Element

```python
print(numbers[4])
```

Output

```
50
```

---

# 📊 Visualization

```
numbers = [10,20,30,40,50]

            ↓

Index 2

Returns

30
```

---

# 💻 Accessing All Elements

```python
numbers = [10,20,30,40,50]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
```

Output

```
10
20
30
40
50
```

---

# ✏ Updating Elements

Arrays are mutable in Python.

Example

```python
numbers = [10,20,30,40]

numbers[1] = 100

print(numbers)
```

Output

```
[10,100,30,40]
```

---

Another Example

```python
fruits = [
    "Apple",
    "Banana",
    "Orange"
]

fruits[2] = "Mango"

print(fruits)
```

Output

```
['Apple', 'Banana', 'Mango']
```

---

# ❌ Invalid Index

Example

```python
numbers = [10,20,30]

print(numbers[5])
```

Output

```
IndexError:
list index out of range
```

Why?

Because index 5 does not exist.

Available indexes are

```
0
1
2
```

---

# 📌 Common Mistake

Array

```
[10,20,30]
```

Many beginners think

```
10 → Index 1

20 → Index 2

30 → Index 3
```

Wrong ❌

Correct

```
10 → Index 0

20 → Index 1

30 → Index 2
```

Always remember:

> **Index starts from 0.**

---

# 📊 Time Complexity

| Operation | Complexity |
|------------|------------|
| Access by Index | O(1) |
| Update by Index | O(1) |

Reason:

Computer directly calculates the memory address using the index.

No searching is required.

---

# 🌎 Real-Life Applications

## Instagram

```
posts[0]
```

First post.

---

## YouTube

```
videos[3]
```

Fourth recommended video.

---

## Netflix

```
movies[5]
```

Sixth movie.

---

## Student Marks

```python
marks = [80,90,75,88]

print(marks[2])
```

Output

```
75
```

---

# 🎯 Interview Questions

### Q1. What is Indexing?

**Answer**

Indexing is the process of accessing an element using its position.

---

### Q2. Why does indexing start from 0?

Because memory addresses are calculated using offsets.

The first element has an offset of 0.

---

### Q3. What happens if we access an invalid index?

Python raises

```
IndexError
```

---

### Q4. What is the time complexity of indexing?

```
O(1)
```

---

### Q5. Can we update an element using indexing?

Yes.

Example

```python
numbers[2] = 500
```

---

# 💻 Practice Programs

## Program 1

```python
numbers = [5,10,15,20]

print(numbers[0])
print(numbers[3])
```

---

## Program 2

```python
cities = [
    "Delhi",
    "Mumbai",
    "Indore",
    "Patna"
]

print(cities[2])
```

---

## Program 3

```python
marks = [90,85,70]

marks[1] = 95

print(marks)
```

---

## Program 4

```python
languages = [
    "Python",
    "Java",
    "C++"
]

print(languages[1])
```

---

## Program 5

```python
fruits = [
    "Apple",
    "Banana",
    "Orange"
]

fruits[0] = "Mango"

print(fruits)
```

---

# 📝 Practice Questions

## Basic

1. What is an index?
2. Why does indexing start from 0?
3. What is IndexError?
4. What is the time complexity of indexing?
5. Can indexing modify values?

---

## Coding

### Question 1

Create an array of 5 numbers and print the first element.

---

### Question 2

Print the last element of an array.

---

### Question 3

Create an array of student names and print the third student.

---

### Question 4

Replace the second element with 100.

---

### Question 5

Replace the last fruit with "Mango".

---

# 🏆 Assignment

Write Python programs to:

- Print the first element.
- Print the last element.
- Print the middle element.
- Update the first element.
- Update the last element.
- Print every element individually using indexing.
- Try accessing an invalid index and observe the error.

---

# 🧠 Summary

✔ Every element has a unique index.

✔ Index always starts from 0.

✔ Accessing an element using an index takes **O(1)** time.

✔ Arrays can be updated using indexing.

✔ Accessing an invalid index raises an **IndexError**.

✔ Indexing is one of the fastest operations in arrays.

---

# 📚 Next Chapter

➡ **Chapter 4 – Negative Indexing**

Topics Covered:

- What is Negative Indexing?
- Why Python Supports Negative Indexing
- Accessing Elements from the End
- Positive vs Negative Indexing
- Practical Examples
- Common Mistakes
- Practice Questions
- Interview Questions