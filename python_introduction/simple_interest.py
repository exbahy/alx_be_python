#!/usr/bin/python3

# Define the variables with the given values
principal = 1000  # Initial investment amount ($1000)
rate = 0.05       # Annual interest rate (5%)
time = 3          # Time in years

# Calculate the simple interest using the formula I = P * R * T
interest = principal * rate * time

# Print the final calculated interest
# The f-string will automatically handle converting the number to a string
print(f"The simple interest is: {interest}")