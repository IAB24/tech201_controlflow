# While Loops

# While loop monitors data rather than iterate

x = 0

# while x < 10:
#     print(f"It's working -> {x}")
#     x += 3 # incrementer

# Using break

# while x < 10:
#     print(f"It's working -> {x}")
#     if x == 4:
#         break
#     x += 1

# Verify user input

# Asking for someone's age
# This can either be an int (20) or a string (twenty)
# age = input("What is your age?")
#
# print(f"your age is {age}")

user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please provide your answer in digits and below 117")

print(f"Your age is {age}")
