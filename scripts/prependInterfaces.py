import os


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
            fdat.insert(0, "// [[Rcpp::interfaces(cpp,r)]]\n")
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


