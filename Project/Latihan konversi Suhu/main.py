#Latihann

#PROGRAM KONVERSI SUHU
print("\nProgram Konversi Suhu\n")

#CELCIUS
celcius = float(input('masukan suhu dalam celcius :'))
print("suhu dalam celcius adalah :",celcius,"Celcius")

#Celcius ----> reamur
reamur = (4/5) * celcius
print('suhu dalam reamur adalah:',reamur,'Reamur')

#Celciius ---> fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit:",fahrenheit,"Fahrenheit")

#Celcius ----> Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin:",kelvin,"Kelvin")

#New Line = PR
print("\nKonversi suhu ke K dan F\n")
fahrenheit = float(input('Masukan Suhu dalam Fahrenheit:'))
print('suhu dalam F :',fahrenheit)

#fahrenheit to kelvin
kelvin = (5/9)* (fahrenheit - 32) + 273
print('suhu dalam K:',kelvin,'K')

#kelvin -- fahrenheit
kelvin = float(input('\nmasukan suhu dalam K:'))
print('suhu dalam kelvin:',kelvin,'K')

fahrenheit = (9/5) * (kelvin - 273) + 32
print('suhu dalam fahrenheit = ',fahrenheit,'F')