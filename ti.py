
print('Insert first number')
a = int(input())
print('Insert f2nd number')
b = int(input())
if (a == b * b):
    print(f'{a} является квадратом {b}')
elif b == a * a:
    print(f'{b} является квадратом {a}')
else:
    print('Введеные числа не являются кватрами')
