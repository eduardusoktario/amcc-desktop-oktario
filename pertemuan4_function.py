##Fungsi di Python
# def salam():
#     print ("Hai, Selamat Siang")
# salam()

##Fungsi Dengan Parameter
# def luas_segitiga (alas,tinggi):
#     luas = (alas * tinggi ) / 2
#     print ('Luas Segitiga: : %f'%luas)

# #%f = Float
# luas_segitiga(4,6)

##Fungsi Pakai Return
# def persegi(sisi):
#     return sisi * sisi

# print(persegi(10))

##Segitiga yang diatas versi Return
# def segitiga(alas,tinggi):
#      luas = alas*tinggi/2
#      return luas

# print(segitiga(6,8))

#Membuat Variabel Global dan Variabel Lokal
##Global = Bisa Diakses Semua Fungsi
##Lokal = Hanya Bisa Diakses Dalam Fungsi Tempat Ia Berada

#Deklarasi Variabel Global
nama = "Rio"
versi = "1.0.0"

def help():
    #Deklarasi Variabel Lokal
    nama = "Oktario"
    versi = "1.0.1"
    #Akses Variabel Lokal
    print ('Nama: %s'%nama)
    print ('Versi: %s'%versi)

#Mengakses Variabel Global
print ('Nama: %s'%nama)
print ('Versi: %s'%versi)

#Memanggil Fungsi Help()
help()