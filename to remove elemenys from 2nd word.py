a=input()
b=input()

for i in a:
    for j in b:
        if(i in j):
            b=b.replace(i,"")
print("afeter modification:",b)       

    