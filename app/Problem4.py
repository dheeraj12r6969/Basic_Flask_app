class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        i=0
        new_pathList=new_path.split('/')   #converting path into list for use
        pathLength=len(new_pathList)
        pathList=self.current_path.split('/')
        if new_pathList[0]=='':
            #direct pathname
            del pathList[:]
            pathList.append('/'+new_pathList[1])
            i=i+2
        while(i<pathLength):
            j=len(pathList)-1
            if new_pathList[i]=='..':
                pathList.pop(j)
            else:
                pathList.append(new_pathList[i])
            i=i+1
        self.current_path="/".join(pathList)
        pass

# ConsoleInput = input("Enter current path seperated by '/' (eg: /a/b/c/d) : ")
# NewPath = input("Enter new path : ")
# path = Path(ConsoleInput)
# path.cd(NewPath)
path = Path("/a/b/c/d")
path.cd("../z")
print(path.current_path) # '/x/z'