n=int(input('num:'))
inc=1
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(' ',end='')
    for k in range(1,inc+1):
        print(k,end='')
    inc+=2
    print()