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
# Sets cannot be accessed, so it is converted to a list.
movie_chosen = list(movies_set)[3]
# Fetch the chosen movie's age.
movie_age = movies[movie_chosen]

print(f"The movie screened now is {movie_chosen}.")
my_age = int(input("Please enter your age: "))
print(f"You are {my_age} years old.") # print the age.

if my_age >= movie_age:
    print("Thank you, please proceed to your purchase.")
elif my_age < movie_age:
    print("Sorry, you are too young to watch this movie.")
else:
    print("Oops, something went wrong.")


#### WHILE LOOPS ####


#### FOR LOOPS ####

