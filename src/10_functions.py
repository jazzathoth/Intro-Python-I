# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even(n):
    if n % 2 == 0:
        print('Even!')
    elif n % 2 != 0:
        print('Odd!')
    else:
        print('This is very strange...')
    return

is_even(num)
