import numpy
import random
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#  задачка с перемножением массивов:
a = []
b = []
for i in range(1000000):
    a.append(random.randint(-10000, 10001))
    b.append(random.randint(-10000, 10001))
start_time = time.perf_counter()
numpy.multiply(a, b)
print(time.perf_counter() - start_time)

#  Достаю нужные данные из файла: вариант 8
with open('data2.csv') as f:
    header = f.readline().split(',')[3]
    data = [float(x.split(',')[3]) for x in f.readlines()]
data_normalized = [(i - min(data))/(max(data) - min(data)) for i in data]

# Строю гистограммы
fig, ax = plt.subplots(2, 1)

ax[0].set_title('Распределение параметра Chloramines')
ax[0].hist(data, bins=20)
ax[0].bar(numpy.std(data, ddof=1), 1200, width=0.03, color='red')
ax[0].text(1.8, 200, 'Среднеквадратическое отклонение', rotation=90)
ax[0].set_xlabel('Значение параметра')
ax[0].set_ylabel('Кол-во значений на интервале')
ax[0].set_facecolor('seashell')

ax[1].set_title('Нормализованное распределение параметра Chloramines')
ax[1].hist(data_normalized, bins=20, density=True)
ax[1].set_xlabel('Значение параметра')
ax[1].set_ylabel('Кол-во значений на интервале')
ax[1].set_facecolor('seashell')

fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(12)

plt.show()

# Строю трёхмерный график, он отобразится после закрытия окна с гистограммами
x = numpy.linspace(-3*numpy.pi, 3*numpy.pi)
y = numpy.cos(x)
z = x/numpy.sin(x)

fg = plt.figure()
axx = fg.add_subplot(111, projection='3d')
axx.plot(x, y, z, label='parametric curve')
axx.set_xlabel('x')
axx.set_ylabel('y')
axx.set_zlabel('z')

plt.show()
