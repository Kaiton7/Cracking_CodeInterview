def Solve(S,T):
    if len(S)==len(T):
        return is_substring(S+S,T)
    return False

def is_substring(S,T):
    return S.find(T) != -1

S = input()
T = input()

Solve(S,T)


