# VIGENERE CIPHER on python3 by B. Pakhomov
import string

alphabet = string.ascii_uppercase
period1 = "FIRST"
period2 = "SECOND"
period3 = "SECURED"
period4 = "VIGENERE"
period5 = "FORTIFICA"

print("Encoding and decoding your text by five different periods!")

plainTxt = input("Input message to encode: ").upper()
plainTxt = plainTxt.replace(" ", "")

def encodeByPeriod(msg, period):
    encryptedMsg = ""
    if len(msg) < len(period):
        period = period[:len(msg)]
    elif len(msg) > len(period):
        while len(msg) != len(period):
            period += period[:len(msg)-len(period)]
    print(period)

    char_indexes = []
    for c in msg:
        if c in alphabet:
            char_indexes.append(alphabet.index(c))
    #print("indexes after msg:", char_indexes)
    i=0
    for cP in period:
        if cP in alphabet:
            char_indexes[i] += alphabet.index(cP)
            i += 1
    #print("indexes after period:", char_indexes)

    for idx in char_indexes:
        #print("idx%26 = ", str(idx%26))
        encryptedMsg += alphabet[idx%26]
    return encryptedMsg

def decodeByPeriod(msg, period):
    decryptedMsg = ""
    if len(msg) < len(period):
        period = period[:len(msg)]
    elif len(msg) > len(period):
        while len(msg) != len(period):
            period += period[:len(msg)-len(period)]
    print(period)

    char_indexes = []
    for c in msg:
        if c in alphabet:
            char_indexes.append(alphabet.index(c))

    i=0
    for cP in period:
        if cP in alphabet:
            char_indexes[i] -= alphabet.index(cP)
            i += 1
    #print("indexes after period:", char_indexes)

    for idx in char_indexes:
        #print("idx%26 = ", str(idx%26))
        decryptedMsg += alphabet[idx%26]
    return decryptedMsg



def start(msg):
    #ENCODE

    print("Encode", plainTxt, "by first period, r1 =", period1)
    encryptedMsg = encodeByPeriod(msg, period1)
    print("Encrypted text =", encryptedMsg)

    print("Encode", plainTxt, "by r2 =", period2)
    encryptedMsg = encodeByPeriod(encryptedMsg, period2)
    print("Encrypted text =", encryptedMsg)

    print("Encode", plainTxt, "by r3 =", period3)
    encryptedMsg = encodeByPeriod(encryptedMsg, period3)
    print("Encrypted text =", encryptedMsg)

    print("Encode", plainTxt, "by r4 =", period4)
    encryptedMsg = encodeByPeriod(encryptedMsg, period4)
    print("Encrypted text =", encryptedMsg)

    print("Encode", plainTxt, "by r5 =", period5)
    encryptedMsg = encodeByPeriod(encryptedMsg, period5)
    print("Encrypted text =", encryptedMsg)
    print()


    # DECODE

    print("Decode", encryptedMsg, "by r5=", period5)
    decryptedMsg = decodeByPeriod(encryptedMsg, period5)
    print("Decoded text =", decryptedMsg)

    print("Decode", decryptedMsg, "by r4=", period4)
    decryptedMsg = decodeByPeriod(decryptedMsg, period4)
    print("Decoded text =", decryptedMsg)

    print("Decode", decryptedMsg, "by r3=", period3)
    decryptedMsg = decodeByPeriod(decryptedMsg, period3)
    print("Decoded text =", decryptedMsg)

    print("Decode", decryptedMsg, "by r2=", period2)
    decryptedMsg = decodeByPeriod(decryptedMsg, period2)
    print("Decoded text =", decryptedMsg)

    print("Decode", decryptedMsg, "by r1=", period1)
    decryptedMsg = decodeByPeriod(decryptedMsg, period1)
    print("Decoded text =", decryptedMsg)

start(plainTxt)
