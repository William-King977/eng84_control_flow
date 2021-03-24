#### Control Flow ####
# if, elif, else
# Conditional statements are used to control the flow of the program
# age = 14
# # if the user is over 15, allow them to buy a ticket
# if age >= 15: # If this condition is met, the print statement will execute
#     print("Thank you, please proceed to your purchase.")
#
# # If the user is under 15, do not allow them to buy a ticket
# elif age < 15:
#     print("Sorry, you are too young to watch this movie.")
#
# # Else block executes if none of the above conditions are met
# else:
#     print("Oops, something went wrong, please try later.")

#### Exercise ####
# As a user, I would like to sell tickets according to the age of the user
# and the category of the movie age = U, PG, 12, 12a, 15, 18
# user input to let us know the age to decide whether to sell the ticket or not
# casting implemented int()
# display the age back to the user with an appropriate message

# Stores movies as a dictionary.
movies = {
    # film : age
    "Predator": 18,
    "The Thing": 18,
    "Ip Man": 15,
    "Jaws": 12,
    "Monster House": 8, # Apparently, PG is an age rating of 8
    "Chicken Run": 0,
    "Flushed Away": 0,
    "The Lorax": 0
}

# Convert movie keys into a set to randomise it.
movies_set = set(movies.keys())
# Sets cannot be accessed by an index, so it is converted to a list.
movie_chosen = list(movies_set)[3]
# Fetch the chosen movie's age.
movie_age = movies[movie_chosen]

# print(f"The movie screened now is {movie_chosen}.")
# my_age = int(input("Please enter your age: "))
# print(f"You are {my_age} years old.") # print the age.
#
# if my_age >= movie_age:
#     print("Thank you, please proceed to your purchase.")
# elif my_age < movie_age:
#     print("Sorry, you are too young to watch this movie.")
# else:
#     print("Oops, something went wrong.")


#### FOR LOOPS ####
shopping_list = ["bread", "eggs", "milk", "orange"]
# print(shopping_list[0])
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])

# Using a for loop to iterate through the list
# for items in shopping_list:
#     print(items)

# Iterate through each letter in a string
# for letter in "fruits":
#     print(letter)

# Exit a loop early
# for item in shopping_list:
#     print(item)
#     if item == "milk":
#         break # exits the loop

# Dictionary of food bills to iterate through
food_bill = {1: {"name": "Will", "bill": "£1"},
             2: {"name": "King", "bill": "£2"},
             3: {"name": "BigW", "bill": "£3"}}

# Print the names and the bill amount for each person
# for value in food_bill.values():
#     print(f"{value['name']} paid {value['bill']}")
#
# Separating the key and value.
# for key, value in food_bill.items():
#     print(f"{value['name']} paid {value['bill']}")

# Nested for loop
# for item in food_bill.values():
#     # Outputs the name and bill individually
#     for name_bill in item.values():
#         print(name_bill)


#### WHILE LOOPS ####
# Syntax while condition:
# Can run indefinitely if there isn't a way of stopping the condition.

# Counting from 0 to 9
# num = 0
# while num < 10: # while true, continue. If false, stop.
#     print(f"It's working -> {num}")
#     num += 1

# An if condition inside
# num = 0
# while num < 10:
#     print(f"It's working -> {num}")
#     if num == 4: # if true, the loop ends
#         break
#     num += 1

# Asking for user input
user_prompt = True
while user_prompt:
    age = input("Enter your age: ")
    if age.isdigit(): # checks if the input is in digits
        user_prompt = False
    else:
        print("Please enter your age in digits.")
print(f"Your age is {age}.") # Runs when the user enters their age in digits













