def filewrite(file, line, message):
        with open (file,'r') as b:
            content = b.readlines()
        with open(file,'w') as f:
            written = False
            for i,l in enumerate(content):
                if i == line:
                    f.write(message)
                    f.write("\n")
                    written = True
                else:
                    f.write(l)
            if not written:
                for x in range(line - (len(content))):
                    f.write("\n")
                f.write(message)
def fileclear(file):
    with open(file,'w') as f:
        pass
def filereplace(file, newfile):
    with open(newfile, "r") as f:
        content = f.readlines()
    with open(file,'w') as f:
        for l in content:
            f.write(l)
    f.close()
def fileread(file, line):
        f = open(file,"r")
        content = f.readlines()
        return content[line]
        f.close()




