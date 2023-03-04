n = input("Masukkan nilai n : ")

if n.isnumeric() == False : 
    print("Mohon masukkan nilai n yang valid!")
else :
    n = int(n)
    factorials = [x for x in range(1, n+1) if n % x == 0]
    print("Faktor pembagi dari " + str(n) + " adalah : ", factorials)