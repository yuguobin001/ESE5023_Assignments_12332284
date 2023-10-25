import numpy as np
def Matrix_multip(x,y):
    m,p = x.shape
    p,n = y.shape
    result = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            s = 0
            for a in range(p):
                e = x[i,a]*y[a,j]
                s =s+e
            result[i,j]= s
    print(result)
M1 = np.random.randint(0, 51, size=(5, 10))
M2 = np.random.randint(0, 51, size=(10, 5))
Matrix_multip(M1,M2)