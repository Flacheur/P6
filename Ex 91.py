n=int(input("entrez un nombre positif:"))
if n>0:
    while n>1:
        if n/2==n//2:
            n=n//2
        else:
            n=n*3+1
        print(n)
else:
    print("nop")