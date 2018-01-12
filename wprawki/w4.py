from random import randint

board = ['_']*9

def winning(b, c='x'):
  for i in range(3):
    if(b[i]==c and b[i+3]==c and b[i+6]=='_'):
      return i+6
    if(b[i+6]==c and b[i+3]==c and b[i]=='_'):
      return i
    if(b[3*i]==c and b[3*i+1]==c and b[3*i+2]=='_'):
      return 3*i+2
    if(b[3*i+2]==c and b[3*i+1]==c and b[3*i]=='_'):
      return 3*i
  for i in range(4):
    if(b[4]==c and b[2*i]==c and b[8-2*i]=='_'):
      return 8-2*i
  return False

def display(b):
  print(b[0:3])
  print(b[3:6])
  print(b[6:9])    

def fork(b):
  bc = b
  if bc[4]=='x':
    return
  return


board[randint(0,4)*2] = 'x'
while(True):
  display(board)
  pl=int(input())
  board[pl]='o'
  #print(reccheck(board))
  if winning(board):
    board[winning(board)] = 'x'
    print("YOU HAVE LOST")
    continue
  if winning(board, 'o'):
    board[winning(board, 'o')] = 'x'
    continue
  if board[4]=='_':
    board[4] = 'x'
    continue
  for i in range(9):
    if board[i]=='_':
      board[i]='x'
      break
  print(winning(board))



