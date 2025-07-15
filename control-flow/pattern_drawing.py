# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate over each row
while row < size:
    # Use a for loop to print asterisks in each column
    for col in range(size):
        print("*", end="")
    # Print a newline after each row
    print()
    row += 1
