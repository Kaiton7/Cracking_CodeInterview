'''
文字コード確認、大文字小文字、スペースの確認
'''
from collections import Counter

c = Counter()

S = input()
T = input()
def Solve(S,T):
    for i in S:
        c[i]+=1

    for i in T:
        if(c[i]==0):
            return False
        c[i]-=1

    return True

def Solve_hash(S,T):
    L = [0]*256
    for i in S:
        L[ord(i)]+=1
    for j in T:
        L[ord(j)]-=1
        if(ord(j)<0):
            return False
    return True

print(Solve(S,T))
print(Solve_hash(S,T))