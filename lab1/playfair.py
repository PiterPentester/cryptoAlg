# PLAYFAIR CIPHER on python3 by AtriSaxena, modified and documented by B. Pakhomov

key=input("Enter key: ")
key=key.replace(" ", "")
key=key.upper()

# Matrix init
"""
[[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]]
"""
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]

result=list()
for c in key: #storing key
    if c not in result:
        if c=='J': # replace "J" by "I"
            result.append('I')
        else:
            result.append(c)

flag=0
# alphabetical chars started at 65
for i in range(65,91): #storing other character
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass
        else:
            result.append(chr(i))

k=0
my_matrix=matrix(5,5,0) #initialize matrix
for i in range(0,5): #making matrix
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1

def locindex(c): #get location of each character in 2d my_matrix => like (0,0) or (0,4)
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc

def encrypt():  #Encryption
    msg=str(input("ENTER MSG: "))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:] # If string = "AA" - we instert "X" between "A" => "AXA"

    # for digram we need len(msg)%2 == 0 else we add "X" to msg
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT: ", end='')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]: #if digram are on same column
            """
            digram = "RU"
            matrix =
            [[A B C D E]  "RU" are on the same column! we just replace our char to next char in this column => "RU" = "NH"
            [Q W T R Y]
            [Z X V N M]
            [P O I U G]
            [L K F H J]]
                   ^
            """
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]), end='')

        elif loc[0]==loc1[0]: # if digram are in same row
            """
            digram = "CA"
            matrix =
            [[A B C D E]  <= "CA" are on the same line! we just replace our char to next char in line => "CA" = "DB"
            [Q W T R Y]
            [Z X V N M]
            [P O I U G]
            [L K F H J]]
            """
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]), end='')

        else: # in other situations
            """
            digram = "QM"
            matrix =
            [[A B C D E ]
            [Q W T R Y] => "Q" = "Y"
            [Z X V N M] => "M" = "Z"
            [P O I U G]
            [L K F H J]]
            """
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]), end='')
        i=i+2

def decrypt():  #decryption
    msg=str(input("ENTER CIPHER TEXT: "))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT: ", end='')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]), end='')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]), end='')
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]), end='')
        i=i+2

while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT\n"))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice!!!\n")
