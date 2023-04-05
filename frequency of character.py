a=input()
b=''
for i in a:
    if i not in b:
        print(i,a.count(i),sep=':')
        b=b+i
        
        