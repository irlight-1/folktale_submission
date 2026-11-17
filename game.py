room = 'starting'
keycard = 0
game_running = True
answer = 0

while game_running:
    if room == "starting":
        print("You wake up in a strange facility, you're unsure where you are. To the left, you see a door with a keycard reader. To the right, you see a room that's connected to this one.")
        print("To attempt to unlock the door, enter 1. To enter the connected room, enter 2")

        answer = input("Left or Right?: ")

        if answer == "1":
            room = "keycard_door"

        elif answer == "2":
            room = "connecting_room"

        else:
            print("Invalid answer, try again.")

    elif room == "keycard_door":
        if keycard >= "2":
            print("The door opened, you step out and see the world once more.")
            game_running = False
        else:
            print("You try to open the door and you fail. Not enough keycards, you have " + str(keycard) + " right now!")
            room = "starting"

    elif room == "connecting_room":
        print("You enter the connecting room, you see three things in front of you, a sleeping guard, a keycard dispenser (how convinent, you say!), a coin machine, and a math puzzle")
        print("Enter '1' to try to steal the keycard from the guard, enter '2' to take a keycard from the dispenser, enter '3' to try the puzzle, or enter '4' to go back to the main room.")

        answer = input("1-4: ")

        if answer == "1":
            room = "guard"
        elif answer == "2":
            room = "dispenser"
        elif answer == "3":
            room = "math"
        elif answer == "4":
            room = "starting"
        else:
            print("Invalid input entered")
    elif room == "math":
        print("You come close up to the math puzzle, the screen boots up and asks you a question:")
        print("What is the X-Intercept of y = 4x - 8?")
        print("Choose your answer below:")
        print("a: 3")
        print("b: 99")
        print("c: 2")
        print("d: 148")

        answer = input("a-d: ").lower()

        if answer == "a" or answer == "b" or answer == "d":
            print("Sorry, that is incorrect")
        elif answer == "c":
            print("That is correct! A keycard was dispensed, and you took it.")
            keycard += 1
            room = "connecting_room"
        else:
            print("Invalid input entered")
    elif room == "guard":
            print("You slowly approach the guard. They're still asleep. You try to grab the keycard.")
            print("Pick a number, 1-4")
    
            answer = input("1-4: ").lower()
    
            if answer == "1" or answer == "2" or answer == "4":
                print("Sorry, you didn't pass. You fail to get the keycard, it's too far.")
            elif answer == "3":
                print("You chose right! You successfully take the keycard, and you head back slowly.")
                keycard += 1
                room = "connecting_room"
            else:
                print("Invalid input entered")
    elif room == "dispenser":
                print("You step up to the machine, there's a paper taped on it saying 'Out of service, sorry!' You walk back in shame.")
                room = "connecting_room"