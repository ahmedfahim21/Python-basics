from email import message


plain_text="The string to be reversed"
cipher_text= ""
i=len(plain_text)-1

while(i>=0):
    cipher_text+= plain_text[i]
    i-=1

print(cipher_text)