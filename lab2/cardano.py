# CARDANO CIPHER (6x6) on python3 by B. Pakhomov

### For encoding
def putPattern(msg):
    i = 0
    for e in g_pattern:
        c_grid[e[0]][e[1]] = msg[i]
        i += 1

def fillGaps(msg):
    i = 0
    for e in g_other:
        c_grid[e[0]][e[1]] = msg[i]
        i += 1


### For decoding
def getFromPattern(res):
    for e in g_pattern:
        res += c_grid[e[0]][e[1]]
    return res

def getFromGaps(res):
    for e in g_other:
        res += c_grid[e[0]][e[1]]
    return res


# An Inplace function to rotate
# N x N matrix by 90 degrees in
# anti-clockwise direction
def rotateAntiClock(mat):
    N = len(mat[0])
    # Consider all squares one by one
    for x in range(0, int(N / 2)):

        # Consider elements in group
        # of 4 in current square
        for y in range(x, N-x-1):

            # store current cell in temp variable
            temp = mat[x][y]

            # move values from right to top
            mat[x][y] = mat[y][N-1-x]

            # move values from bottom to right
            mat[y][N-1-x] = mat[N-1-x][N-1-y]

            # move values from left to bottom
            mat[N-1-x][N-1-y] = mat[N-1-y][x]

            # assign temp to left
            mat[N-1-y][x] = temp

# Function to rotate the matrix
# 90 degree clockwise
def rotateClock(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp

### ENCODING ###
msg = "The Cardan grille is a method of writing secret messages using a grid"
print("Plain text:", msg)

#msg = msg.replace(" ", "")
msg = msg[:36].upper()
for_check = msg

print("Prepared for encoding text:", msg)

# init array
c_grid = [["=" for i in range(6)] for j in range(6)]
for e in c_grid:
    print(e)

# init res for storing our result string
res = ""

# init grid pattern
g_pattern = [[0,3], [1,4], [3,0], [3,2], [4,2], [4,5], [5,4], [5,5]]
# we have 4 empty cell after pattern rotating. Fill them
g_other = [[1,2], [2,4], [3,1], [4,3]]

for e in g_pattern:
    c_grid[e[0]][e[1]] = "X"

print("Our pattern: ")
for e in c_grid:
    print(e)


### FIRST
p_1 = msg[:8]
msg = msg[8:]
putPattern(p_1)
print("First step:")
for e in c_grid:
    print(e)

### SECOND
#print()
rotateAntiClock(c_grid)
#for e in c_grid:
#    print(e)
p_2 = msg[:8]
msg = msg[8:]
putPattern(p_2)
rotateClock(c_grid)

print("Second step:")
for e in c_grid:
    print(e)

### THIRD
# we need to rotate 2x because we always reset our rotatting for print step result
rotateAntiClock(c_grid)
rotateAntiClock(c_grid)
p_3 = msg[:8]
msg = msg[8:]
putPattern(p_3)

rotateClock(c_grid)
rotateClock(c_grid)
print("3rd step:")
for e in c_grid:
    print(e)

### FOUR
# we need to rotate 3x
rotateAntiClock(c_grid)
rotateAntiClock(c_grid)
rotateAntiClock(c_grid)
p_4 = msg[:8]
msg = msg[8:]
putPattern(p_4)

rotateClock(c_grid)
rotateClock(c_grid)
rotateClock(c_grid)
print("4th step:")
for e in c_grid:
    print(e)


### FIVE
p_5 = msg
fillGaps(p_5)
print("5th step:")
for e in c_grid:
    print(e)

for e in c_grid:
    for c in e:
        res += c
print("Encoded string:", res)
#print("DORTTNHFGTHIOLIESMEECRINEAACGRILSWDA" == res)

######## DECODING ##########
res = ""

### FIRST
res = getFromPattern(res)

### SECOND
#print()
rotateAntiClock(c_grid)

res = getFromPattern(res)

rotateClock(c_grid)

### THIRD
# we need to rotate 2x because we always reset our rotatting for print step result
rotateAntiClock(c_grid)
rotateAntiClock(c_grid)

res = getFromPattern(res)

rotateClock(c_grid)
rotateClock(c_grid)

### FOUR
# we need to rotate 3x
rotateAntiClock(c_grid)
rotateAntiClock(c_grid)
rotateAntiClock(c_grid)

res = getFromPattern(res)

rotateClock(c_grid)
rotateClock(c_grid)
rotateClock(c_grid)

### FIVE
res = getFromGaps(res)

print("Decoded text:", res)
print(res == for_check)
