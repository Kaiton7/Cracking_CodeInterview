'''
文字列を一つずつ取り出して奇数個かどうか判定していく
'''
S = input

def Solve(S):
    L = [0]*128
    for i in S:
        i = ord(i)
        L[i]+=1
        if(L[i]%2):
            CO+=1
        else:
            CO-=1
    if(CO<=1):
        print("S is palindrome")
    else:
        print("S isn't palindrome")

Solve(S)
