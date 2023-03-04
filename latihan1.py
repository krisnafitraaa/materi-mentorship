#latihan faktorisasi dan dictionary dan fungsi

def factorization(number) :
    factorization_number = {}

    counter = 1
    
    while True :
        fact_details = {}
        should_break = True

        for i in range(2, number) :
            if number % i == 0 :
                fact_details[i] = int(number / i)
                factorization_number["faktorisasi ke - " + str(counter)] = fact_details
                number = fact_details[i]
                counter += 1
                should_break = False
                break

        if len(factorization_number) == 0 :
            fact_details[number] = 1
            factorization_number["faktorisasi ke - " + str(counter)] = fact_details

        if should_break :
            break

    print(factorization_number)

number = int(input("Masukkan bilangan faktorisasi: "))
factorization(number)