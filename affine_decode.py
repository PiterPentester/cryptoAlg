############################################### decoding #########################################################
# Affine cipher (k=3) by Bohdan Pakhomov
# w^(-1)=49^(-1)=x (mod 26)=17
import numpy as np
# Key A
A = [[12, 4,  3],
     [5,  2,  1],
     [17, 13, 11]] # w=49, HCD(49,26)=1

# Key S
S = [7,
     9,
     3] # in Z(26)

# init array for our input
pText = []

# get input
#plainText = input("Input text to encoding: ").replace(' ', '').upper()
with open('output_affine.txt', 'r') as f:
     plainText = f.read().replace(' ', '').upper().replace('\n', '')

print(plainText)

# init array for our input
pText = []

# string to 2d array
def splitTxt(text):
	txt = list(text)
	print(len(txt))
	while len(txt) % 3 != 0:
		txt.append('A')
	rng = len(txt) / 3
	for i in range(int(rng)):
		r = []
		for j in range(3):
			r.append(txt[0])
			txt = txt[1:]
		pText.append(r)

splitTxt(plainText)
print(pText)

# Char to index of char
def charOrd(text):
	for i in range(len(text)):
		for j in range(len(text[i])):
			text[i][j] = (ord(text[i][j]) - ord('A')) % 26

charOrd(pText)
print("charOrd:")
for i in range(len(pText)):
	print(pText[i])

print()

# transpose our char array (rows -> cols)
trM = []
for i in np.transpose(pText):
	trM.append(list(i))
print("Our char array:")
for i in range(len(trM)):
	print(trM[i])


# Init Aq matrix
Aq = [[0 for x in range(3)] for j in range(3)]

# we need to inverse matrix
Ainv = np.linalg.inv(A)
print("A inverse: ", Ainv)
# Calculate Aq matrix
for x in range(3):
	for j in range(3):
		Aq[x][j]=(round(Ainv[x][j] * 49) * 17)%26

print("Aq:")
for i in Aq:
    print(i)


# Sq = -Aq*S
a = np.array(Aq)
b = np.array(S)
SqT = np.matmul(a,b)
Sq = []
for i in SqT:
    Sq.append((i%26)*(-1))

print("Sq: ", Sq)

# decoding: mult encoded array on Aq
a = np.array(Aq)
b = np.array(trM)
pDec = a.dot(b)
pDecodeU = []
for i in pDec:
    r = []
    for j in i:
        j = j%26
        r.append(j)
    pDecodeU.append(r)
print("Mult encoded array on Aq: ")
for i in pDecodeU:
	print(i)


pDecode = [[0 for i in range(len(pDecodeU[0]))] for j in range(len(pDecodeU))]
# add S to our char array
for i in range(len(pDecodeU[0])):
	for j in range(len(pDecodeU)):
		pDecode[j][i] = (pDecodeU[j][i] + Sq[j]) % 26
print("After adding S:")
for i in pDecode:
	print(i)

# Ord to char
def decodeChar(text):
	res = []
	for i in range(len(text)):
		r = []
		for j in range(len(text[i])):
			r.append(chr(text[i][j]+ord('A')))
		res.append(r)
	return res
charsDecArr = decodeChar(pDecode)
print("In char: ")
for i in range(len(charsDecArr)):
	print(charsDecArr[i])

# write res to file
res = ""
for i in np.transpose(charsDecArr):
	for s in i:
		res += s
print("RES:", res)
