old = 0
name = input("What is your name? ")

while True:
    try:
        old = int(input("How old are you? "))  # Try to convert input to an integer
        break  # Exit the loop if input is valid
    except ValueError:
        print("Please enter a valid number.")  # Prompt the user again if input is invalid

print(f"\nHello, {name}. You are {old} years old.")