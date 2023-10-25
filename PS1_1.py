import numpy as np
def Print_values(a,b,c):
    if a>b:
        if b>c:
            print(a,b,c)
        elif a>c:
            print(a,c,b)
        else:
            print(c,a,b)
    else :
       if b>c:
           print()
       else:
           print(c,b,a)
Print_values(np.random.randint(1,100),np.random.randint(1,100),np.random.randint(1,100))