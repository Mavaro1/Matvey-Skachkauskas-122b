Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> N10 = int(input('Введите исходное 10-тичное число: '))
p = 1
while ((p<2) or (p>9)):
    p = int(input('Введите основание системы счисления в диапазоне [2; 9]: '))
k = int(1)
Np = int(0)
while not (N10 == 0):
    Np = Np + (N10 % p)*k
    k = k*10
    N10 = N10 // p
print('N' + str(p) + ' = ' + str(Np))