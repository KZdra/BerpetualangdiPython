# a = 1 <--- ini interger

# 1.Interger= bilangan without coma(,)
data_int = 2
print("data ;",data_int)
print("tipe :",type(data_int))

# 2.Float= Bilangan with coma(,) 
data_float = 1.4
print("data:",data_float)
print("tipe:",type(data_float))

# 3.string = teks gitu da teuing teu apal kudu dikasih kutip2("")
data_string = "Hellow,World"
print("data:",data_string)
print("tipe:",type(data_string))

# 4.boolean = True or False 
data_bool = True
print("data:",data_bool)
print("tipe:",type(data_bool))

# Tipe data Khusus anjay buat lu tukang mtk
data_complex = complex(4,6)
print("Data:",data_complex)
print("tipe:",type(data_complex))

# affakah bisa kita pake tipe data di C? bisa dong soalnya based nya c
from ctypes import c_double 
data_double = c_double(12.5)
print("data:",data_double)
print("tipe:",type(data_double))