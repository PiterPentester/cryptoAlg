# Affine cipher (k=3) by Bohdan Pakhomov
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
with open('input_affine.txt', 'r') as f:
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

# encode char array by mult on A
M = []
for i in pText:
	M.append(list(i))

# encode char array by mult on A
a = np.array(A)
b = np.array(M)
pEncodeA = [] #np.matmul(a,b)
for i in range(len(M)):
	r = np.matmul(a, b[i])%26
	pEncodeA.append(list(r))

pEncode = []
for i in np.transpose(pEncodeA):
	pEncode.append(list(i))
print("After mult on A:")
for i in range(len(pEncode)):
	print(pEncode[i])

# add S to our char array
for i in range(len(pEncode[0])):
	for j in range(len(pEncode)):
		pEncode[j][i] = (pEncode[j][i] + S[j]) % 26
print("After adding S:")
for i in range(len(pEncode)):
	print(pEncode[i])

# Ord to char
def ordChar(text):
	res = []
	for i in range(len(text)):
		r = []
		for j in range(len(text[i])):
			r.append(chr(text[i][j] + ord('A')))
		res.append(r)
	return res
charsArr = ordChar(pEncode)
print("In char: ")
for i in range(len(charsArr)):
	print(charsArr[i])

# write res to file
res = ""
for i in np.transpose(charsArr):
	for s in i:
		res += s
with open('output_affine.txt', 'w') as f:
    f.write(res)
print("RES:", res)
