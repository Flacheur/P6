acc=0
acc2=0
for i in range(1,20):
    while i>1:
        if i/2==i//2:
            i=i//2
        else:
            i=i*3+1
        if i>acc2:
            acc2=i
        print(i)
        acc=acc+1
    print("il y a:",acc,"étapes")
    print("le nombre le plus grand a été:",acc2)
    acc=0
    acc2=0