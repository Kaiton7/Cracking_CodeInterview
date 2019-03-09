def Solve (n):
    li = [""]*((n+1)*2)
    pok  = [""]
    addParan(pok,n,n,li,0)
    #print(li)
    return pok
c=0

def addParan(pok,leftRem,rightRem,li,index):
    if(leftRem<0 or rightRem < leftRem):
        return False
    if(leftRem==0 and rightRem==0):
        global c
        c+=1
        pok=pok+li
        print(li)
        if(li[0]==")"):
            print(leftRem,rightRem,index)
    else:
        # print("inde")
        li[index]="("
        addParan(pok,leftRem-1,rightRem,li,index+1)
        li[index]=")"
        addParan(pok,leftRem,rightRem-1,li,index+1)

Solve(4)
          
print(c)