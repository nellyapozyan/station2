import random as rd


def dice():
    return rd.randint(1, 6), rd.randint(1, 6)


def game():
    spin = sum(dice())
    print(f"Your spin is {spin}")

    if spin == 7 or spin == 11:
        print("You won!")

    elif spin == 2 or spin == 3 or spin == 12:
        print("Casino won!")

    else:
        print(f"Now your goal number is {spin}")
        while True:
            spin1 = sum(dice())
            print(f"The sum of dice is {spin1}")
            if spin1 == 7:
                print("You lose")
                break
            elif spin1 == spin:
                print("You won")
                break


game()
