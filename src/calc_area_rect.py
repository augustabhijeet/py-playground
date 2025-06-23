#Write a program that calculates the area of a rectangle (ask for length and width).
def get_dimension(prompt_text):
    """
    Prompts the user to enter a dimension (length or width) and validates the input.
    Ensures the input is a positive number.
    """
    while True:
        try:
            # Get input from the user, convert to float, and remove leading/trailing whitespace
            value = float(input(prompt_text).strip())
            if(value < 0):
                print("Dimension must be a positive number. Please try again.")
            else:
                return value
            
        except ValueError:
            # Handle cases where the input is not a valid number
            print("Invalid input. Enter a valid numerical value")

def calc_area_of_rect(length, width):
    return length * width

if __name__ == "__main__":
    print("Welcome to the rectangle area calculator")

    #Get the length from the user
    length = get_dimension("Please enter the length: ")
    width = get_dimension("Please enter the width: ")

    area = calc_area_of_rect(length, width)

    #Print the result
    print(f"\nThe area of the rectangle is: {area}")
