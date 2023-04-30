a = int(input('Enter the number of elements: '))
print('Number of elements:', a)
b = []
for i in range(a):
    element = int(input('Enter element {}: '.format(i+1)))
    b.append(element)
for i in range(a):
    for j in range(a-i-1):
        if(b[j]>b[j+1]):
            b[j],b[j+1]=b[j+1],b[j]
print('sorted array',b)
