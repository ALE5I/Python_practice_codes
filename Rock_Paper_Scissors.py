import random


def assign(int_chose):

    if int_chose == 1:
        return "Rock"
    if int_chose == 2:
        return "Paper"
    if int_chose == 3:
        return "Scissors"


def rules(player_chose, bot_chose):
    result = ''    

    if player_chose == bot_chose:
        result = "It's a draw"
    elif ((player_chose == 1 and bot_chose == 3) or (player_chose == 2 and bot_chose == 1) or (player_chose == 3 and bot_chose == 2)):
        result = 'You Win!'
    else:
        result = 'You Lose'

    return result


def score (result,scr):
    if (result == 'You Win!'):
        scr[0] += 1
    elif (result == 'You Lose'):
        scr[1] += 1
    else:
        scr[2] += 1

    return scr

if __name__=='__main__':
    
    scr = [0,0,0]
    
    while True:

        try:
            player_chose = int(input('\nSelect your move: \n1.Rock\n2.Paper\n3.Scissors\n\n'))
        except ValueError:
            player_chose = int(input('\nPlease type the number of your move: \n"1" for Rock\n"2" for Paper\n"3" for Scissors\n\n'))

        bot_chose = random.randint(1,3)
        
        result = rules(player_chose, bot_chose)
        scr = score(result,scr)

        player_chose, bot_chose = assign(player_chose), assign(bot_chose)
        print(f'\nBot has chosen    = {bot_chose} \nPlayer has chosen = {player_chose} \nResult = {result}')
        
        play = input('\nDo you want to play again (y/n)? -------> ')
        if play == "n":
            break

    print(f'\n       Won  = {scr[0]}\nScore: Lose = {scr[1]}\n       Draw = {scr[2]}\n')

    if (scr[0] > scr[1]):
        print("Congratulations, you won!\n")
    else:
        print("That's a shame, the bot has won :'(\n")

    input('''+-+-+-+-+ +-+-+-+-+ | +-+-+-+-+ +-+-+-+
|G|A|M|E| |O|V|E|R| | |G|O|O|D| |B|Y|E|
+-+-+-+-+ +-+-+-+-+ | +-+-+-+-+ +-+-+-+''')
