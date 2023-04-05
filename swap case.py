a=input()
x=""
for i in a:
    if(65<=ord(i)<=90):
        x=x+chr(ord(i)+32)
    elif(97<=ord(i)<=122):
        x=x+chr(ord(i)-32)
print(x)        