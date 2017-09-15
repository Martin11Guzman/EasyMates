import time
import random



def rent():
    print("Aye let me do the math and yall do the paying how bow dat..")
    time.sleep(1)
    rent = input("What is the rent amount?: ")
    if rent.isnumeric():
        part = float(rent) / 3
        keegan_part = part - 100
        martin_part = keegan_part
        adam_part = part + 200
        print("adam:", adam_part)
        time.sleep(1)
        print("keegan:", keegan_part)
        time.sleep(1)
        print("martin:", martin_part)
        difference = (adam_part - keegan_part) - 100
        time.sleep(1)
        print("HAHAHA ADAM PAYS $" + str(round(difference)) + " dollars moree (:!")
        moneyOrder = input("Would you like me to randomly assign someone to go fetch a money order?"
                           "\ntype-- Yes or No: ")
        if moneyOrder == "yes":
            getMoneyOrder()
        else:
            print("Okey Dokey, son of a monkey, cousin of a donkey")
    else:
        time.sleep(1)
        print("invalid input...jackass")

def bill():
    print("Aye let me do the math and yall do the paying how bow dat..")
    time.sleep(1)
    amount = input("How much is total bill?: ")
    if amount.isnumeric():
        part = float(amount) / 3
        keegan = part
        print("Keegan: ", keegan)
        time.sleep(1)
        martin = part
        print("Martin: ", martin)
        time.sleep(1)
        adam = part
        print("Adam: ", adam)
    else:
        time.sleep(1)
        print("Invalid input... jackass")

def getMoneyOrder():
    people = ["Adam","Martin","Keegan"]
    print("Here is the list of people who will be randomly chosen to get a money order -->>", people)
    secure_random = random.SystemRandom()
    time.sleep(1)
    x = secure_random.choice(people)
    if x == "Adam":
        print("\nIf he doesn't come back with a money order, he will either have a wreckless driving ticket, "
                 "or sores on his feet from walking back home without a car.\n", x)
    elif x == "Keegan":
        print("\nYall sure an elephant is capable of driving??\n", x)

    else:
        print(x)


