import pwinput 



def game_rules(player1, player2):
    
    if (player1 == 'rock' and player2 == 'scissors'):
        print('player 1 wins.')
    elif (player1 == 'paper' and player2 == 'rock'):
        print('player 1 wins.')
    elif (player1 == 'scissors' and player2 == 'paper'):
        print('player 1 wins')

    elif(player1 == player2):
        print('you all loose')
    else:
        print('player2 wins') 
# def validate(val):

def main():
    player1 = input('player1? ')
    # validate(player1) 
    player2 = input('Player2? ') 
    
    game_rules(player1, player2) 
main()