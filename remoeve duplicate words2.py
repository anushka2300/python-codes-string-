j=input()
a=j.split()
x=[]
for i in a:
    if(j.count(i)>=1  and (i not in x) ):
        x.append(i)
print(''.join(x))    