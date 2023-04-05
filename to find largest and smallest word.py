a=input()
x=a.split()
print(x)
max1=min1=len(x[0])
for i in x:
    l=len(i)
    if(l>max1):
        max1=l
    if(l<min1):
        min1=l
for i in x:
    if(len(i)==max1):
        print("largest word is:",i)
    if(len(i)==min1):
        print("smallest word is:",i)
            
