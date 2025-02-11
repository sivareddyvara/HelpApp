for n in range(1,50):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
x=[i for i in range(1,50) if all(i%j!=0 for j in range(2,i))]
print(x)