#!/usr/bin/python3

# 1. Prompt the user for their current age and get the input
# The input() function returns the user's entry as a string.
user_input_age_str = input("How old are you? ")

# 2. Convert the string input to an integer for calculation
# The int() function converts a string of digits into a number.
current_age = int(user_input_age_str)

# 3. Calculate the future age
# The difference between 2050 and 2023 is 27 years.
years_to_add = 27
future_age = current_age + years_to_add

# 4. Print the final result in the specified format
print(f"In 2050, you will be {future_age} years old.")