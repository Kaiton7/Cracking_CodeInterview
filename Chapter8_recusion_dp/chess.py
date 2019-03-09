GS=8
c=0

def Solve(row, point):
    if(row==GS):
        global c
        c+=1
        print(point)

    else:
        for col in range(8):
            if(check(point,row,col)):
                point[row]=col
                Solve(row+1,point)

    #print(res)


def check(point, row, col):
    for r in range(row):
        p = point[r]
        if(col==p):
            return False
        
        columnDistance=abs(p-col)
        rowDistance=row-r
        if(columnDistance==rowDistance):
            return False
    return True


Solve(0,[0]*8)

    
print(c)