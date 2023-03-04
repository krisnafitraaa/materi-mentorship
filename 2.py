def printPrimeNumber(max) :
    max = int(max)
    for i in range(1, max):
        if i == 2 or (i % 2 != 0 and i > 1):
            print(i, end=' ')
            
maxNum = input("Masukkan angka prima : ")
printPrimeNumber(maxNum)