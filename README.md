# Python Control Flow
## Conditional Statements
Conditional statements change the control flow of the program.
 * `if` -  runs a piece of code if the condition is met.
 * `elif` - same as if, but it is checked if the previous
            conditions are not met.
 * `else` - runs if none of the other conditions are met.

```python
age = 18
if age >= 18:
    print("You are an adult.")
elif age < 18:
    print("You are not an adult.")
else:
    print("Oops, something went wrong.")
```

## while loops
While loops execute a section of code until the condition is 
no longer met. Without a stopping condition, while loops will
run indefinitely.
```python
# Counts down from 10 to 1, and outputs it.
num = 10
while num > 0:
    print(num)
    num -= 1
```

## for loops
For loops are used to iterate over a sequence (data collections, 
strings). They can be modified to iterate a section of code a
set number of times using `range()`.

Iterating through data collections
```python
# Iterating through a list
fruits = ["apple", "coconut", "grapes"]
for x in fruits:
    print(fruits)
    
# Iterating a string. Prints each letter.
for x in "king":
    print(x)
```

Using `range()`
```python
# Prints numbers 0 to 9
for i in range(10):
    print(i)
```