# Name Formatter and Length Calculator
# 1. Input your first name and last name
first_name = input("Enter your firstname: ")
last_name = input("Enter your lastname: ")

# 2. Convert first name to uppercase and last name to lowercase
first_name = first_name.upper()
last_name = last_name.lower()

# 3. Calculate and print the sum of the letters
length = len(first_name) + len(last_name)

# 4. Print the first name in uppercase, last name in lowercase, and the total letters

print(f"First name(Upper): {first_name}")
print(f"Last name(lower): {last_name}")
print(f"Sum of letters in your first and last name: {length}")
