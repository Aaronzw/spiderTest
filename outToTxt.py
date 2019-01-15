def outTxt(str,fileName='C:\SPIDER\out.txt'):
    with open(fileName, "a") as f:
        f.writelines(str)
        f.write("\n")
