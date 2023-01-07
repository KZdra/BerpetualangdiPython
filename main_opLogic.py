#operasi logika atau boolean

# not ,or ,and ,xor

#Not  (Bukan a ya berarti false dong)
print('=========NOT===========')
a = True
s = not a
print('data a =',a)
print('-------NOT-------')
print('not a = ',s)

#OR (Berarti kalo ada true 1 berarti tru kaya +1 kalo true +0 kalo false so kalo tru sama tru berarti true karena 1+1=2>1=true kalo true sama false jadinya true soalnya 1+0=1=true)
print('=========OR===========')
k = False
n = False
t = k or n
print(k,'OR',n,'=',t)
k = True
n = False
t = k or n
print(k,'OR',n,'=',t)
k = False
n = True
t = k or n
print(k,'OR',n,'=',t)
k = True
n = True
t = k or n
print(k,'OR',n,'=',t)

#AND (SECARA SINGKAT NYA INI TUH HARUS ADA YANG SAMA KAYAKNYA KALO BEDA 1 YASUDAH FALSE kayak di kaliin)
print('=========AND===========')
k = False
n = False
t = k and n
print(k,'AND',n,'=',t)
k = True
n = False
t = k and n
print(k,'AND',n,'=',t)
k = False
n = True
t = k and n
print(k,'AND',n,'=',t)
k = True
n = True
t = k and n
print(k,'AND',n,'=',t)

#XOR <^> (KALO SEBANDING 1:1 = FALSE KALO BEDA(1:0) YA TRUE true jika salah satu true ngertikan mksd gweh? T_T)
print('=========XOR===========')
k = False
n = False
t = k ^ n
print(k,'XOR',n,'=',t)
k = True
n = False
t = k ^ n
print(k,'XOR',n,'=',t)
k = False
n = True
t = k ^ n
print(k,'XOR',n,'=',t)
k = True
n = True
t = k ^ n
print(k,'XOR',n,'=',t)
