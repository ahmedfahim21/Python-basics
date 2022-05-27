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

shift=int(input("Shift="))
mes="Caesar Text to be manipulated"
print(Caesar(mes,shift))