#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  rabin.py
#  
#  Rabin algorythm implementation by Bohdan Pakhomov
#  
#  

p=int(input("Enter p: "))
q=int(input("Enter q: "))
M=int(input("Enter M: "))

n=p*q

def pow_mod(x, y, z):
    # Calculate (x ** y) % z efficiently
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number
    
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

if n > M:
	print("OK! n > M")
	C=pow_mod(M,2,n)
	print("C = ", C)
	m1=pow_mod(C,int((p+1)/4),p)
	print("m1= ", m1)
	m2=m1*(-1)
	print("m2= ", m2)
	m3=pow_mod(C,int((q+1)/4),q)
	print("m3= ", m3)
	m4=m3*(-1)
	print("m4= ", m4)
	qInv=modinv(q, p)
	print("qInverse = ", qInv)
	pInv=modinv(p, q)
	print("pInverse = ", pInv)
	a=q*qInv
	print("a = ", a)
	b=p*pInv
	print("b = ", b)
	M1=(a*m1+b*m3)%n
	M2=(a*m1+b*m4)%n
	M3=(a*m2+b*m3)%n
	M4=(a*m2+b*m4)%n
	res=[M1,M2,M3,M4]
	print("M1 = ", M1)
	print("M2 = ", M2)
	print("M3 = ", M3)
	print("M4 = ", M4)
	for i in range(len(res)):
		if res[i] == M:
			print("Found decoded M: M"+str(i+1)+"=",res[i])
else:
	print("Error! M is greater or equal to n!!!")
