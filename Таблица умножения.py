Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> p = int(input('Введите р (2<p,=10): '))
print(f'{p} - ичная таблица умножения')
for i in range(1, p):
    for j in range(1, p):
        z = (i*j//p)*10 + (i*j)%p
        print(z, end = ' ')
    print()