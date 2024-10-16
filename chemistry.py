from sympy import solve, Symbol, roots
znachenia_is_sbornika = {
"Al" : [[3, 78.0036, 1, -32]],
"Bi" : [[3, 260.0024, 3.16, -32]],
"Ca" : [[2, 74.09, 5.5, -6]],
"Cd" : [[2, 146.41, [2.2, -14], [5.9, -15]]], 
"Co" : [[2, 92.947875, [1.6, -15], [2, -16]]], 
"Cr" : [[3, 103.018, 6.3, -31]],
"Cu" : [[2, 97.55, 2.2, -20]],
"Fe" : [[2, 89.86, 8, -16 ], [3, 106.869, [6.3, -38], [6.3, -39]]], 
"Ga" : [[3, 120.74, 1.6, -37]],
"Mg" : [[2, 58.327, [6, -10], [7.1, -12]]],
"Mn" : [[2, 88.9528, 1.9, -13]],
"Ni" : [[2, 92.70808, [2, -15], [6.3, -18]]], 
"Pb" : [[2, 241.2, [5, -16], [7.3, -16]]], 
"Sc" : [[3, 95.98, 2, -30]],
"Sn" : [[2, 152.7247, 6.3, -27]],
"Sr" : [[2, 121.63, 3.2, -4]],
"Ti" : [[2, 81.88], [3, 98.8907]], #???
"Zn" : [[2, 99.38, 1.2, -17]]
 
}
 
def gramotey(slovo):
    if slovo == slovo.capitalize():
        return "0"
    else:
        return f"Вы имели ввиду {slovo.capitalize()}?"
 
flag = 0
flag2 = 0
el = input("Введите символ химического элемента: ").strip()
while flag2 == 0:
    if gramotey(el) == "0": 
        if el in znachenia_is_sbornika:
            flag2 = 1
        else:
            print('Введены некорректные данные. Повторите попытку.')
            el = input("Введите символ химического элемента: ")
    else:
      flag3 = 0
      while flag3 != 1:
        if el.capitalize() in znachenia_is_sbornika:
            print(gramotey(el))
            print("Выберите подходящий вариант ответа (введите цифру):", "1. Да", "2. Нет", sep="\n")
            otvet = int(input())
            flag2 = 1
            if otvet == 2:
                print("Повторите попытку.")
                el = input("Введите символ химического элемента: ").strip()
            else:
              flag3 = 1
        else:
            print('Введены некорректные данные. Повторите попытку.')
            el = input("Введите символ химического элемента: ").strip()
el = el.capitalize() 
n = float(input("Введите валентность элемента: "))
while flag == 0:
    for j in range(len(znachenia_is_sbornika[el.capitalize()])):
        if n == znachenia_is_sbornika[el.capitalize()][j][0]:
            flag = 1
            break
    if flag == 0:
        print('Введена некорректные данные. Повторите попытку.')
        n = float(input("Введите валентность элемента: "))
 
K1 = 0 #это константа, которую мы считаем по формуле из 3 и 4 ключа словаря
K2 = (1.76 * (10  (-5)))  n # это вторая константа. Она всегда постоянна
 
M = znachenia_is_sbornika[el][j][1]
 
if type(znachenia_is_sbornika[el][j][2]) == list:
    print("Выберите нужный Вам вариант константы диссоциации (введите цифру):")
    for i in range(2, len(znachenia_is_sbornika[el][j])):
        opuy = znachenia_is_sbornika[el][j][i][0] * (10 ** (znachenia_is_sbornika[el][j][i][1]))
        print(i - 1, ". ", opuy, sep='')
    otvet2 = int(input()) + 1
    K1 = znachenia_is_sbornika[el][j][otvet2][0] * (10 ** (znachenia_is_sbornika[el][j][otvet2][1]))
else:
    K1 = znachenia_is_sbornika[el][j][2] * (10  (znachenia_is_sbornika[el][j][3])) # это формула a * 10  b
z = K1 / K2
 
C = float(input("Введите концентрацию: "))
a = float(input("Введите массу осадка в граммах: "))
print("\n")
 
ans = []
if n == 3:
    a1 = float(C **3)
    b1 = float((-1 * (C **2) * 3 * a * 3) / M)
    c1 = float((3*C*(a2) * 9) / (M  2))
    d1 = float((-1 * (a  3) * 27) / (M  3))
    f1 = float((-1 * 27 * (a  4)) / ((M  4) * z))
    x = Symbol('x')
    ans = solve(a1 * x  4 + b1 * x  3 + c1 * x ** 2 + d1 * x + f1, x)
else:
    x = Symbol('x')
    a1 = float(C ** 2)
    b1 = float((-1 * 2 * a * C * 2)/ M)c1 = float((a  2) * 4 / (M  2))
    d1 = float((-1 * (4*(a3))) / ((M3) * z))
    ans = solve(a1 * x  3 + b1 * x  2 + c1 * x + d1, x)
ans_1 = []
for i in ans:
    if "I" not in str(i):
        ans_1.append(i)
    elif "0.e" in str(i):
            for x in range(len(str(i))):
                if (str(i)[x] == "+" and str(i)[x + 1] == " ") or (str(i)[x] == "-" and str(i)[x + 1] == " "):
                    r = x - 1
                    f = float(str(i)[0: r])
                    ans_1.append(f)
ans_2 = []              
for y in ans_1:
    if y > 0 and 3 * y > 5.4:
        ans_2.append(y)
if len(ans_2) > 0:
    print(*ans_2, end="")
    print(" л.")
else:
    print("Адекватного решения не существует.")