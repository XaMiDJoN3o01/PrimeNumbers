import math

# input natural n
n = int(input("natural n= "))
list = []

# making list of natural numbers
for i in range(2,n+1):
    list.append(i)

# finding prime numbers
for i in range(2,int(math.sqrt(n))+1):
    for j in list:
        if(j%i == 0 and i!=j):
            list.remove(j)
print(list)