def Caesar(mes,shift):
    cipher=""
    for i in range(len(mes)):
        char=mes[i]

        if(char.isupper()):
            cipher += chr((ord(char)+shift-65)%26 +65)
        elif(char.islower()):
            cipher += chr((ord(char)+shift-97)%26 +97)
        else:
            cipher += " "
    return cipher


mes="Caesar Text to be manipulated"
for i in range(1,27):
    print(Caesar(mes,i), end='\n')
