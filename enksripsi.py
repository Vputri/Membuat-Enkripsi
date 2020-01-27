import time
def menu():
    print "                           TUGAS SISTEM OPERASI"
    print "                          MEMBUAT ENKRIPSI BARU"
    print "                    By : Vika Putri Ariyanti (56417094)"
    print "======================================================================="
    print "|                                   MENU                               |"
    print "|                                1. Encoder                            |"
    print "|                                2. Decoder                            |"
    print "======================================================================="
    
    x = input("   Masukkan Pilihan Anda(1/2)   : ")
    if x == 1:
        print "Welcome to the Encoder"
        print "+-----------------------------+"
        time.sleep(2)
        message = raw_input("Please enter your encrypt: ")
        encoded = ""
        for char in message:
            if char == "a" or char == "A":
                encoded += "1"
            elif char == "b" or char == "B":
                encoded += "2"
            elif char == "c" or char == "C":
                encoded += "3"
            elif char == "d" or char == "D":
                encoded += "4"
            elif char == "e" or char == "E":
                encoded += "5"
            elif char == "f" or char == "F":
                encoded += "6"
            elif char == "g" or char == "G":
                encoded += "7"
            elif char == "h" or char == "H":
                encoded += "8"
            elif char == "i" or char == "I":
                encoded += "9"
            elif char == "j" or char == "J":
                encoded += "0"
            elif char == "k" or char == "K":
                encoded += "@"
            elif char == "l" or char == "L":
                encoded += "#"
            elif char == "m" or char == "M":
                encoded += "$"
            elif char == "n" or char == "N":
                encoded += "="
            elif char == "o" or char == "O":
                encoded += ")("
            elif char == "p" or char == "P":
                encoded += "//"
            elif char == "q" or char == "Q":
                encoded += "~"
            elif char == "r" or char == "R":
                encoded += ";"
            elif char == "s" or char == "S":
                encoded += ":"
            elif char == "t" or char == "T":
                encoded += "{}"
            elif char == "u" or char == "U":
                encoded += "[]"
            elif char == "v" or char == "V":
                encoded += "|"
            elif char == "w" or char == "W":
                encoded += "."
            elif char == "x" or char == "X":
                encoded += "?"
            elif char == "y" or char == "Y":
                encoded += "!"
            elif char == "z" or char == "Z":
                encoded += "`"
            elif char == "1":
                encoded += "11"
            elif char == "2":
                encoded += "00"
            elif char == "3":
                encoded += "^^"
            elif char == "4":
                encoded += "$$"
            elif char == "5":
                encoded += "%%"
            elif char == "6":
                encoded += "]["
            elif char == "7":
                encoded += ")*"
            elif char == "8":
                encoded += "(&"
            elif char == "9":
                encoded += "+"
            elif char == "10":
                encoded += "_"
            else:
                encoded += char
        time.sleep(2)
        print "Encoding message..."
        print "Encrypt : ",encoded
        print ""
        milih()
        
    elif x == 2:
        print "Welcome to Decoder"
        print "+-----------------------------+"
        time.sleep(2)
        message = raw_input("Please enter your dencrypt: ")
        encoded = ""
        for char in message:
            if char == "1":
                encoded += "a"
            elif char == "2":
                encoded += "b"
            elif char == "3":
                encoded += "c"
            elif char == "4":
                encoded += "d"
            elif char == "5":
                encoded += "e"
            elif char == "6":
                encoded += "f"
            elif char == "7":
                encoded += "g"
            elif char == "8":
                encoded += "h"
            elif char == "9":
                encoded += "i"
            elif char == "0":
                encoded += "j"
            elif char == "@":
                encoded += "k"
            elif char == "#":
                encoded += "l"
            elif char == "$":
                encoded += "m"
            elif char == "=":
                encoded += "n"
            elif char == ")(":
                encoded += "o"
            elif char == "//":
                encoded += "p"
            elif char == "~":
                encoded += "q"
            elif char == ";":
                encoded += "r"
            elif char == ":":
                encoded += "s"
            elif char == "{}":
                encoded += "t"
            elif char == "[]":
                encoded += "u"
            elif char == "|":
                encoded += "v"
            elif char == ".":
                encoded += "w"
            elif char == "?":
                encoded += "x"
            elif char == "!":
                encoded += "y"
            elif char == "`":
                encoded += "z"
            elif char == "11":
                encoded += "1"
            elif char == "00":
                encoded += "2"
            elif char == "^^":
                encoded += "3"
            elif char == "$$":
                encoded += "4"
            elif char == "%%":
                encoded += "5"
            elif char == "][":
                encoded += "6"
            elif char == ")*":
                encoded += "7"
            elif char == "(&":
                encoded += "8"
            elif char == "+":
                encoded += "9"
            elif char == "_":
                encoded += "10"
            else:
                encoded += char
        time.sleep(2)
        print "Decoding message..."
        print "Dencrypt :", encoded
        print ""
        milih()
        
    else:
        print ""
        ulang()
        
def ulang():
    print "Maaf anda salah menginput"
    print ''
    n = raw_input("Apakah anda ingin memilih lagi(Y/N): ")
    if n in ["Y", "y"]:
        print ''
        menu()
    elif n in ["N", "n"]:
        exit()
    else:
        print ''
        print "Maaf anda salah menginput"
        print ''
        milih()

def milih():
        n = raw_input("Apakah anda ingin memilih lagi(Y/N): ")
        if n in ["Y", "y"]:
            print ''
            menu()
        elif n in ["N", "n"]:
            exit()
menu()
