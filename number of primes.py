n=int(input('no of primes to be generated : '))
counter=0
n1=2
while True:
    is_prime=True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(n1)
        counter=counter+1
    if counter==n:
        break
    n1=n1+1