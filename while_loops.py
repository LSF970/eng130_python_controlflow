# While loops

data = 0

while data < 10:
    print(f"It's working -> {data}")
    if data == 5:
        break
    data += 1

# Age verification program
user_prompt = True

while user_prompt:
    age = input("Please enter your age")
    if age.isdigit():
        user_prompt = False # We have what we want so the while loop ends
    else:
        print("Please enter your age in digits only") # We do not have what we want so message is displayed and while loop starts again
print("Your age is" + " " + age)