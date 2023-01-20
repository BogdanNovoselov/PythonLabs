import numpy as np

a = np.array(range(10000000), float)
print("Сумма ряда = " + a.sum().__str__())
print("Среднее значение ряда  = " + a.mean().__str__())
a = np.random.choice(range(100), 10000, float)
print (a)
print("Произведение 10000 случайных чисел в диапазоне от 0 до 100 = " + np.median(a).__str__())