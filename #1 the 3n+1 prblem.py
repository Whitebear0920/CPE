def nnn(n):
    t=1
    while n!=1:
        if n%2:
            n=n*3+1
        else:
            n/=2
        t+=1
    return t
try:
    num = input().split()
    j,i = int(max(num)),int(min(num))
    max=0
    z=0
    for x  in range(i,j+1):
        z = nnn(x)
        if z>max:
            max = z
    print(num[0],num[1],max)
except:
    pass