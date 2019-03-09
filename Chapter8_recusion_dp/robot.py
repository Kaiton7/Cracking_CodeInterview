'''
def Solve(Matrix):
    s_r,s_c=0,0
    t_r,t_c=len(Matrix),len(Matrix[0])
    dp=[[0]*len(t_c)]*t_r

    detect_path(s_r,s_c,t_r,t_c,Matrix,dp)


def detect_path(s_r,s_c,t_r,t_c,Matrix,dp):
    if(s_r==t_r and s_c==t_c):
        return dp[t_r][t_c]
    direction=[[1,0],[0,1]]
    for i in direction:
        dx=i[0]
        dy=i[1]
        if(dp[s_r+dx][s_c+dy]>dp[s_r][s_c]+1):
            dp[s_r+dx][s_c+dy]=dp[s_r][s_c]+1
'''


def Solve(Matrix):
    if(Matrix==None or len(Matrix)==0):
        return None
    path=[]
    fielddp=[]
    if findpath(Matrix,len(Matrix)-1,len(Matrix[0])-1,path,fielddp):
        print(fielddp)
        return path
    return None

def findpath(Matrix,t_r,t_c,path,fielddp):
    if(t_r<0 or t_c<0 or not(Matrix[t_r][t_c])):
        return False

    point = (t_r,t_c)

    if point in fielddp:
        print("failed")
        return False

    isAtorigin=(t_c==0) and (t_r==0)
    #左と上を探しに行って、両方共行き止まりならそのポイントは調べたってことでfielddpに記録するよ
    if(isAtorigin or findpath(Matrix,t_r,t_c-1,path,fielddp) or findpath(Matrix,t_r-1,t_c,path,fielddp)):
        path.append(point)
        print(fielddp)
        return True
    print("tt")
    fielddp.append(point)
    return False

print(Solve([   [True, True,True,True],
                [True,False,False,True],
                [False,True,True,True]]))
