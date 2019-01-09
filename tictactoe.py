
def display_board(board):
    print(f"\n  Available        Tic Tac Toe Board \n{avail[6]}  |  {avail[7]}  |  {avail[8]}        {board[6]}  |  {board[7]}  |  {board[8]}\n{avail[3]}  |  {avail[4]}  |  {avail[5]}        {board[3]}  |  {board[4]}  |  {board[5]}\n{avail[0]}  |  {avail[1]}  |  {avail[2]}        {board[0]}  |  {board[1]}  |  {board[2]}\n\n")
def player_input(player):
    playermark=None
    while playermark!="X" and playermark!="O":
        playermark=input(f"Player {player} is X or O ?  : ").upper()
    print(f"Player {player} choose {playermark}")
    return playermark
def place_marker(board, marker, position):
    board[position-1]=marker
def win_check(board, mark):
    if board[6]==mark:
        # cond1 vertical
        if board[3]==mark and board[0]==mark:
            return True
        # cond2 horizontal
        if board[7]==mark and board[8]==mark:
            return True
        # cond 3 diagonal
        if board[4]==mark and board[2]==mark:
            return True
    if board[7]==mark:
        # only cond is vertical
        if board[4]==mark and board[1]==mark:
            return True
    if board[8]==mark:
        # cond 1 vertical
        if board[5]==mark and board[2]==mark:
            return True
        # cond 2 diagonal
        if board[0]==mark and board[4]==mark:
            return True
    if board[3]==mark:
        # only cond is horizontal
        if board[4]==mark and board[5]==mark:
            return True
    if board[0]== mark:
        # only cond is horizontal
        if board[1]==mark and board[2]==mark:
            return True
    return False

import random
def choose_first():
    return random.randint(1,2)
def space_check(board, position):
    if board[position-1] != " ":
        return False
    else:
        return True
def full_board_check(board):
    for i in board:
        if i==" ":
            return False
    return True     
def player_choice(board,turn):
    global avail
    print(f"Player {turn['player']}'s turn")
    select=True
    while select:
        pos=int(input("Choose your Postion: "))
        if space_check(board, pos):
            select=False
            place_marker(board,turn['mark'],pos)
            avail[pos-1]=" "
            display_board(board)
        else:
            print("This position is already taken")
def replay():
    ans=None
    while ans!="yes" and ans!="no":
        ans=input("Do you want to play again? : ").lower()
    if ans=="yes":
        return True
    else:
        return False


#######    Main     #######
print('Welcome to Tic Tac Toe!')    
while True:
    # Game initiation 
    board=[" "," "," "," "," "," "," "," "," "]
    avail=[1,2,3,4,5,6,7,8,9]
    first={'player':"",'mark':''}
    second={'player':"",'mark':''}
    turn=first
    win=False
    display_board(board)
    
    # Random first player and selecting mark
    first['player']=choose_first()
    print(f"Player {first['player']} will go first ")
    if first['player']==1:
        second['player']=2
    else:
        second['player']=1
    first['mark']=player_input(first['player'])
    if first['mark']=="X":
        second['mark']="O"
    else:
        second['mark']="X"
    print(f"Then player {second['player']}\'s mark is {second['mark']}")
    
    # Game start
    while not win and not full_board_check(board):
        player_choice(board,turn)
        win=win_check(board,turn['mark'])
        if win:
            winner=turn['player']
        else:
            if turn==first:
                turn=second
            else:
                turn=first
    if not win:
        print("Draw")
    else:
        print(f"The winner is Player {winner}")
    if replay():
        print("\n\n\n\n\n")
        continue
    else:
        print("Goodbye")
        break

