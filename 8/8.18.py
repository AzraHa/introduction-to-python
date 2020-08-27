for i in range(11,100):
    stri = str(i)
    if stri[0] == stri[1]:
        for j in range(101,1000):
            strj = str(j)
            if strj[0] == strj[2]:
                r = int(stri) + int(strj)
                strr = str(r)
                if len(strr) == 4 and strr[0] == strr[3] and strr[1] == strr[2]:
                    print(i,j,r)

