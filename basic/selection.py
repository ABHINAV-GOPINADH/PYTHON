def selection(a,n):
    for i in range(n):
        min=i
        for j in range(1,n):
            if(a[min]>a[j]):
                min=j
        (a[i],a[min])=(a[min],a[i])
    print(a)
n=int(input("enter the number "))
a=[]
print('enter the numbers :')
for i in range(n):
    b=input()
    a.append(b)
selection(a,n)