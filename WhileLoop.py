name=input("Enter your name: ")

while name=="":
    print("Name not entered")
    name = input("Please enter your name: ")
print(f"Hello {name}")

food=input("Enter your favourite food: ")

while not food=="exit":
    print(f"You like {food}")
    food = input("Enter your favourite food: ")
print("You exited the program")