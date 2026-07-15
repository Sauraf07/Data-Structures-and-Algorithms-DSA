# 📘 DSA in Python - Phase 1: Arrays
# Chapter 4 - Array Traversal (Iteration)

> **Learning Goal**
>
> By the end of this chapter, you will understand:
>
> - What Array Traversal is
> - Why Traversal is important
> - Types of Traversal
> - Traversing using `for` loop
> - Traversing using `while` loop
> - Forward and Reverse Traversal
> - Time Complexity
> - Interview Questions
> - Practice Problems

---

# 📖 What is Array Traversal?

Traversal means **visiting every element of an array one by one**.

Whenever we want to:

- Print all elements
- Calculate sum
- Find maximum
- Find minimum
- Search an element

we first **traverse** the array.

---

# 🌍 Real-Life Example

Imagine you are checking attendance in a classroom.

```
Roll No.

1 Rahul
2 Aman
3 Priya
4 Neha
5 Karan
```

Teacher checks every student one after another.

This is called **Traversal**.

---

# 📦 Visual Representation

```
Array

+----+----+----+----+----+
|10  |20  |30  |40  |50  |
+----+----+----+----+----+

Index

0    1    2    3    4
```

Traversal Order

```
10 → 20 → 30 → 40 → 50
```

---

# 🧠 Why Traversal is Important?

Without traversal we cannot:

✔ Print array

✔ Find largest element

✔ Find smallest element

✔ Calculate sum

✔ Count elements

✔ Search element

Almost every array problem starts with traversal.

---

# 📝 Method 1 – Using for Loop

```python
numbers = [10,20,30,40,50]

for num in numbers:
    print(num)
```

Output

```
10
20
30
40
50
```

This is called **Element Traversal**.

---

# 📝 Method 2 – Using Index

```python
numbers = [10,20,30,40,50]

for i in range(len(numbers)):
    print(numbers[i])
```

Output

```
10
20
30
40
50
```

Here,

```
i = Index

numbers[i] = Element
```

---

# 📝 Dry Run

```
numbers = [10,20,30]
```

Iteration 1

```
i = 0

numbers[0]

Output = 10
```

Iteration 2

```
i = 1

numbers[1]

Output = 20
```

Iteration 3

```
i = 2

numbers[2]

Output = 30
```

Loop Ends.

---

# 📝 Method 3 – Using while Loop

```python
numbers = [10,20,30,40,50]

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1
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

# 🔄 Reverse Traversal

Sometimes interview questions ask you to print array in reverse order.

```
Original

10 20 30 40 50

Reverse

50 40 30 20 10
```

Program

```python
numbers = [10,20,30,40,50]

for i in range(len(numbers)-1,-1,-1):
    print(numbers[i])
```

Output

```
50
40
30
20
10
```

---

# 🔍 Traversal with Index and Value

Sometimes we need both.

```python
numbers = [10,20,30]

for index, value in enumerate(numbers):
    print(index, value)
```

Output

```
0 10
1 20
2 30
```

---

# 📊 Time Complexity

| Operation | Complexity |
|------------|------------|
| Traversal | O(n) |

Why?

Because we visit every element exactly once.

---

# 📦 Space Complexity

```
O(1)
```

No extra memory is used.

---

# 💻 Example 1 – Print All Elements

```python
numbers = [5,10,15,20]

for num in numbers:
    print(num)
```

---

# 💻 Example 2 – Print Index and Element

```python
numbers = [10,20,30]

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])
```

Output

```
Index: 0 Value: 10
Index: 1 Value: 20
Index: 2 Value: 30
```

---

# 💻 Example 3 – Reverse Print

```python
numbers = [1,2,3,4,5]

for i in range(len(numbers)-1,-1,-1):
    print(numbers[i])
```

---

# 💻 Example 4 – Print Even Index Elements

```python
numbers = [10,20,30,40,50]

for i in range(0,len(numbers),2):
    print(numbers[i])
```

Output

```
10
30
50
```

---

# 💻 Example 5 – Print Odd Index Elements

```python
numbers = [10,20,30,40,50]

for i in range(1,len(numbers),2):
    print(numbers[i])
```

Output

```
20
40
```

---

# 🚀 Common Mistakes

### Mistake 1

```python
for i in range(len(numbers)+1):
```

❌ IndexError

Correct

```python
for i in range(len(numbers)):
```

---

### Mistake 2

```python
while i <= len(numbers):
```

❌ Wrong

Correct

```python
while i < len(numbers):
```

---

# 🎯 Interview Questions

### Q1 What is Array Traversal?

### Q2 Why is Traversal important?

### Q3 Difference between

```
for num in numbers
```

and

```
for i in range(len(numbers))
```

### Q4 Time Complexity of Traversal?

### Q5 How do you traverse an array in reverse order?

---

# 📝 Practice Questions

## Easy

1. Print all elements.
2. Print elements using while loop.
3. Print elements in reverse order.
4. Print index and value.
5. Print even index elements.
6. Print odd index elements.

---

## Medium

7. Count total elements.
8. Count even numbers.
9. Count odd numbers.
10. Count positive numbers.
11. Count negative numbers.
12. Count zeros.

---

## Challenge

13. Print every alternate element.
14. Print array from last to first.
15. Traverse array without using `for` loop.

---

# 🏆 Assignment

Write Python programs to:

- Traverse an array using `for` loop.
- Traverse an array using `while` loop.
- Print array in reverse order.
- Print index and value together.
- Print alternate elements.
- Print even index elements.
- Print odd index elements.
- Count total elements.

---

# 🧠 Summary

✔ Traversal means visiting every element one by one.

✔ Traversal is the foundation of almost every array problem.

✔ We can traverse using:

- `for` loop
- `while` loop
- `enumerate()`

✔ Reverse traversal is commonly asked in interviews.

✔ Time Complexity = **O(n)**

✔ Space Complexity = **O(1)**

---

# 📚 What's Next?

➡️ **Chapter 5 – Array Operations (Insertion, Deletion & Update)**

Topics Covered:

- Updating Elements
- Inserting Elements
- Deleting Elements
- append()
- insert()
- remove()
- pop()
- del
- clear()
- Time Complexity of Operations
- Interview Questions