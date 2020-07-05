# will improve this later

win = False
Tie = False
counter = 0
it_=''
board=["-","-","-",
        "-","-","-",
        "-","-","-",]

def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

def inp(input_ ):
    global counter
    global it_
    flip_Turn()
    turn_var=it_
    input_ = input('Enter 1-9:')
    input_ = int(input_) - 1
    if(board[input_]=='-'):
        board[input_]=turn_var
        counter+=1
    else:
        print("invalid input")

    
def check_win_row():
    global win
    if (board[0]=='X' and board[1]=='X' and  board[2]=='X' or board[3]=='X' and board[4]=='X' and  board[5]=='X' or board[6]=='X' and board[7]=='X' and  board[8]=='X'):
        print("X wins")
        win =True
    elif(board[0]=='O' and board[1]=='O' and  board[2]=='O' or board[3]=='O' and board[4]=='O' and  board[5]=='O' or board[6]=='O' and board[7]=='O' and  board[8]=='O'):
        print("O wins")
        win =True
    else:
        return

def check_Win_Col():
    global win
    if (board[0]=='X' and board[3]=='X' and  board[6]=='X' or board[1]=='X' and board[4]=='X' and  board[7]=='X' or board[2]=='X' and board[5]=='X' and  board[8]=='X'):
        print("X wins")
        win =True
    elif(board[0]=='O' and board[3]=='O' and  board[6]=='O' or board[1]=='O' and board[4]=='O' and  board[7]=='O' or board[2]=='O' and board[5]=='O' and  board[8]=='O'):
        print("O wins")
        win =True
    else:
        return

def check_Win_Diag():
    global win
    if( board[0]=='X' and board[4]=='X' and board[8]=='X' or board[2]=='X' and board[4]=='X' and board[6]=='X'):
        print("X wins")
        win =True
    elif( board[0]=='O' and board[4]=='O' and board[8]=='O' or board[2]=='O' and board[4]=='O' and board[6]=='O'):
        print("O wins")
        win =True
    else:
        return

        
def check_win():
    check_win_row()
    check_Win_Col()
    check_Win_Diag()
    if(win):
        print("Game Over")
    else:
        return

def check_Tie():
    global Tie
    if(counter==9):
        print("Tie")
        Tie = True
    else:
        return


def flip_Turn():
    global counter
    global it_
    if(counter%2==0):
        it_='X'
    else:
        it_='O'

while(win == False and Tie == False):
    display_board()
    
    inp(it_)
    check_win()
    if(win == True or Tie == True):
        display_board()
        break
    

