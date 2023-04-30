def factor(n):
    fl=[]
    for i in range(1,n+1):
        if(n%i==0):
            fl.append(i)
    return fl
def prime(n):
    if(factor(n)==[1,n]):
        return True
    else:
        return False
def no_prime(n):
    pl=[]
    for i in range(1,n+1):
        if(prime(i)==True):
            pl.append(i)
    print(pl)
        
n=int(input('enter the number : '))
r=prime(n)
if(r==True):
    print('prime')
else:
    print('not prime')
no_prime(n)