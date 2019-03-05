S1 = input()
S2 = input()
l1=len(S1)
l2=len(S2)

def Solve(S1,S2):
    if(l1==l2):
        return one_edit(S1,S2)

    elif(l1-1 == l2):
        return one_edit_insert(S1,S2)
    elif(l1+1==l2):
        return one_edit_insert(S2,S1)
    return False

def one_edit(S1,S2):
    edit=False
    for i,j in zip(S1,S2):
        if(i != j):
            if(edit):
                return False
            edit =True
        
    return True

def one_edit_insert(S1,S2):
    edit=False
    i,j=0,0
    while(i<len(S1) and j<len(S2)):
        if(S1[i]!=S2[j]):
            if(edit):
                return False
            edit=True
            j+=1
        else:
            i+=1
            j+=1
        return True
        
if(Solve(S1,S2)):
    print("ok")
else:
    print("NG")

    