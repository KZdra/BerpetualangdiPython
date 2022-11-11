#Casting data
#mengubah bentuk data dari a ke b
#tipe data int,float,double,str,boolean

#Int 
print("=====Interger=====")
data_int = 5 #asli
print("data = ",data_int,"tipe = ",type(data_int)) #data int asli
data_float = float(data_int) # data int --> float
print("data = ",data_float,"tipe = ",type(data_float))
data_str = str(data_int) #data int --> string
print("data = ",data_str,"tipe = ",type(data_str))
data_bool = bool(data_int) #data int --> BOOLean
print("Data = ",data_bool,"tipe = ",type(data_bool))

#Float
print("===Float===")
data_float = 9.6 #mentah
print("data =",data_float,"tipe = ",type(data_float))
data_int = int(data_float) #float --> int
print("data = ",data_int,"tipe = ",type(data_int))
data_str = str(data_float) #float --> string
print("data = ",data_str,"tipe = ",type(data_str))
data_bool = bool(data_float) #float --> bool
print("data = ",data_bool,"tipe = ",type(data_bool))
