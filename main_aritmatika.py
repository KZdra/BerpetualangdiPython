#operasi aritmatika di python

#tempat variable angka

a = 10
b = 2

#penjumblahan +

hasil = a + b
print(a,'+',b,'=',hasil)

#pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

#pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

#perkalian  *
hasil = a * b 
print(a,'*',b,'=',hasil)

#eksponen/pangkat **
hasil = a ** b 
print(a,'**',b,'=',hasil)

#modulus %
hasil = a % b
print(a,'%',b,'=',hasil)

#florr division //
hasil = a // b
print(a,"//",b,'=',hasil)

#prioritas operasi, operation predence
'''
1. ()
2. exponen **
3. perkalian dan teman-teman * / ** % //
4.pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

#kurung akan mengambil langkah pertama
hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)
