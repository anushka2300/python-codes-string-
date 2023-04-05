a=input()
b=''
for i in range(len(a)-1,-1,-1):
   b=b+a[i]
print(b)
if(a==b):
    print("YES")
else:
    print("NO") 
    