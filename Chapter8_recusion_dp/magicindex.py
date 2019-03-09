def Solve(L):
    n = len(L)//2
    if(L[n]>n):
        return Solve(L[:n])
    elif(L[n]<n):
        return Solve(L[n:])
    
    return print(L[n])

def FillArray():
    array = [0] * 11
    array[0] = -14
    array[1] = -12
    array[2] = 0
    array[3] = 1
    array[4] = 4
    array[5] = 5
    array[6] = 9
    array[7] = 10
    array[8] = 23
    array[9] = 25
    array[10]=30
    return array

array = FillArray()
Solve(array)
