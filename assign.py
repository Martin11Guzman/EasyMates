import time
from random import choice

def scheduleChores():
    print("Scheduling chores randomly...")
    time.sleep(1)
    # create a list of roomates from a file
    roomates = []
    file = open('roomates.txt', 'r')
    roomates = file.read().splitlines()
    print('roomates --->:', roomates)
    time.sleep(2)

    # create a list of chore names from a file
    chores = []
    file = open('chores.txt', 'r')
    chores = file.read().splitlines()
    print('Chore instructions:', chores)
    time.sleep(2)

    # create empty person lists
    person1 = []
    person2 = []
    person3 = []


    # loop until there are no roomates left
    while len(roomates) > 0:

        # choose a random person for chore
        roomate1 = choice(roomates)
        person1.append(roomate1)
        # remove the person from the roomates list
        roomates.remove(roomate1)

        # break out of the loop if there are no roomates left
        if roomates == []:
            break

        # choose a random person for chore
        roomate2 = choice(roomates)
        person2.append(roomate2)
        # remove the person from the roomates list
        roomates.remove(roomate2)

        # choose a random roomate for chore
        roomate3 = choice(roomates)
        person3.append(roomate3)
        # remove the person from the roomates list
        roomates.remove(roomate3)

    # choose random chore names for the 3 people
    choreName1 = choice(chores)
    chores.remove(choreName1)

    choreName2 = choice(chores)
    chores.remove(choreName2)

    choreName3 = choice(chores)
    chores.remove(choreName3)

    choreName4 = choice(chores)
    chores.remove(choreName4)

    choreName5 = choice(chores)
    chores.remove(choreName5)

    choreName6 = choice(chores)
    chores.remove(choreName6)

    # print the names with chores assaign
    print('\nHere are your assigned chores you slaves:\n')
    print(person1, "---> ", choreName1, choreName4)
    time.sleep(1)
    print(person2, "---> ", choreName2, choreName5)
    time.sleep(1)
    print(person3, "---> ", choreName3, choreName6)
