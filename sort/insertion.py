def insertion(a,n):
    for i in range(1,n):
        temp=a[i]
        j=i-1
        while j>=0 and temp<a[j]:
            (a[j],temp)=(temp,a[j])
    print(a)
n=int(input("enter the number "))
a=[]
print('enter the numbers :')
for i in range(n):
    b=input()
    a.append(b)
insertion(a,n)