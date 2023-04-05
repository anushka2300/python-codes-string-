a=input()
b=a.split()
a=""
for i in b:
    if i not in a:
        a+=i
        a=a+" "
print(a)