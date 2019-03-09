def Solve(box):
    box.sort(reverse=True)
    print(box)
    maxHeight=0
    stackmap = [0]*(len(box)+1)
    for i in range(len(box)):
        height = CS(box, i, stackmap)
        maxHeight=max(maxHeight,height)

    return maxHeight

def CS(box,bottomindex,stackmap):
    if(bottomindex<len(box) and stackmap[bottomindex]>0):
        print("test")
        return stackmap[bottomindex]

    bottom = box[bottomindex]
    maxHeight=0
    print(bottom,bottomindex)
    for i in range(bottomindex+1,len(box)):
        if(canbeAbove(box[i],bottom)):
            if(bottom[0]==19):
                print("tetete",box[i])
            height = CS(box, i, stackmap)
            maxHeight=max(maxHeight,height)
    
    maxHeight+=bottom[0]
    stackmap[bottomindex]=maxHeight
    # print("test")
    return maxHeight

def canbeAbove(over,under):
    for i in range(3):
        # print("test")
        if(over[i]>under[i]):
            print("failed to above",over,under)
            return False

    return True

S=[[19,20,21],[1,2,100],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
print(Solve(S))
    