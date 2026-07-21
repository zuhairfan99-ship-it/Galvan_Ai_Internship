# Choose Your Own Adventure Game
name = input("Type your name: ")
print("Hello", name, "Welcome to my game!")
should_play = input("Do you want to play? (yes/no) ").lower()
if should_play == "yes":
    print("We are playing!")
    direction = input("Do you want to go left or right? (left/right) ").lower()
    if direction == "left":
        choice = input(
            "You come to a river, you can walk around it or swim across. (walk/swim) "
        ).lower()
        if choice == "swim":
            print("You swam across and were eaten by an alligator. You lose.")
        elif choice == "walk":
            print("You walked for many miles, ran out of water, and lost the game.")
        else:
            print("Not a valid option. You lose.")
    elif direction == "right":
        choice = input(
            "You come to a bridge, it looks wobbly. Do you want to cross or head back? (cross/back) "
        ).lower()
        if choice == "back":
            print("You go back to the main road and get hit by a car. You lose.")
        elif choice == "cross":
            choice = input(
                "You cross the bridge and meet a stranger. Do you talk to them? (yes/no) "
            ).lower()
            if choice == "yes":
                print("You talk to the stranger and they give you gold. YOU WIN!")
            elif choice == "no":
                print("You ignore the stranger and they get offended and attack you. You lose.")
            else:
                print("Not a valid option. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("We are not playing...")