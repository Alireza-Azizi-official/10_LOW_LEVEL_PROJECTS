import random
#run the game and show the hints
#make a 4*4 matrix as a table
def start():
    matrix = []
    for i in range(0, 4):
        matrix.append([0] * 4)
    
    print('You can use these keys to play this game:')
    print('"W" or "w" : move up')
    print('"S" or "s" : move down')
    print('"D" or "d" : move right')
    print('"A" or "a" : move left')
    add_random_4(matrix)
    return matrix
#add a random number 2 to a random place in the matrix 
def add_random_4(matrix):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if matrix[i][j] == 0]
    if empty_cells:
        a, b = random.choice(empty_cells)
        matrix[a][b] = random.choice([2, 4])

#if the player reaches 2048 then the message you won will be returend
def position(matrix):
    for row in matrix:
        if 2048 in row:
            return 'YOU WON.'
#after each try check if there is an empty place if true then send the game is not over yet
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == matrix[i + 1][j] or matrix[i][j] == matrix[i][j + 1]:
                return 'GAME IS NOT OVER YET.'
    
    for i in range(3):
        if matrix[i][3] == matrix[i + 1][3]:
            return 'GAME IS NOT OVER YET.'
    
    for j in range(3):
        if matrix[3][j] == matrix[3][j + 1]:
            return 'GAME IS NOT OVER YET.'
#if there is no room then return game over to the player   
    return 'GAME OVER.'

#show the changes
def compress(matrix):
    changed = False
    new_matrix = []
    
    for i in range(4):
        new_matrix.append([0] * 4)
    
    for i in range(4):
        pos = 0
        
        for j in range(4):
            if (matrix[i][j] != 0):
                new_matrix[i][pos] = matrix[i][j]
                
                if (j != pos):
                    changed = True
                pos += 1
    return new_matrix, changed

#show the changes after merging two items
def merge(matrix):
    changed = False
    
    for i in range(4):
        for j in range(3):
            if (matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0):
                matrix[i][j] *= 2
                matrix[i][j + 1] = 0
                changed = True
    return matrix, changed

def reverse(matrix):
    nmatrix = []
    for i in range(4):
        nmatrix.append([])
        for j in range(4):
            nmatrix[i].append(matrix[i][3 - j])
    return nmatrix

def transpose(mat):
    nmatrix=[]
    
    for i in range(4):
        nmatrix.append([])
        
        for j in range(4):
            nmatrix[i].append(mat[j][i])
            
    return nmatrix
#create the move and changes of 4 directions
def to_left(grid):
    ngrid, changed1 = compress(grid)
    ngrid, changed2 = merge(ngrid)
    
    changed = changed1 or changed2
    
    ngrid, _ = compress(ngrid) # Discard the second value as it is not needed here
    
    return ngrid, changed

def to_right(grid):
    ngrid = reverse(grid)
    
    ngrid, changed = to_left(ngrid)
    
    ngrid = reverse(ngrid)
    
    return ngrid, changed

def to_up(grid):
     ngrid = transpose(grid)

     ngrid, changed = to_left(ngrid)

     ngrid=transpose(ngrid)

     return ngrid,changed

def to_down(grid):
     ngrid=transpose(grid)

     ngrid,changed=to_right(ngrid)

     ngrid=transpose(ngrid)

     return ngrid,changed
