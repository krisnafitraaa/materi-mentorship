n = input("Masukkan nilai n : ")

if n.isnumeric() == False : 
    print("Mohon masukkan nilai n yang valid!")
else :
    n = int(n)
    sigma = [2*i if i % 2 == 0 else 3*i for i in range(n+1)]
    print("Persamaan dari 2i jika bilangan genap dan 3i jika tidak dimana i=0.." + str(n) + " adalah : ", sigma)