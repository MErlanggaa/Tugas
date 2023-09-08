
def tabung ( b, c):
    volume = 22/7 * b * c
    luas = 2*22/7*b*(b + c)
    return volume,luas
def balok ( a, b , c):
    volume = a * b * c
    return volume

def main():
    ma = input("masukkan yang ingin di pake rumus (tabung, balok): ")

    if ma == "tabung":
       
        b = float(input("masukkan jari"))
        c = float(input("masukkan tinggi"))
        volume, luas = tabung( b, c)
    elif ma == "balok":
        a = float(input("panjang : "))
        b = float(input("lebar : "))
        c = float(input("tinggi"))
        volume =balok (a, b, c)
        
    else:
        print("Tidak ada rumus.")
        return

    print(f"volume: {volume}")
    print(f"luas: {luas}")

if __name__ == "__main__":
    main()
