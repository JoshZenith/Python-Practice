name = input("What is your name?")
old = input("How old are you?")
print("Hello " + name + ", you are " + old + " years old.")

print("\n")

print("Hello " + name + ", you will be " + str(int(old) + 5) + " years old in 5 years.\n")
print("Hello " + name + ", you were " + str(int(old) - 5) + " years old \"5\" years ago.\n")

if int(old) < 18:
    print("You are a minor.")
else:
    print("You are an adult.")