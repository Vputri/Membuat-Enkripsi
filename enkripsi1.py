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
        time.sleep(2)
        encrypt = raw_input("Pesan: ")
        encoded = ""
        for char in encrypt:
            if char == "a" or char == "A":
                encoded += "!$"
            elif char == "b" or char == "B":
                encoded += "@"
            elif char == "c" or char == "C":
                encoded += "#"
            elif char == "d" or char == "D":
                encoded += "$"
            elif char == "e" or char == "E":
                encoded += "%"
            elif char == "f" or char == "F":
                encoded += "^"
            elif char == "g" or char == "G":
                encoded += "&"
            elif char == "h" or char == "H":
                encoded += "*"
            elif char == "i" or char == "I":
                encoded += "(*"
            elif char == "j" or char == "J":
                encoded += "*)"
            elif char == "k" or char == "K":
                encoded += "-+"
            elif char == "l" or char == "L":
                encoded += "_"
            elif char == "m" or char == "M":
                encoded += "+"
            elif char == "n" or char == "N":
                encoded += "="
            elif char == "o" or char == "O":
                encoded += "~"
            elif char == "p" or char == "P":
                encoded += "`"
            elif char == "q" or char == "Q":
                encoded += "{"
            elif char == "r" or char == "R":
                encoded += "}"
            elif char == "s" or char == "S":
                encoded += "|"
            elif char == "t" or char == "T":
                encoded += "["
            elif char == "u" or char == "U":
                encoded += "]"
            elif char == "v" or char == "V":
                encoded += "\/"
            elif char == "w" or char == "W":
                encoded += "?"
            elif char == "x" or char == "X":
                encoded += ":"
            elif char == "y" or char == "Y":
                encoded += ";"
            elif char == "z" or char == "Z":
                encoded += "'"
            elif char == 1:
                encoded += "<"
            elif char == 2:
                encoded += ","
            elif char == 3:
                encoded += ">"  
            elif char == 4:
                encoded += "."
            elif char == 5:
                encoded += "?"
            elif char == 6:
                encoded += 7
            elif char == 7:
                encoded += 0
            elif char == 8:
                encoded += 9
            elif char == 9:
                encoded += 8
            elif char == 0:
                encoded += 6
            else:
                encoded += char
        time.sleep(2)
        print "Encoding message..."
        print ""
        print "Encoder = ",encoded

    elif x == 2:
        print "Welcome to Decoder"
        dencrypt = raw_input("dencrypt : ")
        time.sleep(2)
        dencoded = ""
        for char in dencrypt:
            if char == "!$":
                encode += "a"
            elif char == "@":
                encode += "b"
            elif char == "#":
                encode += "c"
            elif char == "$":
                encode += "d"
            elif char == "%":
                encode += "e"
            elif char == "^":
                encode += "f"
            elif char == "&":
                encode += "g"
            elif char == "*":
                encode += "h"
            elif char == "(*":
                encode += "i"
            elif char == "*)":
                encode += "j"
            elif char == "-+":
                encode += "k"
            elif char == "_":
                encode += "l"
            elif char == "+":
                encode += "m"
            elif char == "=":
                encode += "n"
            elif char == "~":
                encode += "o"
            elif char == "`":
                encode += "p"
            elif char == "{":
                encode += "q"
            elif char == "}":
                encode += "r"
            elif char == "|":
                encode += "s"
            elif char == "[":
                encode += "t"
            elif char == "]":
                encode += "u"
            elif char == "\/":
                encode += "v"
            elif char == "?":
                encode += "w"
            elif char == ":":
                encode += "x"
            elif char == ";":
                encode += "y"
            elif char == "'":
                encode += "z"
            elif char == "{":
                encode += 1
            elif char == "}":
                encode += 2
            elif char == "|":
                encode += 3
            elif char == "[":
                encode += 4
            elif char == "]":
                encode += 5
            elif char == 7:
                encode += 6
            elif char == 0:
                encode += 6
            elif char == 9:
                encode += 8
            elif char == 8:
                encode += 9
            elif char == 7:
                encode += 0
            else:
                encode += char
                
        time.sleep(2)
        print "Decoding message..."
        print ""
        print "Encoder = ",encode
        
menu()
