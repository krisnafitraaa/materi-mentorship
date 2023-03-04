#notes : running on python >= 3, because i'am using end=''. 
def printMyNRP(size) :
    #casting j to integer
    size = int(size)

    #force size minimum to 6
    if size < 6 :
        size = 6

    #my last NRP is : 110
    nrp = "110"

    #print newline space to give newline space after input
    print("")
    print("")

    for x in nrp :
        match x:
            case "1":
                #process print number 1
                for i in range(0, size) :
                    if i == 1:
                        print(x, x)
                    elif i == size - 1:
                        print(x, x, x)
                    else :
                        print(" ", x)
            case "0":
                #process print number 0
                for i in range(0, size) :
                    for j in range(0, size) :
                        if j == 0 or j == size - 1 :
                            print(x, end=' ')
                        else :
                            if i == 0 or i == size - 1 :
                                print(x, end=' ')
                            else :    
                                print(" ", end=' ')
                    
                    print("")

        print("")


size = input("Masukkan size (minimal 6): ")
printMyNRP(size)