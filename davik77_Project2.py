
import random
def main():
    user = input('Enter your Name: ')
    print("Ok, here is the board:")
    Count = 0
    board1 = board()
    #print("Your move,",user)
    while checklist(board)!= True:
        create(board1)
        print("Your move,",user)
        board1 = move1(board1)
        Count += 1 #Extra
        if sum(board1) == 0:
                print('Hmm... What shall I say? I guess I won...')
                break
        board1,compPile,x = move2(board1)
        if sum(board1) == 0:
            print('You Lost!')
            break
        print('I pick {} stones from pile {}'.format(x,compPile))
        print("Ok, here is the board:")
        Count +=1 #Extra
        #print(board1)
    print('The Number of moves it took to win the game was {}'.format(Count)) #Extra
    #create(board1)
    round2 = input('Another game? Enter y for yes, anything for no:')
    if round2 in 'yY':
        main()
    else:
        print('Thanks for playing...David is the best player!')


def board():
    ch = random.randint(3,6)
    piles = []
    for i in range(ch): 
        piles.append(random.randint(1,10)) #["X"]*
    #for i in range(ch):
        #print("Pile",i+1,":",piles[i])
    #print("Your move,",user)
    return piles




def create(board):
    count = 0
    for i in board:
        count += 1
        var = ('X ' *i)
        print("Pile ",count,":    ",var,sep = '')



def checklist(board):
    var = board()
    for ch in var:
        if ch != 0:
            return False
    return True


def move1(board):
        pileCount = (input('What Pile?  '))
        stoneRe = (input('How many Stones?  '))
        
        while not pileCount.isdigit() or not stoneRe.isdigit(): #or int(pileCount) > len(board)or stoneRe > (board[pileCount-1]):
            print("Something is wrong. Make sure your pile and number of stones are valid")
            pileCount = (input('What Pile? '))
            stoneRe = (input('How many Stones? '))
        pileCount = int(pileCount)
        stoneRe = int(stoneRe)

        while  int(pileCount) > len(board)or stoneRe > board[pileCount-1]:
            print("Something is wrong. Make sure your pile and number of stones are valid")
            pileCount = int(input('What Pile? '))
            stoneRe = int(input('How many Stones? '))
        board[pileCount-1] -= stoneRe #Boardcount subtracting the amount that user entered

        return board
    

def move2(board):
    print('My turn:')
    compPile = random.randint(1,len(board))

    while board[compPile-1] == 0:
        compPile = random.randint(1,len(board))
    #print(board)
    x = random.randint(1,6)

    if board[compPile-1] < x:
        x = board[compPile-1]
        
    board[compPile-1] -= x
    return board, compPile, x
    

main()
