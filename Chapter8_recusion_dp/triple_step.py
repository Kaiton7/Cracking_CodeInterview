'''
fibonacciのmemoを使用した例と再帰でやってしまった例
def fib(n):
    li = [0]*(n+1)
    return fib_memo(n,li)

def fib_memo(n, memo):
    if(n==0):
        return 0
    elif(n==1):
        return 1

    elif(memo[n]==0):
        memo[n]=fib_memo(n-1,memo)+fib_memo(n-2,memo)
    return memo[n]
print(fib(200))
def solve(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return solve(n-1)+solve(n-2)
print(solve(34))
'''

def Solve(n,memo):
    if(n<0):
        return 0
    elif(n==0):
        return 1
    elif(memo[n]==-1):
        memo[n]=Solve(n-1,memo)+Solve(n-2,memo)+Solve(n-3,memo)
        
    return memo[n]

N=40
memo = [-1]*(N+1)
print(Solve(N,memo))