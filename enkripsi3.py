import time
def menu():
    print "                           TUGAS SISTEM OPERASI"
    print "                          MEMBUAT ENKRIPSI BARU"
    print "                                  By :"
    print "                      Vika Putri Ariyanti (56417094)"
    print "                      Rifqy Adli Damhuri  (55417203))"
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
        key = 'qwertyuiopasdfghjklzxcvbnm'
        offset = 5
        def encrypt(n, message):
            result = ''
            for l in message.lower():
                try :
                    i = (key.index(l) + n) % 26
                    result += key[i]
                except ValueError:
                    result += l
            return result.lower()
        encrypted = encrypt(offset, message)
        print'Encrypted:', encrypted
        milih()
        
    elif x == 2:
        print "Welcome to Decoder"
        print "+-----------------------------+"
        time.sleep(2)
        message = raw_input("Please enter your dencrypt: ")
        key = 'qwertyuiopasdfghjklzxcvbnm'
        offset = 5
        def decrypt(n, message):
            result = ''
            for l in message:
                try:
                    i = (key.index(l) - n) % 26
                    result += key[i]
                except ValueError:
                    result += l
            return result
        dencrypted = decrypt(offset, message)
        print 'Encrypted:', dencrypted
        milih()
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
