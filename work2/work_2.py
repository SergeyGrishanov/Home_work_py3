#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X 
import random

num = []

n = int(input("Введите количество элементов в массиве: "))

for i in range(n):
    
    num.append(random.randrange(n))
print(num)
mass = list(map(int, num))

x = int(input("Введите искомое число: "))

min = abs(x - num[0])
index = 0
for i in range(1, n):
    count = abs(x - num[i])
    if count < min:
        min = count
        index = i
print(f'Число {num[index]} в списке A наиболее близко по величине к числу {x}')