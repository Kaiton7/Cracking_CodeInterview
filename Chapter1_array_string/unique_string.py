# まず文字コードを確認する
# 今回はASCIIと仮定

S = input()

def unique_string(S):
    if(len(S)>128):
        return False
    char_set = [False for i in range(128)]
    for ch in S:
        if(char_set[ord(ch)]):
            return False
        char_set[ord(ch)] = True
    return True

print(ord("z"))

def unique_bool(S):
    checker = 0
    for i in S:
        val = ord(i)
        if(checker & (1 << val)>0):
            return False
        checker |= (1 << val)
        
    return True

def never_new_mem(S):
    S=list(S)
    S.sort()
    print(S)
    for i in range(len(S)-1):
        if(S[i+1]==S[i]):
            return False
    
    return True


if(never_new_mem(S)):
    print("yes")

if(unique_bool(S)):
    print("yes")