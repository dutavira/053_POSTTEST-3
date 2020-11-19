print("==== Menghitung Bilangan 10^x terkecil >  N====\n")
n = int(input("Masukkan nilai dari N : "))
x = 0
while x < n:
    if (10 **x > n):
        break
    else:
        print("Menghitung bilangan terkecil")
    x += 1

print("Bilangan terkecil dari 10^x > N adalah : ", 10 ** x)