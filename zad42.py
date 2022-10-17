l = 1257
rzym = {"t": ["M", "MM", "MMM"], "s": ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        "d": ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        "j": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]}
t = l // 1000
s = (l % 1000) // 100
d = (l % 100) // 10
j = l % 10
wynik = ""
if t != 0:
    wynik += rzym["t"][t - 1]
if s != 0:
    wynik += rzym["s"][s - 1]
if d != 0:
    wynik += rzym["d"][d - 1]
if j != 0:
    wynik += rzym["j"][j - 1]
print(wynik)
