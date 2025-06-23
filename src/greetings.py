# This program asks the user for their name and then prints a personalized greeting.
def get_user_name():
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Please try again.")

def greet_user(name):
    print(f"Hello, {name}! Welcome here!")

# Main function to run the greeting program
def main():
    user_name = get_user_name()
    greet_user(user_name)

if __name__ == "__main__":
    main()
# This ensures that the main function runs only when this script is executed directly.
# If this script is imported as a module, the main function will not run.
# This is a common practice in Python to allow code reusability and modularity.