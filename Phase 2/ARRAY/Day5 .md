# 📘 DSA in Python - Phase 1: Arrays
# Chapter 5 - Array Operations (Insertion, Deletion & Update)

> ## 🎯 Learning Objectives
>
> By the end of this chapter, you will understand:
>
> - What Array Operations are
> - Update Operation
> - Insert Operation
> - Delete Operation
> - append()
> - insert()
> - extend()
> - remove()
> - pop()
> - del
> - clear()
> - Time & Space Complexity
> - Real-Life Examples
> - Dry Runs
> - Interview Questions
> - Practice Problems

---

# 📖 Introduction

Arrays are **mutable** in Python.

This means we can change the data stored inside them.

There are three major operations performed on arrays:

1. Update
2. Insertion
3. Deletion

These operations are used almost everywhere in software development.

---

# 🌍 Real-Life Example

Imagine a classroom.

```
Roll No.

1  Rahul
2  Aman
3  Priya
4  Neha
```

Now,

- A new student joins ➜ Insert
- A student leaves ➜ Delete
- A student's name changes ➜ Update

Exactly the same happens in Arrays.

---

# 📦 Initial Array

```
Index

0    1    2    3

+-----+------+-------+------+
|Rahul| Aman | Priya |Neha |
+-----+------+-------+------+
```

---

# Part 1 - Update Operation

## What is Update?

Updating means replacing an existing value with another value.

Example

```
Before

[10,20,30,40]

Update Index 2

↓

After

[10,20,99,40]
```

---

## Python Syntax

```python
array[index] = new_value
```

---

## Example 1

```python
numbers = [10,20,30,40]

numbers[2] = 99

print(numbers)
```

Output

```
[10,20,99,40]
```

---

## Dry Run

```
numbers = [10,20,30,40]

Index = 2

Old Value = 30

↓

New Value = 99

↓

[10,20,99,40]
```

---

## Time Complexity

Updating requires direct access using index.

```
Time Complexity = O(1)
```

Reason

Direct indexing takes constant time because Python lists provide random access. :contentReference[oaicite:0]{index=0}

---

# Part 2 - Insertion Operation

## What is Insertion?

Insertion means adding a new element into the array.

Example

```
Before

[10,20,30]

Insert 15

↓

[10,15,20,30]
```

---

# Method 1 - append()

Adds element at the **end**.

Syntax

```python
array.append(value)
```

Example

```python
numbers = [10,20,30]

numbers.append(40)

print(numbers)
```

Output

```
[10,20,30,40]
```

---

## Visualization

Before

```
10 20 30
```

After

```
10 20 30 40
```

---

## Time Complexity

```
Average = O(1)

Worst Case = O(n)
```

Python lists are implemented as dynamic arrays, so `append()` is amortized **O(1)**, but occasional resizing makes the worst case **O(n)**. :contentReference[oaicite:1]{index=1}

---

# Method 2 - insert()

Insert at any position.

Syntax

```python
array.insert(index,value)
```

Example

```python
numbers = [10,20,30]

numbers.insert(1,15)

print(numbers)
```

Output

```
[10,15,20,30]
```

---

## Visualization

Before

```
10 20 30
```

Insert 15

```
10 15 20 30
```

Notice

20 and 30 shifted one place.

---

## Dry Run

```
Index = 1

Insert = 15

Old

10 20 30

↓

10 15 20 30
```

---

## Time Complexity

```
O(n)
```

Reason

Elements after the insertion index must shift to create space. :contentReference[oaicite:2]{index=2}

---

# Method 3 - extend()

Insert multiple values.

Syntax

```python
array.extend(iterable)
```

Example

```python
numbers = [10,20]

numbers.extend([30,40,50])

print(numbers)
```

Output

```
[10,20,30,40,50]
```

---

# append() vs extend()

```python
numbers = [10,20]

numbers.append([30,40])

print(numbers)
```

Output

```
[10,20,[30,40]]
```

Whereas,

```python
numbers = [10,20]

numbers.extend([30,40])

print(numbers)
```

Output

```
[10,20,30,40]
```

---

# Part 3 - Deletion Operation

Deletion means removing an element.

Python provides multiple methods.

---

# Method 1 - remove()

Remove by value.

Syntax

```python
array.remove(value)
```

Example

```python
numbers = [10,20,30,40]

numbers.remove(20)

print(numbers)
```

Output

```
[10,30,40]
```

---

## Important

If value is not present,

Python raises

```
ValueError
```

because `remove()` deletes the **first matching value** only. :contentReference[oaicite:3]{index=3}

---

## Time Complexity

```
O(n)
```

Reason

Python first searches for the value, then shifts remaining elements. :contentReference[oaicite:4]{index=4}

---

# Method 2 - pop()

Remove using index.

Syntax

```python
array.pop(index)
```

Example

```python
numbers = [10,20,30,40]

numbers.pop(2)

print(numbers)
```

Output

```
[10,20,40]
```

---

Without Index

```python
numbers.pop()
```

Removes last element.

---

## Difference

```
remove()

↓

Needs Value

pop()

↓

Needs Index
```

---

## Time Complexity

```
pop(last)

O(1)

pop(front)

O(n)
```

Removing the last element is constant time, while removing from the front or middle requires shifting elements. :contentReference[oaicite:5]{index=5}

---

# Method 3 - del

Delete using keyword.

Example

```python
numbers = [10,20,30,40]

del numbers[1]

print(numbers)
```

Output

```
[10,30,40]
```

---

Delete entire list

```python
del numbers
```

Now

```python
print(numbers)
```

Produces

```
NameError
```

---

Delete multiple elements

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

# Method 4 - clear()

Remove every element.

```python
numbers = [10,20,30]

numbers.clear()

print(numbers)
```

Output

```
[]
```

The list object still exists—it is simply empty. :contentReference[oaicite:6]{index=6}

---

# Complete Example

```python
numbers = [10,20,30]

numbers.append(40)

numbers.insert(1,15)

numbers.remove(20)

numbers.pop()

numbers[1] = 99

print(numbers)
```

Output

```
[10,99,30]
```

---

# 📊 Time Complexity Table

| Operation | Complexity |
|------------|------------|
| Update | O(1) |
| append() | O(1) Average |
| insert() | O(n) |
| extend() | O(k) |
| remove() | O(n) |
| pop() Last | O(1) |
| pop(Index) | O(n) |
| del | O(n) |
| clear() | O(n) |

(`k` is the number of elements being added.) :contentReference[oaicite:7]{index=7}

---

# ⚠️ Common Mistakes

### Mistake 1

```python
numbers.remove(100)
```

Value not found

↓

```
ValueError
```

---

### Mistake 2

```python
numbers.pop(10)
```

Invalid index

↓

```
IndexError
```

---

### Mistake 3

```python
numbers[10]=100
```

Index does not exist

↓

```
IndexError
```

---

# 💼 Real-Life Applications

## Shopping Cart

```
Add Product

↓

append()
```

Remove Product

```
remove()
```

Update Quantity

```
Update Index
```

---

## WhatsApp Contacts

Add Contact

↓

append()

Delete Contact

↓

remove()

Edit Contact

↓

Update

---

## Student Database

New Student

↓

Insert

Student Leaves

↓

Delete

Correct Name

↓

Update

---

# 🎯 Interview Questions

### Q1 What is the difference between append() and insert()?

### Q2 Difference between remove() and pop()?

### Q3 Difference between del and clear()?

### Q4 Why is insertion at the beginning O(n)?

### Q5 Why is append() generally O(1)?

### Q6 Which deletion method returns the removed element?

Answer:

```
pop()
```

---

# 📝 Practice Questions

## Easy

1. Add one element using append().
2. Insert 50 at index 2.
3. Remove value 30.
4. Delete last element.
5. Delete first element.
6. Clear the array.

---

## Medium

7. Replace every even index with 0.
8. Insert an element at the beginning.
9. Delete the middle element.
10. Delete every alternate element.

---

## Challenge

11. Build a menu-driven program that supports:
   - Insert
   - Delete
   - Update
   - Display
   - Exit

---

# 🏆 Assignment

Create a Student Management Program using Arrays.

Menu

```
1 Add Student

2 Update Student

3 Remove Student

4 Display Students

5 Exit
```

Requirements

✔ Use append()

✔ Use insert()

✔ Use remove()

✔ Use pop()

✔ Use clear()

✔ Use update

---

# 🧠 Summary

✔ Arrays are mutable.

✔ Update changes an existing element.

✔ append() adds at the end.

✔ insert() adds at a specific position.

✔ extend() adds multiple elements.

✔ remove() deletes by value.

✔ pop() deletes by index and returns the removed element.

✔ del removes elements or entire lists.

✔ clear() empties the list without deleting the list object.

---

# 📚 What's Next?

➡️ **Chapter 6 – Array Searching (Linear Search)**

Topics Covered

- What is Searching?
- Linear Search Algorithm
- Step-by-Step Dry Run
- Best, Average & Worst Case
- Time Complexity
- Real-Life Examples
- Python Implementation
- Interview Questions
- Practice Problems