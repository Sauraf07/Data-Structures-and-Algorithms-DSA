# 📘 DSA in Python - Phase 1: Arrays
# Chapter 6 - Array Operations (Part 1)
## Update & Insert Operations

> **Learning Objectives**
>
> After completing this chapter, you will be able to:
>
> - Understand Array Operations
> - Update an existing element
> - Insert elements at different positions
> - Understand memory shifting
> - Analyze Time & Space Complexity
> - Solve beginner interview questions
> - Practice insertion-based coding problems

---

# 📚 Table of Contents

1. Introduction to Array Operations
2. Types of Operations
3. Update Operation
4. Insert Operation
5. Insert at End
6. Insert at Beginning
7. Insert at Middle
8. Memory Shifting
9. Time Complexity
10. Common Mistakes
11. Interview Questions
12. Practice Questions
13. Assignment

---

# 📖 Introduction

An array is useful only when we can modify its data.

There are three fundamental operations performed on every array.

```
Update
Insert
Delete
```

Every array interview question is built around these three operations.

---

# 🌍 Real Life Example

Imagine a classroom.

```
Roll No.

1 Rahul
2 Aman
3 Priya
4 Neha
```

Now suppose

Rahul changes his name

➡ Update

A new student joins

➡ Insert

One student leaves

➡ Delete

Arrays behave exactly the same.

---

# 📌 Types of Array Operations

| Operation | Description |
|-----------|-------------|
| Update | Replace an existing value |
| Insert | Add a new value |
| Delete | Remove an existing value |

---

# 🎯 Operation 1 - Update

## What is Update?

Updating means changing an existing element without changing the size of the array.

---

## Example

Before

```
Index

0   1   2   3

+----+----+----+----+
|10  |20  |30  |40  |
+----+----+----+----+
```

Update index **2**

```
30 → 100
```

After

```
+----+----+-----+----+
|10  |20  |100  |40  |
+----+----+-----+----+
```

---

## Python Code

```python
numbers = [10,20,30,40]

numbers[2] = 100

print(numbers)
```

Output

```python
[10,20,100,40]
```

---

# Dry Run

```
numbers = [10,20,30,40]

numbers[2] = 100
```

Step 1

```
Index 2

↓

30
```

Step 2

Replace

```
30

↓

100
```

Final Array

```
[10,20,100,40]
```

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Update | O(1) |

### Why?

Because the computer already knows the exact memory location using the index. Setting a list item by index is a constant-time operation. Python lists are backed by arrays, allowing direct indexed access.¹

---

# Space Complexity

```
O(1)
```

No extra memory is used.

---

# 🎯 Operation 2 - Insert

Insertion means adding a new element into an existing array.

There are three possible positions.

```
Insert at Beginning

Insert at Middle

Insert at End
```

---

# 🌍 Real Life Example

Imagine a queue.

```
Rahul

Aman

Priya
```

Now

Neha joins.

She can stand

- At the front
- In the middle
- At the end

Exactly the same happens in arrays.

---

# Case 1 - Insert at End

This is the most common insertion.

---

Before

```
+----+----+----+----+
|10  |20  |30  |40  |
+----+----+----+----+
```

Insert

```
50
```

After

```
+----+----+----+----+----+
|10  |20  |30  |40  |50  |
+----+----+----+----+----+
```

---

## Python Code

```python
numbers = [10,20,30,40]

numbers.append(50)

print(numbers)
```

Output

```python
[10,20,30,40,50]
```

---

### How append() Works

Python's `append()` adds the new item to the end of the list. Internally, Python lists keep extra allocated space whenever possible, making most append operations **amortized O(1)**.²³

---

# Time Complexity

```
O(1) (Amortized)
```

---

# Space Complexity

```
O(1)
```

---

# Case 2 - Insert at Beginning

Before

```
+----+----+----+----+
|10  |20  |30  |40  |
+----+----+----+----+
```

Insert

```
5
```

After

```
+----+----+----+----+----+
|5   |10  |20  |30  |40  |
+----+----+----+----+----+
```

Notice

Every element shifts one position to the right.

---

## Visual Explanation

```
Before

10
20
30
40

↓

Insert 5

↓

5
10
20
30
40
```

---

## Python Code

```python
numbers = [10,20,30,40]

numbers.insert(0,5)

print(numbers)
```

Output

```python
[5,10,20,30,40]
```

---

# Dry Run

```
[10,20,30,40]
```

Insert

```
5
```

Shift

```
40 → Right

30 → Right

20 → Right

10 → Right
```

Final

```
[5,10,20,30,40]
```

---

# Time Complexity

```
O(n)
```

### Why?

Every existing element must shift one position to make room for the new value. Python documentation notes that inserting at the front requires moving all following elements.¹²

---

# Case 3 - Insert in Middle

Before

```
+----+----+----+----+
|10  |20  |40  |50  |
+----+----+----+----+
```

Insert

```
30
```

at Index 2

After

```
+----+----+----+----+----+
|10  |20  |30  |40  |50  |
+----+----+----+----+----+
```

---

## Python Code

```python
numbers = [10,20,40,50]

numbers.insert(2,30)

print(numbers)
```

Output

```python
[10,20,30,40,50]
```

---

# Dry Run

Before

```
10

20

40

50
```

Shift

```
40 → Right

50 → Right
```

Insert

```
30
```

Final

```
10

20

30

40

50
```

---

# Time Complexity

```
O(n)
```

Remaining elements must shift one position to the right.²

---

# 🧠 Memory Shifting Concept

This is one of the most important interview concepts.

Suppose

```
Index

0 1 2 3

10

20

30

40
```

Insert

```
25
```

at Index 2

Memory becomes

```
10

20

25

30

40
```

Notice

```
30 shifted

40 shifted
```

Because of shifting,

Insertion is not O(1).

---

# 📊 Time Complexity Summary

| Operation | Complexity |
|-----------|------------|
| Update | O(1) |
| Append | O(1) Amortized |
| Insert at Beginning | O(n) |
| Insert at Middle | O(n) |
| Insert at End (append) | O(1) Amortized |

---

# 📌 Space Complexity

| Operation | Complexity |
|-----------|------------|
| Update | O(1) |
| Insert | O(1) Extra Space |

---

# 🚨 Common Mistakes

## Mistake 1

```python
numbers[10] = 50
```

Output

```
IndexError
```

Reason

Index does not exist.

---

## Mistake 2

```python
numbers.insert(100,50)
```

Python does **not** raise an error. If the index is larger than the list length, the element is appended to the end.¹

---

## Mistake 3

```python
numbers.append([50])
```

Output

```python
[10,20,30,[50]]
```

Instead of

```python
[10,20,30,50]
```

---

# 🎯 Interview Questions

### Q1

What is the difference between Update and Insert?

---

### Q2

Why is Update O(1)?

---

### Q3

Why is insertion at the beginning O(n)?

---

### Q4

Why is append() faster than insert()?

---

### Q5

What happens internally during insertion?

---

# 📝 Practice Questions

## Easy

1. Update the first element.
2. Update the last element.
3. Update every even index.
4. Insert at the beginning.
5. Insert at the end.
6. Insert at index 3.
7. Insert five values one by one.

---

## Medium

8. Insert an element after every even number.
9. Insert an element before every odd number.
10. Insert an element into a sorted array.
11. Insert without using `insert()`.
12. Count the number of shifts required during insertion.

---

# 🏆 Assignment

Write Python programs to:

- Update an element.
- Update multiple elements.
- Insert at beginning.
- Insert at middle.
- Insert at end.
- Print the array after every insertion.
- Show how many elements shifted after each insertion.

---

# 🧠 Chapter Summary

- Arrays support **Update**, **Insert**, and **Delete** operations.
- Updating changes an existing value without changing the array size.
- `append()` adds an element to the end and is **amortized O(1)**.
- `insert()` can place an element at any index, but usually requires shifting elements, making it **O(n)**.
- Understanding memory shifting is essential for coding interviews.

---

# 📚 What's Next?

➡ **Chapter 6 (Part 2) – Delete Operations**

Topics Covered:

- `remove()`
- `pop()`
- `del`
- `clear()`
- Memory shifting during deletion
- Time Complexity
- Interview Questions
- Coding Problems

---

## References

1. Python Documentation – List Methods (`append()`, `insert()`, `remove()`, etc.). :contentReference[oaicite:0]{index=0}
2. Python Wiki – Time Complexity of List Operations. :contentReference[oaicite:1]{index=1}
3. Python Reference – `append()` and `insert()` complexity. :contentReference[oaicite:2]{index=2}


# 📘 DSA in Python - Phase 1: Arrays
# Chapter 6 (Part 2) – Array Deletion Operations

> **Learning Goals**
>
> By the end of this chapter, you will understand:
>
> - What is Deletion?
> - Deleting Elements by Value
> - Deleting Elements by Index
> - `remove()`
> - `pop()`
> - `del`
> - `clear()`
> - Memory Shifting Concept
> - Time Complexity Analysis
> - Common Mistakes
> - Interview Questions
> - Practice Problems
> - Assignments

---

# 📖 What is Deletion?

Deletion means **removing one or more elements from an array.**

After deleting an element, the remaining elements shift to fill the empty position because Python lists are implemented as **dynamic arrays**. This shifting is the reason why many deletion operations take **O(n)** time. :contentReference[oaicite:0]{index=0}

---

# 🌍 Real-Life Example

Imagine a classroom.

```
Roll No

1 Rahul
2 Aman
3 Priya
4 Neha
5 Karan
```

Suppose **Priya leaves the class.**

New Attendance

```
Rahul
Aman
Neha
Karan
```

Notice that everyone after Priya moves one position forward.

Exactly the same thing happens inside an array.

---

# 📦 Visual Representation

Before Deletion

```
Index

0    1    2    3    4

+----+----+----+----+----+
|10  |20  |30  |40  |50  |
+----+----+----+----+----+
```

Delete

```
30
```

After

```
+----+----+----+----+
|10  |20  |40  |50  |
+----+----+----+----+
```

Notice

```
40 shifted left

50 shifted left
```

---

# Types of Deletion

Python provides four common ways to remove elements.

```
remove()

pop()

del

clear()
```

---

# Method 1 – remove()

## Definition

`remove()` deletes the **first occurrence** of a given value.

### Syntax

```python
list.remove(value)
```

---

## Example

```python
numbers = [10,20,30,40]

numbers.remove(30)

print(numbers)
```

Output

```python
[10,20,40]
```

---

## Dry Run

Initial

```
[10,20,30,40]
```

Search

```
30 found
```

Delete

```
30 removed
```

Remaining elements shift left.

```
[10,20,40]
```

---

## Important Note

If the value does not exist,

Python raises

```python
ValueError
```

Example

```python
numbers = [10,20,30]

numbers.remove(100)
```

Output

```
ValueError
```

The official Python documentation specifies that `remove()` deletes the first matching value and raises `ValueError` if it cannot find the value. :contentReference[oaicite:1]{index=1}

---

# Time Complexity

| Operation | Complexity |
|------------|------------|
| remove() | O(n) |

Why?

- Search takes O(n)
- Elements shift after deletion

---

# Method 2 – pop()

## Definition

`pop()` removes an element **by index**.

It also **returns** the removed element.

---

### Syntax

```python
list.pop(index)
```

or

```python
list.pop()
```

---

# Pop Last Element

```python
numbers = [10,20,30,40]

removed = numbers.pop()

print(removed)

print(numbers)
```

Output

```
40

[10,20,30]
```

---

# Pop Middle Element

```python
numbers = [10,20,30,40]

numbers.pop(1)

print(numbers)
```

Output

```
[10,30,40]
```

---

# Dry Run

Before

```
10
20
30
40
```

Delete Index

```
1
```

After

```
10
30
40
```

---

# Time Complexity

| Operation | Complexity |
|------------|------------|
| pop() | O(1) |
| pop(index) | O(n) |

Reason

- Last element requires no shifting.
- Middle or first element requires shifting.

Python's list complexity documentation notes that `pop()` from the end is **O(1)**, while `pop(i)` from the middle/front is **O(n)** because later elements must be moved. :contentReference[oaicite:2]{index=2}

---

# Method 3 – del

## Definition

`del` removes an element using its index.

Unlike `pop()`, it **does not return** the removed element.

---

## Syntax

```python
del list[index]
```

---

## Example

```python
numbers = [10,20,30,40]

del numbers[2]

print(numbers)
```

Output

```
[10,20,40]
```

---

# Delete Multiple Elements

```python
numbers = [10,20,30,40,50]

del numbers[1:4]

print(numbers)
```

Output

```
[10,50]
```

---

# Delete Entire List

```python
numbers = [10,20]

del numbers
```

Now the variable no longer exists.

---

# Method 4 – clear()

## Definition

`clear()` removes **every element** from the list.

The list still exists.

---

## Example

```python
numbers = [10,20,30]

numbers.clear()

print(numbers)
```

Output

```
[]
```

According to Python's documentation, `clear()` removes all items and is equivalent to deleting the entire slice (`del a[:]`). :contentReference[oaicite:3]{index=3}

---

# Difference

```
clear()

↓

List still exists

[]
```

```
del list

↓

List itself is deleted
```

---

# Memory Shifting

Before

```
Index

0 1 2 3 4

10 20 30 40 50
```

Delete

```
20
```

After

```
10 30 40 50
```

Memory

```
10

30 ← Shift Left

40 ← Shift Left

50 ← Shift Left
```

This shifting is why deleting near the beginning is expensive.

---

# Why Does Shifting Happen?

Python lists store elements in **contiguous memory**.

```
+----+----+----+----+----+
|10  |20  |30  |40  |50  |
+----+----+----+----+----+
```

If `20` is deleted,

a gap appears.

```
+----+----+----+----+----+
|10  |    |30  |40  |50  |
+----+----+----+----+----+
```

To remove the gap,

every remaining element shifts left.

This is the primary reason deletion from the beginning or middle takes **O(n)** time. :contentReference[oaicite:4]{index=4}

---

# Time Complexity Summary

| Operation | Time Complexity |
|------------|----------------|
| remove() | O(n) |
| pop() | O(1) |
| pop(index) | O(n) |
| del last | O(1) |
| del middle | O(n) |
| clear() | O(n) |

---

# Common Mistakes

## Mistake 1

```python
numbers.pop(100)
```

Output

```
IndexError
```

---

## Mistake 2

```python
numbers.remove(100)
```

Output

```
ValueError
```

---

## Mistake 3

Deleting while traversing

```python
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
```

This may skip elements because the list changes while iterating.

---

# Interview Questions

### Q1

Difference between

```
remove()

pop()
```

---

### Q2

Difference between

```
del

clear()
```

---

### Q3

Why is deleting the first element O(n)?

---

### Q4

Which deletion operation returns the removed value?

---

### Q5

Which method removes by value?

---

### Q6

Which method removes by index?

---

# Practice Questions

## Easy

1. Remove the value 30.
2. Remove the last element.
3. Remove the first element.
4. Delete index 2.
5. Clear the entire list.

---

## Medium

6. Remove all even numbers.
7. Remove all odd numbers.
8. Remove all duplicate values.
9. Delete every alternate element.
10. Remove negative numbers.

---

## Hard

11. Implement `remove()` manually.
12. Implement `pop()` manually.
13. Delete without using Python built-in functions.
14. Shift elements manually after deletion.
15. Build your own delete function.

---

# Assignment

Write Python programs to:

- Delete by value.
- Delete by index.
- Delete last element.
- Delete first element.
- Delete middle element.
- Delete multiple elements.
- Clear an entire list.
- Store removed value using `pop()`.
- Implement deletion manually.
- Compare all deletion methods.

---

# Key Takeaways

- `remove()` deletes the **first matching value**.
- `pop()` deletes by **index** and returns the removed value.
- `del` deletes by **index or slice**.
- `clear()` removes every element while keeping the list object.
- Deleting from the beginning or middle requires **element shifting**, so it is **O(n)**.
- Deleting the last element with `pop()` is **O(1)**.

---

# 📚 Next Chapter

## ➡️ Chapter 6 (Part 3) – Advanced Array Operations

Topics Covered:

- extend()
- copy()
- reverse()
- sort()
- count()
- index()
- Membership Operator (`in`)
- Comparison Operators
- Best Practices
- Interview Questions
- 50+ Practice Problems
- Revision Notes


# 📘 DSA in Python – Phase 1: Arrays
# Chapter 6 (Part 3) – Advanced Array Operations, Interview Preparation & Practice

> **Learning Goals**
>
> By the end of this chapter, you will understand:
>
> - `extend()`
> - `copy()`
> - `reverse()`
> - `reversed()`
> - List Aliasing
> - Shallow Copy
> - Common Mistakes
> - Interview Questions
> - Coding Practice
> - Assignments
> - Revision Notes

---

# 📖 Introduction

So far we have learned:

- Update
- Insert
- Delete

Now we will learn some additional array (Python List) operations that are frequently used in coding interviews and real-world applications.

---

# 1️⃣ extend()

## What is extend()?

`extend()` adds **all elements of another iterable** (list, tuple, set, string, etc.) to the end of the current list.

Unlike `append()`, which adds the entire object as a single element, `extend()` adds each element individually. Python's official documentation defines `extend()` as appending all items from an iterable to the list. :contentReference[oaicite:0]{index=0}

---

## Syntax

```python
list.extend(iterable)
```

---

## Example 1

```python
list1 = [10, 20, 30]
list2 = [40, 50]

list1.extend(list2)

print(list1)
```

### Output

```text
[10, 20, 30, 40, 50]
```

---

## Example 2

```python
fruits = ["Apple", "Mango"]

fruits.extend(["Banana", "Orange"])

print(fruits)
```

Output

```text
['Apple', 'Mango', 'Banana', 'Orange']
```

---

## Visual Representation

Before

```text
List 1

10 20 30

List 2

40 50
```

After

```text
10 20 30 40 50
```

---

## Time Complexity

| Operation | Complexity |
|------------|------------|
| extend() | O(k) |

where **k = number of inserted elements**. :contentReference[oaicite:1]{index=1}

---

# append() vs extend()

## append()

```python
numbers = [10,20]

numbers.append([30,40])

print(numbers)
```

Output

```text
[10,20,[30,40]]
```

---

## extend()

```python
numbers = [10,20]

numbers.extend([30,40])

print(numbers)
```

Output

```text
[10,20,30,40]
```

---

## Difference

| append() | extend() |
|------------|-----------|
| Adds one object | Adds all elements |
| Nested List | Flat List |
| O(1) | O(k) |

---

# 2️⃣ copy()

## What is copy()?

`copy()` creates a **new list** containing the same elements.

The new list has a different memory location.

Python documentation describes it as creating a **shallow copy** of the list. :contentReference[oaicite:2]{index=2}

---

## Syntax

```python
list.copy()
```

---

## Example

```python
numbers = [10,20,30]

new_list = numbers.copy()

print(new_list)
```

Output

```text
[10,20,30]
```

---

## Memory Representation

```text
numbers

↓

[10 20 30]

new_list

↓

[10 20 30]
```

Different memory

Same values

---

## Time Complexity

```text
O(n)
```

Because every element is copied. :contentReference[oaicite:3]{index=3}

---

# Shallow Copy

```python
a = [10,20,30]

b = a.copy()

b[0] = 100

print(a)
print(b)
```

Output

```text
[10,20,30]

[100,20,30]
```

Original list remains unchanged.

---

# Assignment vs Copy

Many beginners make this mistake.

---

## Wrong

```python
a = [10,20,30]

b = a
```

This **does NOT create a new list**.

Both variables point to the same memory. :contentReference[oaicite:4]{index=4}

---

```python
b[0] = 100

print(a)
```

Output

```text
[100,20,30]
```

Original list changed!

---

## Correct

```python
b = a.copy()
```

---

# 3️⃣ reverse()

## What is reverse()?

`reverse()` reverses the elements **in place**.

It changes the original list.

It does **not return** a new list. :contentReference[oaicite:5]{index=5}

---

## Example

```python
numbers = [10,20,30,40]

numbers.reverse()

print(numbers)
```

Output

```text
[40,30,20,10]
```

---

## Visual

Before

```text
10 20 30 40
```

After

```text
40 30 20 10
```

---

## Time Complexity

```text
O(n)
```

Each element participates in reversing. :contentReference[oaicite:6]{index=6}

---

# reversed()

Python also provides

```python
reversed()
```

Example

```python
numbers = [10,20,30]

for num in reversed(numbers):
    print(num)
```

Output

```text
30
20
10
```

Unlike `reverse()`, `reversed()` returns an iterator and leaves the original list unchanged. :contentReference[oaicite:7]{index=7}

---

# reverse() vs reversed()

| reverse() | reversed() |
|------------|------------|
| Changes original list | Doesn't modify list |
| Returns None | Returns iterator |
| In-place | New reverse iteration |

---

# Common Mistakes

## Mistake 1

```python
numbers.reverse()

print(numbers.reverse())
```

Output

```text
None
```

Reason

`reverse()` modifies the list but returns `None`. :contentReference[oaicite:8]{index=8}

---

## Mistake 2

```python
a = [10,20]

b = a

b.append(30)
```

Output

```text
a

[10,20,30]
```

Reason

Both variables refer to the same list.

---

## Mistake 3

```python
numbers.extend(100)
```

Error

```text
TypeError
```

Because `extend()` expects an iterable.

Correct

```python
numbers.extend([100])
```

---

# Summary of Advanced Operations

| Method | Description | Complexity |
|------------|------------|------------|
| append() | Add one element | O(1)* |
| extend() | Add multiple elements | O(k) |
| copy() | Duplicate list | O(n) |
| reverse() | Reverse original list | O(n) |
| reversed() | Reverse iterator | O(1) to create iterator |

*Amortized for Python lists. :contentReference[oaicite:9]{index=9}

---

# Interview Questions

## Easy

1. Difference between append() and extend().
2. Difference between copy() and assignment.
3. Difference between reverse() and reversed().
4. Why does reverse() return None?
5. What is shallow copy?

---

## Medium

6. Why is copy() O(n)?
7. Why is extend() O(k)?
8. Why is reverse() O(n)?
9. Explain aliasing in Python.
10. Explain mutable objects.

---

# Coding Practice

## Question 1

Create two arrays.

Merge them using `extend()`.

---

## Question 2

Create a copy of an array.

Modify the copy.

Print both arrays.

---

## Question 3

Reverse an array using

```python
reverse()
```

---

## Question 4

Print array in reverse using

```python
reversed()
```

---

## Question 5

Show difference between

```python
copy()

assignment
```

---

# Practice Problems

## Beginner

- Reverse an array.
- Copy an array.
- Merge two arrays.
- Append one element.
- Extend another array.

---

## Intermediate

- Reverse without using `reverse()`.
- Copy without using `copy()`.
- Merge three arrays.
- Reverse using loop.
- Check whether two lists share the same memory.

---

## Challenge

- Implement your own `extend()`.
- Implement your own `copy()`.
- Reverse without built-in functions.
- Compare execution of `append()` vs `extend()`.
- Demonstrate aliasing using memory addresses (`id()`).

---

# Assignment

Write Python programs to:

- Use `append()`
- Use `extend()`
- Use `copy()`
- Use `reverse()`
- Use `reversed()`
- Demonstrate aliasing
- Demonstrate shallow copy
- Print memory addresses using `id()`
- Compare outputs of all methods
- Write observations for each program

---

# Quick Revision Notes

✅ `append()` adds one object.

✅ `extend()` adds multiple elements.

✅ `copy()` creates a shallow copy.

✅ `a = b` creates another reference, not a copy.

✅ `reverse()` changes the original list.

✅ `reversed()` returns an iterator.

---

# Cheat Sheet

| Method | Changes Original | Returns Value |
|---------|------------------|---------------|
| append() | ✅ Yes | None |
| extend() | ✅ Yes | None |
| copy() | ❌ No | New List |
| reverse() | ✅ Yes | None |
| reversed() | ❌ No | Reverse Iterator |

---

# Chapter Summary

In this chapter, you learned advanced array (Python List) operations that are essential for interviews and real-world programming:

- How to merge lists with `extend()`
- The difference between `append()` and `extend()`
- How `copy()` creates a shallow copy
- Why assignment (`=`) does not create a new list
- How `reverse()` modifies the original list
- How `reversed()` provides reverse iteration without modifying the original list
- Time complexities and common pitfalls

Mastering these operations will make it much easier to solve array-based interview problems efficiently.

---

# What's Next?

## 📘 Chapter 7 – Linear Search

Topics Covered:

- What is Searching?
- Linear Search Algorithm
- Dry Run
- Time Complexity
- Best, Average & Worst Case
- Searching in Unsorted Arrays
- Searching in Sorted Arrays
- Finding First Occurrence
- Finding Last Occurrence
- Counting Occurrences
- Interview Questions
- 40+ Practice Problems
- Assignments