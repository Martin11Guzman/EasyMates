from assign import *
from calculations import *


def main():
    print("Welcome to the ghetto roomate app!")
    print("This is where you can solve easy household problems(:")
    time.sleep(1)
    option = input("What problem could I solve my fellow hitz?..\n"
                   "Options:  \n"
                   "\tCalculate rent?-- type 'rent'\n\tCalculate a bill?--type 'bill'\n\tAssign Chores?--type 'chores'"
                   "\n\tRandomly choose someone to get a money order?--type 'money'\n")
    if option == "rent":
        rent()

    elif option == "bill":
        bill()
    elif option == "chores":
        scheduleChores()
    elif option == "money":
        getMoneyOrder()
    else:
        print("Aye type up an option mane wtf is wrong witcha wid yo broke ah..")
        time.sleep(1)
        main()

if __name__ == '__main__':
    main()
