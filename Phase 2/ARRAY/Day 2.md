# 📘 DSA in Python - Phase 1: Arrays
# Chapter 2 - Creating Arrays & Memory Representation

> ## 🎯 Learning Objectives
>
> By the end of this chapter, you will be able to:
>
> - Create arrays in Python
> - Understand how arrays are stored in memory
> - Understand contiguous memory allocation
> - Learn indexing
> - Access elements using indexes
> - Differentiate positive and negative indexing
> - Understand why random access is O(1)
> - Solve beginner-level problems

---

# 📖 Introduction

In the previous chapter, we learned what an Array is.

Now, it's time to create arrays and understand **how the computer stores them in memory**.

This is one of the most important concepts in Data Structures.

If you understand this chapter properly, every future Array topic will become much easier.

---

# 🌍 Real-Life Example

Imagine a hotel.

```
Room No.

101
102
103
104
105
```

Every room has:

- A fixed location
- A unique room number
- Easy access

If someone asks,

> "Who is in Room 103?"

The receptionist directly goes to Room 103.

No need to check every room.

Arrays work in exactly the same way.

Every element has its own location.

That location is called an **Index**.

---

# 📝 Creating Arrays in Python

Python uses **Lists** as Arrays.

## Example 1

```python
numbers = [10, 20, 30, 40, 50]
```

Output

```
[10, 20, 30, 40, 50]
```

---

## Example 2

```python
fruits = ["Apple", "Mango", "Banana"]
```

---

## Example 3

```python
prices = [10.5, 25.75, 99.99]
```

---

## Example 4

```python
is_pass = [True, False, True]
```

---

## Example 5

Mixed Data Types

```python
data = [10, "Python", 95.5, True]
```

Although Python allows mixed data types, for DSA we generally use arrays containing the **same type of data**.

---

# 📦 Memory Representation

Suppose we have

```python
numbers = [10, 20, 30, 40, 50]
```

Inside memory, it looks conceptually like this:

```
Index

0      1      2      3      4

+----+----+----+----+----+
|10  |20  |30  |40  |50  |
+----+----+----+----+----+
```

Each box stores one value.

Each value has an index.

---

# 💾 Contiguous Memory

One of the biggest characteristics of an array is:

> **Elements are stored in contiguous (continuous) memory locations.**

Imagine five houses built side by side.

```
🏠🏠🏠🏠🏠
```

No gaps.

Arrays are stored similarly.

```
Memory

1000
1004
1008
1012
1016
```

Each element occupies the next available memory location.

This continuous storage makes arrays extremely fast for accessing data.

---

# 🧠 Memory Address Calculation

Suppose

```
Base Address = 1000
```

Each integer occupies **4 bytes**.

Then,

```
Index 0

1000 + (0 × 4)

=1000
```

---

```
Index 1

1000 + (1 × 4)

=1004
```

---

```
Index 2

1000 + (2 × 4)

=1008
```

---

General Formula

```
Address

=

Base Address

+

(Index × Size of Data Type)
```

This formula is why arrays support **Random Access**.

---

# 🚀 Random Access

Suppose you want the element at Index 4.

The computer directly calculates its address.

It does **NOT** check every previous element.

This makes array access extremely fast.

Time Complexity

```
O(1)
```

Constant Time.

---

# 📌 Indexing

Every element has a position.

```
Index

0      1      2      3      4

+----+----+----+----+----+
|10  |20  |30  |40  |50  |
+----+----+----+----+----+
```

Example

```python
numbers = [10,20,30,40,50]
```

Access first element

```python
print(numbers[0])
```

Output

```
10
```

---

Access second element

```python
print(numbers[1])
```

Output

```
20
```

---

Access last element

```python
print(numbers[4])
```

Output

```
50
```

---

# ❌ Invalid Index

```python
numbers = [10,20,30]
```

```
print(numbers[5])
```

Output

```
IndexError
```

Because index 5 does not exist.

---

# 📌 Positive Indexing

Positive indexing starts from the beginning.

```
Index

0

1

2

3

4
```

Example

```python
cities = [
    "Delhi",
    "Mumbai",
    "Indore",
    "Pune",
    "Jaipur"
]
```

```
cities[0]
```

Output

```
Delhi
```

---

```
cities[2]
```

Output

```
Indore
```

---

# 📌 Negative Indexing

Python provides another feature.

Negative indexing starts from the end.

```
Index

-5 -4 -3 -2 -1

+----+----+----+----+----+
|10  |20  |30  |40  |50  |
+----+----+----+----+----+
```

Example

```python
numbers = [10,20,30,40,50]
```

Last element

```python
print(numbers[-1])
```

Output

```
50
```

Second Last

```python
print(numbers[-2])
```

Output

```
40
```

Third Last

```python
print(numbers[-3])
```

Output

```
30
```

---

# 📊 Positive vs Negative Index

| Positive | Negative | Value |
|-----------|-----------|------|
|0|-5|10|
|1|-4|20|
|2|-3|30|
|3|-2|40|
|4|-1|50|

---

# 🎯 Accessing Multiple Elements

```python
numbers = [10,20,30,40,50]
```

```python
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

# 💡 Interview Question

### Why is accessing an array element O(1)?

Answer:

Because the computer directly calculates the memory address using

```
Address = Base + Index × Size
```

No searching is required.

---

# 💡 Common Mistakes

### Mistake 1

```python
numbers = [10,20,30]

print(numbers[3])
```

Wrong.

Valid indexes are

```
0
1
2
```

---

### Mistake 2

Confusing value with index.

```
numbers[20]
```

means

Index 20

NOT

Value 20.

---

### Mistake 3

Thinking negative indexing starts from 0.

It starts from

```
-1
```

---

# 📝 Practice Programs

## Program 1

Create an integer array.

```python
numbers = [10,20,30,40,50]

print(numbers)
```

---

## Program 2

Access first element.

```python
numbers = [10,20,30]

print(numbers[0])
```

---

## Program 3

Access last element.

```python
numbers = [10,20,30]

print(numbers[-1])
```

---

## Program 4

Print every element using indexing.

```python
numbers = [5,10,15,20]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
```

---

# 🎯 Interview Questions

### Q1 What is indexing?

### Q2 Why does indexing start from 0?

### Q3 What is contiguous memory?

### Q4 Explain Random Access.

### Q5 Difference between positive and negative indexing.

### Q6 Why is array access O(1)?

---

# 🏆 Assignment

## Theory

1. Define contiguous memory.
2. Explain indexing.
3. What is Random Access?
4. Why is array access O(1)?
5. Difference between positive and negative indexing.

---

## Coding

### Question 1

Create an array of 10 numbers.

---

### Question 2

Print the first element.

---

### Question 3

Print the last element using negative indexing.

---

### Question 4

Print the third element.

---

### Question 5

Print the second last element.

---

### Question 6

Create an array of five cities and print each city using indexing.

---

# 🧠 Summary

✔ Python uses Lists as Arrays.

✔ Arrays conceptually store elements in contiguous memory.

✔ Every element has an index.

✔ Positive indexing starts from 0.

✔ Negative indexing starts from -1.

✔ Arrays support Random Access.

✔ Accessing any element takes O(1) time.

✔ Invalid indexes raise an IndexError.

---

# 📚 Next Chapter

## ➡️ Chapter 3 – Traversing Arrays

Topics:

- What is Traversal?
- for Loop Traversal
- while Loop Traversal
- Enumerate Function
- Forward Traversal
- Reverse Traversal
- Time Complexity
- Dry Run
- Practice Problems
- Interview Questions