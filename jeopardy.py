
score = 0

while True:
    try:
        section= str(input("Pick a Section: Math, Science or History "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
if section == "Math":
    mathVal= int(input("Pick a Question Amount: 100, 200, 300, 400, 500 "))
    if mathVal == 100:
        mathOne= int(input("What is 9+10 "))
        if mathOne == 19:
            print("Gaming Win")
            print(int(score + 100)," Points")
        else:
            print("Wrong.")
            print(int(score - 100))
    if mathVal == 200:
        mathTwo= int(input("What is 50x3 "))
        if mathTwo == 150:
            print("Gaming Win")
            print(int(score + 200)," Points")
        else:
            print("Wrong.")
            print(int(score - 200))
    if mathVal == 300:
        mathThree= int(input("What is 9+10 "))
    if mathVal == 400:
        mathFour= int(input("What is 9+10 "))
    if mathVal == 500:
        mathFive= int(input("What is 9+10 "))

