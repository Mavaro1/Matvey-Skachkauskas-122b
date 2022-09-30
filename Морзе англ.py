a='abwgdevzijklmnoprstufhcqx'
abc=list(a)
print(abc)
b='.- -... .-- -.. . ...- --.. .. .--- -.- .-..  -- -. --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-'
abcm = b.split()
indm=str()
print(abcm)
tekst=input("Введите текстдля перевода в морзянку(агл.алфавит)")
for i in range (len (tekst)):
    ind = abc.index(tekst[i])
    indm = indm+abcm[ind]+' '
print(f"Морзянка = {indm}")


