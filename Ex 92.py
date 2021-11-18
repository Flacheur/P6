n=int(input("entrez un nombre positif:"))
acc=0
acc2=0
if n>0:
    while n>1:
        if n/2==n//2:
            n=n//2
        else:
            n=n*3+1
        if n>acc2:
            acc2=n
        print(n)
        acc=acc+1
else:
    print("nop")

print("ily a:",acc,"étapes")
print("le nombre le plus grand a été:",acc2)