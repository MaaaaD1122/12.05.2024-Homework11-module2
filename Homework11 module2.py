n = int(input('Введите число на камне: '))
result = []
for i in range(1, n // 2 + 1):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result.append(str(i))
            result.append(str(j))
password = ''.join(result)
print(f'Нужный пароль для выхода: {password}')