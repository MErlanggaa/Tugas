a = int(input("masukkan jumlah baris : "))
a
for i in range(0, a):
    for j in range(0, i + 1):
        print('* ' , end='')
    print('')