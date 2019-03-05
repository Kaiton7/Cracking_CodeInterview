S = input()

def Solve(S):
    compress = ""
    counter=0

    for i in range(len(S)):
        if(i!=0 and S[i]!=S[i-1]):
            compress+=S[i-1]+str(counter)
            counter=0
        counter+=1
    compress+=S[-1]+str(counter)
    return min(S,compress,key=min)
print(Solve(S))

