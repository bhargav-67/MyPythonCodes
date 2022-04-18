

import numpy as np


board=np.array([[5,3,0,0,7,0,0,0,0],
       [6,0,0,1,9,5,0,0,0],
       [0,9,8,0,0,0,0,6,0],
       [8,0,0,0,6,0,0,0,3],
       [4,0,0,8,0,3,0,0,1],
       [7,0,0,0,2,0,0,0,6],
       [0,6,0,0,0,0,2,8,0],
       [0,0,0,4,1,9,0,0,5],
       [0,0,0,0,8,0,0,7,9]])





    
def show_board(bo):
    m=9
    n=9
    for i in range(m):
        if i%3==0 :
            if i>0:
                print()
                print()
              
        for j in range(n):
            if j%3==0 :
                if j>0:
                     print(end="\t")
                
            
            print(bo[i,j],end="\t")
        print()
        print()
            




     
     
def find_next_empty(puzzle):
    m=len(puzzle)
    n=len(puzzle[0])
    for i in range(m):
        for j in range(n): 
            if puzzle[i][j] == 0: 
                return i,j
            
    return None, None



def guess_is_valid(puzzle,guess,row,col):
    row_vals = puzzle[row]
    if guess in row_vals:
        
   
        return False
    
    
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    
    row_start=(row//3)*3
    col_start=(col//3)*3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c]==guess:
                return False
    return True
        
   
    
    


def solve_sudoku(puzzle):
    
    
    row,col=find_next_empty(puzzle)
    
    if row==None:
      
        
        return True
        
    
    for guess in range(1,10):
        if guess_is_valid(puzzle,guess,row,col):
            puzzle[row][col]=guess  
            
            if solve_sudoku(puzzle):
                return True
            
        puzzle[row][col]=0
        
        
    return False


print()
print('______________________________________________________________________________________')
print("SUDOKU TO BE SOLVED")
print('______________________________________________________________________________________')
print()
show_board(board)

if solve_sudoku(board) == False:
    print("_____________________________________________________")
    print("******** YOU HAVE POSED AN INVALID QUESTION********")
    print("************* THE PUZZLE CAN  NEVER BE SOLVED************")
    print("_____________________________________________________")
    
else:
    print()
    print('______________________________________________________________________________________')
    print("SOLVED SUDOKU")
    print('______________________________________________________________________________________')
    print()
    Solved=np.array(solve_sudoku(board))
    
    
    
    
    print()
    show_board(board)
