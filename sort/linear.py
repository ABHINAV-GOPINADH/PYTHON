a=int(input('enter the number of elements \n'))
print('number of elements : ',a)
print('enter the numbers : \n')

c=[]
f=0
for i in range(a):
    b=input()
    c.append(b)
s=input('enter the number to search')
for i in range(a):
    if(c[i]==s):
        print('element found at position ',(i+1))
        f=1
if(f==0):
    print('element not found')