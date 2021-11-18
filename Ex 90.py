def nb_chiffres(n):
    acc=0
    
    while n>0:
        n=n//10
        acc=acc+1
    
    return acc