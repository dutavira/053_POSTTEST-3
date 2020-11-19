stop = False
while(not stop):
    print("====================================================\n"
          "           SELAMA DATANG DI TOKO TAKOYAKI           \n"
          "====================================================")
    nama = input("Masukkan nama Anda : ")
    print("----------------------------------------------------")
    print("-Berikut Takoyaki yang kami sediakan :\n"
          "1. Takoyaki varian 1 (Original) - Rp. 2000\n"
          "2. Takoyaki varian 2 (Cheese Mentaiko)- Rp. 2500\n\n"
          "-Diskon Spesial Bila Memesan:\n"
          "Varian 1 sebanyak 10/lebih, diskon 10%\n"
          "Varian 2 sebanyak 8/lebih, diskon 8%")
    print("----------------------------------------------------")
    pesanan = int(input("Masukkan varian yang anda inginkan (1/2) : "))
    print("----------------------------------------------------")
    jumlah = int(input("Berapa Takoyaki yang ingin Anda pesan : "))
    print("----------------------------------------------------")
    total1 = jumlah * 2000
    total2 = jumlah * 2500
    if pesanan == 1 and total1 > 20000 and total1 < 90000 :
        print("Selamat Anda mendapatkan diskon spesial 10%")
    elif pesanan == 1 and total1 < 20000 :
        print("Mohon maaf Anda tidak mendapatkan diskon")
    elif pesanan == 1 and total1 > 90000 :
        print("Mohon maaf kami hanya menyediakan 45pcs")    
    elif pesanan == 2 and total2 > 20000 and total2 < 100000 :
        print("Selamat Anda mendapatkan diskon spesial 8%")
    elif pesanan == 2 and total2 < 20000 :
        print("Mohon maaf Anda tidak mendapatkan diskon")
    elif pesanan == 2 and total2 > 100000 :
        print("Mohon maaf kami hanya menyediakan 45pcs")       
    else :
        print("Mohon maaf pilihan Anda tidak tersedia")
    print("----------------------------------------------------")
    print("Pemesanan dengan : \n\n"
          "Atas Nama        : ", nama, "\n"
          "Takoyaki Varian  : ", pesanan, "\n"
          "Banyak Pesanan   : ", jumlah,)

    if pesanan == 1 and total1 > 20000 and total1 < 90000 :
        print("Voucher Diskon 10%")
        diskon1 = jumlah * (2000 - (2000 * (10/100)))
        print("Total Harga      :  Rp ", diskon1)
    elif pesanan == 1 and total1 < 20000 :
        print("Total Harga      :  Rp ", total1)
    elif pesanan == 1 and total1 > 90000 :
        print("           !!! Pemesanan Tidak Valid !!!            ")
    elif pesanan == 2 and total1 > 20000 and total2 < 100000 :
        print("Voucher Diskon 8%")
        diskon2 = jumlah * (2500 - (2500 * (8/100)))
        print("Total Harga      :  Rp ", diskon2)
    elif pesanan == 2 and total2 < 20000 :
        print("Total Harga      :  Rp ", total2)
    elif pesanan == 2 and total2 > 100000 :
        print("           !!! Pemesanan Tidak Valid !!!            ")
    else :
        print("           !!! Pemesanan Tidak Valid !!!            ")
    print("----------------------------------------------------")
    ulangi = input("Apakah Anda ingin memesan lagi? (ya/tidak) : ")
    print("----------------------------------------------------\n")
    if ulangi == "tidak" :
        stop = True
print("====================================================\n"
      "                  SILAHKAN MENUNGGU                 \n"
      "           PESANAN ANDA SEDANG KAMI PROSES          \n"
      "         ---TERIMAKASIH ATAS KUNJUNGANNYA---        \n"
      "====================================================\n\n")
