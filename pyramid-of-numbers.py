# Function pyramid of numbers
def print_number_pyramid(x):
    for i in range(1, x + 1):  # For loop for length of pyramid
        # Print leading spaces for alignment
        for j in range(x - i): # For loop for spaces before and after each row
            print(" ", end="")

        # Print numbers from 1 to i
        for k in range(1, i + 1): # Foe loop for printing consecutive numeric values
            print(k, end=" ")

        print() 

# Main program function
def main():
    x = int(input("Enter a number: "))
    # Iterate the function
    print_number_pyramid(x)

# Run main program
if __name__ == "__main__":

    main()

