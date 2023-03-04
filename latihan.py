def convertDistance(distance_value, a_distance, b_distance) :
    if distance_value.isnumeric() == False :
        print("Oops nilai jarak tidak valid") 
        exit()

    distance_value = int(distance_value)

    list_distance_unit = ["mm", "m", "km"]
    index_a = None
    index_b = None

    for i in range(0, len(list_distance_unit)) :
        if a_distance.lower() == list_distance_unit[i].lower() :
            index_a = i

        if b_distance.lower() == list_distance_unit[i].lower() :
            index_b = i


    if index_a == None or index_b == None :
        print("Oops satuan jarak tidak ditemukan")
    else :
        value = 0
        conversion_value = 1000

        if index_a - index_b > 0 :
            value = distance_value * pow(conversion_value, (index_a - index_b))
        else :
            value = distance_value / pow(conversion_value, abs((index_a - index_b)))

        print("Jadi jarak ", distance_value, a_distance, "ke", b_distance, "adalah :", value)



distance_value = input("Masukkan jumlah jarak : ")
a_distance = input("Masukkan satuan jarak : ")
b_distance = input("Masukkan satuan jarak konversi :")

convertDistance(distance_value, a_distance, b_distance)