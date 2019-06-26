import random

name = input("What is your name? ")
salary = input("How much money do you make? ")
raise_per = random.randint(0, 100)
raise_amount = (int(salary) / raise_per) + int(salary)
print(f"{name} you currently make ${salary}")
print(f"{name} your new salary is ${raise_amount} with {raise_per}% interest" )