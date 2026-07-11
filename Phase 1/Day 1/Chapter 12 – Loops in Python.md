# 📘 Chapter 12 – Loops in Python

<div align="center">

# 🔄 Loops in Python

### "Why repeat yourself when a computer can do it for you?"

🐍 Python 3.x | Beginner Friendly | DSA Preparation

</div>

---

# 📑 Table of Contents

- What is a Loop?
- Why Do We Need Loops?
- Types of Loops
- while Loop
- for Loop
- range() Function
- Nested Loops
- break Statement
- continue Statement
- pass Statement
- Loop else
- Infinite Loop
- Common Mistakes
- Interview Questions
- Practice Questions
- Cheat Sheet
- Summary

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to

✅ Understand loops

✅ Use while loops

✅ Use for loops

✅ Use range()

✅ Write nested loops

✅ Control loops using break and continue

---

# 🤔 What is a Loop?

A **Loop** is used to execute the same block of code **multiple times**.

Instead of writing the same code again and again, we use loops.

---

# 🌍 Real-Life Example

Imagine your teacher says

```
Write

"I will complete my homework."

100 times.
```

Without loops

```
print("I will complete my homework.")
print("I will complete my homework.")
print("I will complete my homework.")
...
100 times
```

Very difficult!

Using a loop

```python
for i in range(100):
    print("I will complete my homework.")
```

Simple and efficient.

---

# Why Do We Need Loops?

Loops help us

- Save time
- Reduce code
- Avoid repetition
- Make programs efficient

---

# Types of Loops

Python has

- while Loop
- for Loop

---

# 1️⃣ while Loop

A **while loop** repeats as long as a condition is **True**.

### Syntax

```python
while condition:
    # code
```

---

# Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```
1
2
3
4
5
```

---

# 🌍 Real-Life Example

Imagine filling a water bottle.

```
Bottle Full?

↓

No

↓

Keep Filling

↓

Yes

↓

Stop
```

Exactly how a while loop works.

---

# Dry Run

```python
count = 1
```

Condition

```
1 <= 5

↓

True
```

Print

```
1
```

Increase

```
count = 2
```

Again

```
2 <= 5

↓

True
```

Continue...

Finally

```
6 <= 5

↓

False

↓

Stop
```

---

# Infinite Loop

If the condition never becomes False,

the loop never stops.

Example

```python
while True:
    print("Hello")
```

⚠️ This runs forever until manually stopped.

---

# 2️⃣ for Loop

A **for loop** is used to iterate over a sequence.

### Syntax

```python
for variable in sequence:
    # code
```

---

# Example

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

# 🌍 Real-Life Example

Imagine attendance.

Teacher calls every student's roll number one by one.

```
1

↓

2

↓

3

↓

4
```

The teacher is iterating through the class list.

---

# range() Function

`range()` generates a sequence of numbers.

---

## range(stop)

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

## range(start, stop)

```python
for i in range(2, 6):
    print(i)
```

Output

```
2
3
4
5
```

---

## range(start, stop, step)

```python
for i in range(2, 11, 2):
    print(i)
```

Output

```
2
4
6
8
10
```

---

# Reverse Loop

```python
for i in range(10, 0, -1):
    print(i)
```

Output

```
10
9
8
7
6
5
4
3
2
1
```

---

# Looping Through a String

```python
name = "Python"

for ch in name:
    print(ch)
```

Output

```
P
y
t
h
o
n
```

---

# Looping Through a List

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

Output

```
10
20
30
```

---

# Nested Loops

A loop inside another loop is called a **Nested Loop**.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Output

```
0 0
0 1
1 0
1 1
2 0
2 1
```

---

# 🌍 Real-Life Example

Imagine a school.

Each class has many students.

```
Class 1

↓

Student 1

Student 2

Student 3

----------------

Class 2

↓

Student 1

Student 2

Student 3
```

Loop for classes

Inside it,

loop for students.

---

# break Statement

`break` immediately exits the loop.

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

Output

```
0
1
2
3
4
```

---

# 🌍 Real-Life Example

Searching for your friend in a crowd.

As soon as you find them,

you stop searching.

That is `break`.

---

# continue Statement

`continue` skips the current iteration.

```python
for i in range(6):

    if i == 3:
        continue

    print(i)
```

Output

```
0
1
2
4
5
```

---

# 🌍 Real-Life Example

Teacher checks homework.

One student is absent.

Teacher skips that student and continues checking others.

---

# pass Statement

`pass` is a placeholder.

It does nothing.

```python
for i in range(5):

    if i == 3:
        pass

    print(i)
```

Used when code is not yet written.

---

# Loop else

Python allows an `else` block with loops.

It executes only if the loop finishes normally.

```python
for i in range(3):
    print(i)
else:
    print("Loop Finished")
```

Output

```
0
1
2
Loop Finished
```

---

# Common Mistakes

## Forgetting to update while loop variable

Wrong

```python
count = 1

while count <= 5:
    print(count)
```

Infinite Loop

Correct

```python
count += 1
```

---

## Wrong range()

```python
range(5)
```

Produces

```
0 1 2 3 4
```

Not

```
1 2 3 4 5
```

---

## Using break instead of continue

Remember

```
break

↓

Stops Loop

----------------

continue

↓

Skips One Iteration
```

---

# Interview Questions

### Q1. What is a Loop?

### Q2. Difference between while and for?

### Q3. What is range()?

### Q4. Difference between break and continue?

### Q5. What is an Infinite Loop?

### Q6. What is pass?

### Q7. What is Loop else?

---

# Practice Questions

## Easy

1. Print numbers from 1 to 10.

2. Print even numbers.

3. Print odd numbers.

4. Find sum of first 10 numbers.

5. Print multiplication table.

---

## Medium

1. Reverse a number.

2. Find factorial.

3. Count digits.

4. Check palindrome number.

5. Print Fibonacci series.

---

## Pattern Printing

```
*
**
***
****
*****
```

---

```
*****
****
***
**
*
```

---

```
    *
   ***
  *****
 *******
*********
```

---

# Mini Project

## Guess the Number

```python
secret = 7

while True:

    guess = int(input("Enter Number: "))

    if guess == secret:
        print("Correct!")
        break

    print("Try Again")
```

---

# Cheat Sheet

```python
# while

while condition:
    pass

# for

for i in range(5):
    pass

# range

range(stop)

range(start, stop)

range(start, stop, step)

# break

break

# continue

continue

# pass

pass

# Loop else

for i in range(5):
    pass
else:
    print("Done")
```

---

# Summary

✅ Loops repeat code.

✅ while works using a condition.

✅ for works using sequences.

✅ range() generates numbers.

✅ break exits a loop.

✅ continue skips an iteration.

✅ pass is a placeholder.

✅ Nested loops solve multi-level problems.

---

# 🎯 Mini Assignment

Write a program that

- Prints numbers from **1 to 100**
- Prints all **even numbers**
- Prints all **odd numbers**
- Calculates the **sum of numbers from 1 to 100**
- Prints the **multiplication table** of any number entered by the user
- Prints a **right triangle star pattern**

Example

```
Enter Number : 5

5 x 1 = 5

5 x 2 = 10

...

5 x 10 = 50
```

---

# 🎉 Congratulations!

You have completed **Chapter 12 – Loops in Python**.

You can now repeat tasks efficiently, control loop execution using `break`, `continue`, and `pass`, and solve many beginner-level programming and DSA problems using loops.

---

# 🚀 What's Next?

## Chapter 13 – Functions in Python

You'll learn:

- What are Functions?
- Why Functions are Important
- Defining Functions
- Calling Functions
- Parameters & Arguments
- Return Statement
- Local vs Global Variables
- Recursion (Introduction)
- Lambda Functions (Introduction)
- Best Practices
- Interview Questions
- Practice Problems