# 📘 Chapter 14 – Recursion in Python

<div align="center">

# 🔄 Recursion in Python

### "A function calling itself until a stopping condition is reached."

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What is Recursion?
- Why Learn Recursion?
- Real-Life Example
- How Recursion Works
- Base Case
- Recursive Case
- Call Stack
- Dry Run
- Factorial Example
- Fibonacci Example
- Advantages
- Disadvantages
- Common Mistakes
- Interview Questions
- Practice Questions
- Cheat Sheet
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Understand Recursion

✅ Identify Base Case

✅ Write Recursive Functions

✅ Understand the Call Stack

✅ Dry Run Recursive Programs

---

# 🤔 What is Recursion?

Recursion is a programming technique where

> **A function calls itself** until a stopping condition is reached.

Instead of solving the entire problem at once,

it solves a smaller version of the same problem.

---

# 🌍 Real-Life Example 1 – Russian Dolls

Imagine Russian Dolls.

```
Big Doll

↓

Medium Doll

↓

Small Doll

↓

Smallest Doll
```

To reach the smallest doll,

you keep opening the current doll.

This is recursion.

---

# 🌍 Real-Life Example 2 – Climbing Stairs

Imagine climbing 5 stairs.

```
Step 5

↓

Step 4

↓

Step 3

↓

Step 2

↓

Step 1
```

You reach the top by repeating the same action.

Recursion works similarly.

---

# Why Learn Recursion?

Many important algorithms use recursion.

Examples

- Factorial
- Fibonacci
- Binary Search
- Merge Sort
- Quick Sort
- Tree Traversal
- Graph DFS
- Backtracking
- Dynamic Programming

---

# How Recursion Works

Every recursive function has **two important parts**.

```
1. Base Case

↓

2. Recursive Case
```

Without a Base Case,

the function never stops.

---

# Base Case

The Base Case is the stopping condition.

It tells Python

```
"Stop calling the function."
```

Example

```python
if n == 0:
    return
```

---

# Recursive Case

The Recursive Case is where

the function calls itself.

Example

```python
countdown(n-1)
```

---

# General Structure

```python
def function(n):

    if base_case:
        return

    function(smaller_problem)
```

---

# 🌍 Real-Life Example

Imagine looking for a book in a stack.

```
Book 5

↓

Book 4

↓

Book 3

↓

Book 2

↓

Book 1
```

You remove one book at a time until you reach the desired one.

Each step is similar to a recursive call.

---

# Example 1 – Countdown

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n-1)

countdown(5)
```

Output

```
5
4
3
2
1
```

---

# Dry Run

```
countdown(5)

↓

Print 5

↓

countdown(4)

↓

Print 4

↓

countdown(3)

↓

Print 3

↓

countdown(2)

↓

Print 2

↓

countdown(1)

↓

Print 1

↓

countdown(0)

↓

Stop
```

---

# Call Stack

Python keeps track of function calls using a **Call Stack**.

Think of it like a stack of plates.

```
Top

countdown(1)

countdown(2)

countdown(3)

countdown(4)

countdown(5)

Bottom
```

The last function called is the first one to finish.

This is called

**LIFO (Last In, First Out)**.

---

# Example 2 – Factorial

Factorial means

```
5!

↓

5 × 4 × 3 × 2 × 1

↓

120
```

---

# Recursive Formula

```
n!

↓

n × (n-1)!
```

---

# Python Code

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)

print(factorial(5))
```

Output

```
120
```

---

# Dry Run

```
factorial(5)

↓

5 × factorial(4)

↓

5 × 4 × factorial(3)

↓

5 × 4 × 3 × factorial(2)

↓

5 × 4 × 3 × 2 × factorial(1)

↓

5 × 4 × 3 × 2 × 1

↓

120
```

---

# Call Stack Visualization

```
factorial(5)

↓

factorial(4)

↓

factorial(3)

↓

factorial(2)

↓

factorial(1)

↓

factorial(0)

↓

Return 1

↓

Return 1

↓

Return 2

↓

Return 6

↓

Return 24

↓

Return 120
```

---

# Example 3 – Fibonacci Series

Sequence

```
0

1

1

2

3

5

8

13
```

Formula

```
F(n)

↓

F(n-1) + F(n-2)
```

---

# Python Code

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
```

Output

```
8
```

---

# 🌍 Real-Life Example

Imagine a family tree.

Every person has

```
Father

Mother
```

Each parent again has parents.

This branching structure is similar to recursion.

---

# Advantages of Recursion

✅ Cleaner Code

✅ Easy to Solve Tree Problems

✅ Useful in Divide & Conquer

✅ Natural for Recursive Problems

---

# Disadvantages

❌ Uses more memory

❌ Can be slower

❌ Stack Overflow if Base Case is missing

---

# Common Mistakes

## Mistake 1

Forgetting the Base Case.

```python
def hello():

    print("Hi")

    hello()
```

This never stops.

Result

```
RecursionError
```

---

## Mistake 2

Not reducing the problem size.

Wrong

```python
factorial(n)
```

Correct

```python
factorial(n-1)
```

---

## Mistake 3

Returning the wrong value.

Always ensure the recursive call contributes to the final result.

---

# Interview Questions

### Q1. What is Recursion?

### Q2. What is a Base Case?

### Q3. What is a Recursive Case?

### Q4. What is a Call Stack?

### Q5. Difference between Recursion and Loops?

### Q6. What is Stack Overflow?

### Q7. Give two real-life examples of recursion.

---

# Practice Questions

## Easy

1. Print numbers from 1 to N.

2. Print numbers from N to 1.

3. Find Sum of N numbers.

4. Find Factorial.

5. Find Power of a Number.

---

## Medium

1. Fibonacci Number

2. Reverse a String

3. Check Palindrome

4. Count Digits

5. Sum of Digits

---

## Advanced (Later)

- Binary Search
- Merge Sort
- Quick Sort
- Tower of Hanoi
- Tree Traversals
- Backtracking

---

# Cheat Sheet

```python
# Basic Structure

def recursive_function(n):

    if n == 0:
        return

    recursive_function(n-1)

# Factorial

def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)
```

---

# Summary

✅ Recursion means a function calls itself.

✅ Every recursive function must have a Base Case.

✅ The Recursive Case solves a smaller version of the problem.

✅ Python uses a Call Stack to manage recursive calls.

✅ Recursion is widely used in Trees, Graphs, Backtracking, Sorting, and Dynamic Programming.

---

# 🎯 Mini Assignment

Write recursive functions to:

- Print numbers from 1 to N
- Print numbers from N to 1
- Find the sum of first N numbers
- Find the factorial of a number
- Find the nth Fibonacci number
- Reverse a string

---

# 🎉 Congratulations!

You have completed **Chapter 14 – Recursion in Python**.

Recursion is one of the most powerful concepts in programming. Although it may seem difficult at first, mastering it will make advanced DSA topics like Trees, Graphs, Dynamic Programming, and Backtracking much easier.

---

# 🚀 What's Next?

## Chapter 15 – Python Collections (List, Tuple, Set & Dictionary)

You'll learn:

- Lists
- Tuples
- Sets
- Dictionaries
- CRUD Operations
- List Methods
- Tuple Methods
- Set Methods
- Dictionary Methods
- Time Complexity
- Interview Questions
- Practice Problems
- GitHub-ready Markdown