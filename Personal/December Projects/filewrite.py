def filewrite(a,b):
        f = open(b,"w")
        f.write(a)
        f.close()
def fileread(a,b):
        f = open(b,"r")
        content = file.readlines()
        return content[0]
        f.close()
filewrite("yoooo","test.txt")
