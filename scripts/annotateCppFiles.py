import os

cl = open("./CAF_classes.csv", "r")
cl_l = cl.readlines()
classes = cl_l[1][2:(len(cl_l[1])-1)].split(",")

outLines = []

def processFiles(dirname):
    savedPath = os.getcwd()
    os.chdir(dirname)
    err = 0
    try:
        files = [x for x in os.listdir("./") if (".cpp" in x)]
        for f in files:
            print(f)
            f_handle = open(f, "r")
            fdat = f_handle.readlines()
            idx = 0
            lines_since_annot = 0
            insert_idx = []
            for ln in fdat:
                #tmpln = ln.replace("std::", "")
                if (ln[0] != " " and any([(x + "::") in ln for x in classes]) and lines_since_annot > 0):
                    outLines.append(ln)
                    insert_idx.insert(0, idx)
                    lines_since_annot = 0
                lines_since_annot += 1
                    #fdat.insert(idx, "// [[register]]\n")
                idx += 1
            for idx in insert_idx:
                fdat.insert(idx, "// [[register]]\n")
            f_handle.close()
            f_handle = open(f, "w")
            f_handle.writelines(fdat)
            f_handle.close()
    except(e):
        print(e)
        err = 1
        os.chdir(savedPath)
    finally:
        if (err == 0):
            os.chdir(savedPath)
        


processFiles("../RcppCAF/src/libcaf_core")
processFiles("../RcppCAF/src/libcaf_io")


