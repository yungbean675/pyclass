while True:
    try:
        name= str(input("What is your name? "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
if name == "Ethan":
    print("You have a big brain!")
else:
    print("Stupid idiot.")