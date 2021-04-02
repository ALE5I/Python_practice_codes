#Dice simulator
import random


def roll_die(num_faces):
    return random.randint(1,num_faces)


if __name__ == '__main__':
    
    while True:
        die_result = []
        num_faces = []
        num_dice = int(input("How many dice are you going to throw? --> "))

        for x in range (0, num_dice):
            num_faces.append(int(input('How many faces does this die has? --> ')))
            die_result.append(roll_die(num_faces[x]))
            
        while True:
            
            print(f'This are the results: {die_result}')

            die_result = []
            repeat = input('Again? --> ')
            if repeat != 'n':
                for x in range (0, num_dice):
                    die_result.append(roll_die(num_faces[x]))
            else:
                break     

        game_over = input("Do you want to keep playing? --> ")
        if game_over == "n":
            break
