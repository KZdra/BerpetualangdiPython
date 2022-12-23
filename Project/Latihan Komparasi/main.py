#Latihan komparasi

#hasil pasti boolean True or False!
# >,<,>=,<=,==,!=, (is , is not)-(Khusus Object Identity)

a = 4
b = 2

#Lebih besar >
print('===============Lebih besar dari (>)')
hasil = a > 3 
print(a ,'>','3','=',hasil)
hasil = b > a
print(a,'>',b,'=',hasil)
hasil = b > 2
print(a,'>',b,'=',hasil)

#Lebih kecil <
print('=================Lebih kecil (<)')
hasil = a < 3
print(a,'<','3','=',hasil)
hasil = b < 4
print(b,'<','4','=',hasil)
hasil = b < 2
print(b,'<','2','=',hasil)

# lebih besar samadengan >=
print('===============lebih besar samadengan (>=)')
hasil = a >= 3
print(a,'>=','3','=',hasil)
hasil = b >= 4
print(b,'>=','4','=',hasil)
hasil = b >= 2
print(b,'>=','2','=',hasil)

# lebih kecil samadengan <=
print('===============lebih kecil samadengan (<=)')
hasil = a <= 3
print(a,'<=','3','=',hasil)
hasil = b <= 4
print(b,'<=','4','=',hasil)
hasil = b <= 2
print(b,'<=','2','=',hasil)

# samadengan ==
print('=============== samadengan (==)')
hasil = a == 3
print(a,'==','3','=',hasil)
hasil = b == 4
print(b,'==','4','=',hasil)
hasil = b == 2
print(b,'==','2','=',hasil)

# tidak samadengan !=
print('===============tidak samadengan (!=)')
hasil = a != 3
print(a,'!=','3','=',hasil)
hasil = b != 4
print(b,'!=','4','=',hasil)
hasil = b != 2
print(b,'!=','2','=',hasil)

# object identity = is , is not
print('================OI Is Isnot')
a = 5
b = 5
print(a,'=',hex(id(a)))
print(b,'=',hex(id(b)))
hasil = a is b 
print('a is b = ',hasil)

#is not 
print('================OI Isnot')
a = 6
b = 5
print(a,'=',hex(id(a)))
print(b,'=',hex(id(b)))
hasil = a is not b 
print('a is not b = ',hasil)