n = input("Masukkan nilai n : ")

if n.isnumeric() == False : 
    print("Mohon masukkan nilai n yang valid!")
else :
    n = int(n)
    evenNumber = [i for i in range(n, pow(n, 2) + 1) if i % 2 == 0]
    print("Bilangan genap dari " + str(n) + " sampai " + str(pow(n, 2)) + " adalah : ", evenNumber)