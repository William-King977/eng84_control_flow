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

## `for` loops
The `for` loop is used to iterate over a sequence (data collections, 
strings). They can be modified to iterate a section of code a
set number of times using `range()`.

Iterating through a list
```python
shopping_list = ["bread", "eggs", "milk", "orange"]
for item in shopping_list:
    print(item)
```

To exit a loop early, use `break`
```python
shopping_list = ["bread", "eggs", "milk", "orange"]

# Only outputs "bread", "eggs" and "milk".
for item in shopping_list:
    print(item)
    if item == "milk":
        break
```

Iterating through each character in a string
```python
# Prints each character.
for x in "fruits":
    print(x)
```

Iterating through a dictionary
```python
food_bill = {1: {"name": "Will", "bill": "£1"},
             2: {"name": "King", "bill": "£2"},
             3: {"name": "BigW", "bill": "£3"}}

# Fetching just the value (another dictionary)
for value in food_bill.values():
    print(f"{value['name']} paid {value['bill']}")

# Separating the key and value, same output.
for key, value in food_bill.items():
    print(f"{value['name']} paid {value['bill']}")
```

Using `range()`
```python
# Prints numbers 0 to 9. 
# The loop is run 10 times.
for i in range(10):
    print(i)
```

## `while` loops
The `while` loop executes a section of code until the condition is 
no longer met. Without a way of stopping the condition, 
while loops will run indefinitely.

```python
# Counts down from 10 to 1, and outputs it.
num = 10
while num > 0:
    print(num)
    num -= 1

# Asking for user input until it is valid.
isValid = False
while not isValid:
    name = input("Enter your name: ")
    if name.isalpha():
        isValid = True
        print("This name is valid.")
    else:
        print("Your name must only contain letters.")
        print("Please enter again.")
```