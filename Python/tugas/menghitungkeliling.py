#a = sisi ( alas atas )
#b = panjang (alas  bawah )
#c = lebar ( tinggi)
#d = sisi miring

def persegi(a):
    luas = a ** 2
    keliling = 4 * a
    return luas, keliling

def persegipanjang(b, c):
    luas = b * c
    keliling = 2 * (b + c)
    return luas, keliling

def trapesium(a, b, c, d):
    luas = 0.5 * (a + b) * c
    keliling = a + b + (2 * d)
    return luas, keliling

def main():
    ma = input("masukkan yang ingin di pake rumus (persegi, persegipanjang, trapesium): ")

    if ma == "persegi":
        a = float(input("panjang : "))
        luas, keliling = persegi(a)
    elif ma == "persegipanjang":
        b = float(input("panjang : "))
        c = float(input("lebar : "))
        luas, keliling = persegipanjang(b, c)
    elif ma == "trapesium":
        a = float(input("alas 1: "))
        b = float(input("alas 2: "))
        c = float(input("tinggi: "))
        d = float(input("sisi miring "))
        luas, keliling = trapesium(a, b, c, d)
    else:
        print("Tidak ada rumus.")
        return

    print(f"Luas: {luas}")
    print(f"Keliling: {keliling}")

if __name__ == "__main__":
    main()
