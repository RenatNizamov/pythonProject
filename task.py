x = float(input("Введите x: "))
while abs(x) <= 1:
    x = float(input("Вы ошиблись. |x| > 1 должен быть. \nВведите x: "))
n = int(input("Введите n: "))
y = 0
for i in range(0, n):
    y = y + 1 / ((2 * i + 1) * x ** (2 * i + 1))
    #y += 1 / ((2 * i + 1) * x ** (2 * i + 1))
y *= 2
print('Результат: ', y)