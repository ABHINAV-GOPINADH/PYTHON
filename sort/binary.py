from math import *
a=int(input('enter the number of elements \n'))
print('number of elements : ',a)
print('enter the numbers : \n')

c=[]
f=0
for i in range(a):
    b=input()
    c.append(b)
s=int(input('enter the number to search : '))
h=c[a-1]
l=c[0]
while(h>=l):
    mid=(h+l)//2
    if(c[mid]>s):
        h=mid-1
    elif(c[mid]<s):
        l=mid+1
    else:
        print('the element is present in ',mid)
        f=1
if(f==0):
    print('element is not found') 
    