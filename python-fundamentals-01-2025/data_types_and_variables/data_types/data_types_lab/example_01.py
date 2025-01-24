# Example string with comma-separated numbers
input_string = "1,2,3,4,5"

# Split the string into a list of strings using split()
string_list = input_string.split(',')

# Convert each element to an integer using a list comprehension
integer_list = [int(num) for num in string_list]

# Print the resulting list of integers
print("Input String:", input_string)
print("List of Integers:", integer_list)
