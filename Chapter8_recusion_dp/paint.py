Color = ["Red","Blue","Green"]
def Paintfill(screen,r,c,ncolor):
    if(screen[r][c]==ncolor):
        return False
    
    return Paintdfs(screen,r,c,screen[r][c],ncolor)

def Paintdfs(screen,r,c,ocolor,ncolor):
    if(r<0 or c<0 or r>len(screen) or c>len(screen[0])):
        return False

    if(screen[r][c]==ocolor):
        Paintdfs(screen,r-1,c,ocolor,ncolor)
        Paintdfs(screen,r,c-1,ocolor,ncolor)
        Paintdfs(screen,r+1,c,ocolor,ncolor)
        Paintdfs(screen,r,c+1,ocolor,ncolor)
    return True


