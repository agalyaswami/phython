def pattern(n):
    for i in range(0,n):
        for k in range(n-i,0):
            print(" ",end="")
        
            
        for j in range(0,n-i):
            print("*",end="")
        print("\r")
n=5
pattern(n)
