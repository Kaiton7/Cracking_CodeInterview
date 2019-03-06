def Solve(M):
    m = len(M)
    n = len(M[0])
    print(m,n)
    RowhasZero,ColhasZero=False,False
    for i in range(n):
        if(M[0][i]==0):
            RowhasZero=True
            break
    for i in range(m):
        if(M[i][0]==0):
            ColhasZero=True
            break
    for i in range(m):
        for j in range(n):
            if(M[i][j]==0):
                M[i][0]=0
                M[0][j]=0
    print(M)
    for i in range(1,n):
        if(M[0][i]==0):
            print(i)
            nullify_col(M,i)
    for i in range(1,m):
        if(M[i][0]==0):
            print(i)
            nullify_row(M,i)
    if(RowhasZero):
        nullify_row(M,0)
    if(ColhasZero):
        nullify_col(M,0)
    print(M)

def nullify_row(M,row):
    for i in range(len(M[0])):
        M[row][i]=0

def nullify_col(M, col):
    for i in range(len(M)):
        M[i][col]=0


matrix = [  [1, 2, 3, 4, 0,9],
            [6, 0, 8, 9, 10,22],
            [11, 12, 13, 14, 15,23],
            [16, 0, 18, 19, 20,24],
            [21, 22, 23, 24, 25,26]]

Solve(matrix)
