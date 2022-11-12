total = 0
nomer_telepon=input("Masukan Nomer Telepon Pelanggan : ")
tanggal      =input("Masukan Tanggal Pembelian       : ")
nama         =input("Masukan Nama Pelanggan          : ")
alamat       =input("Masukan Alamat Pelanggan        : ")
print("=====================================")
while True :
    print("""============= Menu ==================\n
    1. Mizone       : Rp 5.000\n
    2. Teh Pucuk    : Rp 6.000\n
    3. Kopi         : Rp 4.000\n
    4. Es Teh       : Rp 3.000\n
    5. Aqua         : Rp 2.000 """)
    print("=====================================")
    item = int(input("Masukan nomer angka minuman pada menu :"))
    jumlahPesanan=int(input(" Jumlah dibeli = "))
    if item == 1:
        NamaMinuman    = "Mizone"
        harga           = (5000*jumlahPesanan)
        total           += harga
    elif item ==2:
        NamaMinuman    = "Teh Pucuk"
        harga           = (6000*jumlahPesanan)
        total           += harga
    elif item ==3:
        NamaMinuman    = "Kopi"
        harga           = (4000*jumlahPesanan)
        total           += harga
    elif item ==4:
        NamaMinuman    = "Es Teh"
        harga           = (3000*jumlahPesanan)
        total           += harga
    elif item ==5:
        NamaMinuman    = "Aqua"
        harga           = (2000*jumlahPesanan)
        total           += harga
    else:
        print("tidak jadi beli")
    print("minumanan yang di beli :", NamaMinuman)
    print("harga minumannya :", harga)
    tambah = input("tambah minuman (y/n) :")
    if tambah == "n" :
        print("")
        break

print("=====================================")
print("             TOKO UNKRIS             ")
print(" ====================================")
print("Nama Pelanggan           :"                ,nama)
print("Nomor Telepon Pelanggan  :"                ,nomer_telepon)
print("Alamat Pelanggan         :"                ,alamat)
print("Tanggal Pembelian        :"                ,tanggal)
print("total yang harus dibayar :", total)
print(" ====================================")
print(" =========Datang Lagi Ya :)==========")

