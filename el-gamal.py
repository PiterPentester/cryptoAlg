#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  el-gamal.py
#  
#  El-Gamal cipher implementation by Bohdan Pakhomov
#  
#  
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

### MAIN ###

p=int(input("Enter p: "))
q=int(input("Enter q: "))
ka=int(input("Enter ka: "))
kb=int(input("Enter kb: "))
M=int(input("Enter M: "))

Ya=pow_mod(M,ka,p)
Yb=pow_mod(M,kb,p)
print("Ya=", str(Ya) + ", Yb=", str(Yb))

Ya_kb=pow_mod(Ya,kb,p)

Mbin=bin(M)
Ya_kb_bin=bin(Ya_kb)
C=bin(M^Ya_kb)
print("Mbin="+Mbin[2:]+", Ya_kb_bin="+Ya_kb_bin[2:]+", C= "+Mbin[2:]+"^"+Ya_kb_bin[2:]+"="+C[2:])

Yb_ka=pow_mod(Yb,ka,p)
Yb_ka_bin=bin(Yb_ka)
Mdecoded=bin(int(C,2)^Yb_ka)
print("M decoded="+C[2:]+"^"+Yb_ka_bin[2:]+"="+Mdecoded[2:])
