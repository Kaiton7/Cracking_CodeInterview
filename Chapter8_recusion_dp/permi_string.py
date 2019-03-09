
def Solve(S):
    result=[]
    getperms(" ",S,result)
    return result

def getperms(prefix,remainder, result):
    if(len(remainder)==0):
        result.append(prefix)
    l = len(remainder)
    for i in range(l):
        b = remainder[:i]
        a=remainder[i+1:]
        res= remainder[i]
        getperms(prefix+res,a+b,result)

print(Solve("str"))