def ConstBoard(board):
  #function to print the current board
  print("Current State of the Board: \n")
  for i in range(0, 9):
    if((i>0) and (i%3==0)):
      print("\n")
    if(board[i]==0):
      print(" - ", end=" ")
    elif(board[i]==1):
      print(" X ", end=" ")
    else:
      print(" O ", end=" ")
  print("\n\n")


def minmax(board, player):
  x =  analyseboard(board)
  if(x!=0):
    return (x*player)
  value = -2
  pos = -1
  for i in range(0,9):
    #Check if board is empty
    if(board[i]==0):
      board[i]=player
      score= -minmax(board, player*-1)
      board[i]=0
      if(score>value):
        value=score
        pos=i
  if(pos==-1):
    return 0
  return value


def CompTurn(board):
  value = -2
  pos = -1
  for i in range(0,9):
    #Check if board is empty
    if(board[i]==0):
      board[i]=1
      score= -minmax(board, -1)
      board[i]=0
      if(score>value):
        value=score
        pos=i
  board[pos]=1


#Player playing first (X)
def user1Turn(board):
  pos = int(input("Enter the position for X: "))
  if((pos<1) or (pos>9)):
    print("Wrong move. Invalid position")
    user1Turn(board)
  elif(board[pos-1]!=0):
    print("Wrong move. Position already taken")
    user1Turn(board)
  else:
    board[pos-1]=1



#player playing second (O)
def user2Turn(board):
  pos = int(input("Enter the position for O: "))
  if((pos<1) or (pos>9)):
    print("Wrong move. Invalid position")
    user2Turn(board)
  elif(board[pos-1]!=0):
    print("Wrong move. Position already taken")
    user2Turn(board)
  else:
    board[pos-1]=-1


def analyseboard(board):
  #Champion Board
  cb = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

  for i in range(0,8):
    #Checking if someone won
    if((board[cb[i][0]]!=0) and
       (board[cb[i][0]]==board[cb[i][1]]) and
       (board[cb[i][1]]==board[cb[i][2]])):
      return board[cb[i][0]]
  return 0


def main():
  choice = int(input("Enter 1 for Single player and 2 for Multiplayer: "))
  # board ( 0->Empty, 1->X, -1->O)
  board = [0,0,0,0,0,0,0,0,0]

  if(choice==1):
    #code to play against AI
    print("Computer:X and You:O ")
    player = int(input("Enter to play: 1(1st) or 2(2nd): "))
    for i in range(0,9):
      if(analyseboard(board)!=0):
        break
      if((i+player)%2==0):
        CompTurn(board)
      else:
        ConstBoard(board)
        user2Turn(board)

  elif(choice==2):
    #code for multiplayer
    for i in range(0,9):
      if (analyseboard(board)!=0):
        break
      if(i%2==0):
        ConstBoard(board)
        user1Turn(board)
      else:
        ConstBoard(board)
        user2Turn(board)

  else:
    print("Wrong choice")
    main()

  x = analyseboard(board)

  if(x==0):
    ConstBoard(board)
    print("Match is a Draw")
  if(x==1):
    ConstBoard(board)
    print("Player One has won")
  if(x==-1):
    ConstBoard(board)
    print("Player Two has won")

  c = int(input("If you want to play again press 1 else any other number: "))
  if(c==1):
    main()
  else:
    print("Thankyou for playing")
