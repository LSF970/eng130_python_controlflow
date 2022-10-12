# Pseudo code

# if it's cold:
#   take jacket
# if it's sunny: boolean value true - next line
#    go to the beach
# else or elif

# Real code

weather = "sunny"

if weather == "cold": # true or false
    print("Get a jacket")
elif weather == "sunny": # if false or condition met, do this
    print("Go to the beach")
else:
    print("No match found, better luck next time") # Don't leave the user hanging with no outcome.

# Age restriction for movie tickets
user_age = int(input("Please enter your age:"))

if user_age > 117: # Filter values you do not want first
    print("This age is invalid, please enter a younger age")
elif user_age >= 18:
    print("You can watch all movies")
elif user_age >= 15:
    print("You can watch movies up to 15 rated")
elif user_age >= 12:
    print("You can watch movies up to 12 rated")
elif user_age < 12:
    print("You can watch movies up to PG rated")
elif user_age > 0:
    print("You can watch movies up to U rated")
else:
    print("Input invalid, Please try again") # else statement if input is not what is expected

# film rating

# film_rating = input("Please enter the rating of the film")
#
# if film_rating.lower() == "universal":
#     print("all age groups can watch this film")
# elif film_rating.lower() == "pg":
#     print("General viewing, but some scenes may be unsuitable for young children.")
# elif film_rating.lower() == "12" or film_rating == "12a":
#     print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
# elif film_rating.lower() == "15":
#     print("No one younger than 15 may see a 15 film in a cinema.")
# elif film_rating.lower() == "18":
#     print("No one younger than 18 may see an 18 film in a cinema.")
# else:
#     print("this is not a correct rating, please use universal, pg, 12, 12a, 15, 18")


