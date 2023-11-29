def filewrite(a,b):
        f = open(b,"w")
        f.write(a)
        f.close()
def fileread(b):
        f = open(b,"r")
        content = f.readlines()
        return content[0]
        f.close()

