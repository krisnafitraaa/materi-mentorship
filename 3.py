def checkTollTicket(vehicle) :
    #force to lowercase
    vehicle = vehicle.lower()
    #remove whitespace character from words
    vehicle = vehicle.strip()

    list_vehicles = ["mobil", "truk", "bus"]

    for v in list_vehicles:
        if vehicle == v :
            return True
        
    return False

while True:
    vehicle = input("Masukkan jenis kendaraan : ")

    if checkTollTicket(vehicle) :
        print("Silahkan Masuk")
        break
    else :
        print("Anda tidak termasuk jenis kendaraan yang boleh masuk ke tol, Silahkan Ulangi!")

