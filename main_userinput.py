# input? user
# target bisa str int sama bool

#1
data = input("masukan data:") #pasti jadinya str walaupun masukin angka
print("data=",data,"tipe=",type(data))

#2 int???
angka = int(input("masukan angka:")) # kita casting str ---> int biar kalo masukin angka jadi int
print("hasil=",angka,"tipe=",type(angka))

#3 BooL
biner = bool(int(input("1 or 0?"))) # CARA JADI BOOL = CASTING STR-->INT--->BOOL MAKA KALO 1=TRUE KALO 0=FALSE
print("hasil=",biner,"tipe",type(biner))


# bonus
nama = input('masukan nama:')
print("hallo",nama)