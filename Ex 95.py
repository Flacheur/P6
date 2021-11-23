def digramme(a,b,t):
    for i in range(len(t)-1):
        if t[i]==a and t[i+1]==b:
            return True
    
    return False