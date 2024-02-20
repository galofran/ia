def fizz_buzz_cuckoo_clock(time):
    pos = time.index(":")
    hora = int(time[0:pos])
    min = int(time[3:])  
    multiplicador = 0
    
    if hora == 13:
        multiplicador = 1
    elif hora == 14:
        multiplicador = 2
    elif hora == 15:
        multiplicador = 3
    elif hora == 16:
        multiplicador = 4
    elif hora == 17:
        multiplicador = 5
    elif hora == 18:
        multiplicador = 6
    elif hora == 19:
        multiplicador = 7
    elif hora == 20:
        multiplicador = 8
    elif hora == 21:
        multiplicador = 9
    elif hora == 22:
        multiplicador = 10
    elif hora == 23:
        multiplicador = 11
    elif hora == 24 or hora == 00:
        multiplicador = 12

    if min % 3 == 0 and min % 5 == 0:
        if min == 30:
            return "Cuckoo"
        elif min == 0:
            msj = "Cuckoo " * multiplicador
            return f"{msj.strip()}"
        else:
            return "Fizz Buzz"
        #msj = "Cuckoo " * multiplicador
        #return f"{msj.strip()}"
    elif min % 3 == 0:
        return f"Fizz"
    elif min % 5 == 0:
        return f"Buzz"
    else:
        return "a"
    
print(fizz_buzz_cuckoo_clock("12:00"))

