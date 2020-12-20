import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
import numpy as np
import random
import time

startTime = time.time()

# setting style yang akan dipakai
plt.style.use('fivethirtyeight')

# n = jumlah array
print('Masukkan nilai n (maksimal 100 untuk mengurangi waktu tunggu):')
n = int(input())
a = [i for i in range(1, n+1)]
#random list dishuffle
random.shuffle(a)

# insertion sort
def insertionsort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1

        while(i >= 0 and a[i] > key):
            a[i+1] = a[i]
            i -= 1

            yield a
        a[i+1] = key
        yield a


#objek generator yang direturn berdasarkan fungsinya
generator = insertionsort(a)

# set warna di bar plot
data_normalizer = mp.colors.Normalize()
color_map = mp.colors.LinearSegmentedColormap(
    "my_map",
    {
        "red": [(0, 1.0, 1.0),
                (1.0, .5, .5)],
        "green": [(0, 0.5, 0.5),
                  (1.0, 0, 0)],
        "blue": [(0, 0.50, 0.5),
                 (1.0, 0, 0)]
    }
)

fig, ax = plt.subplots()

#bar container
rects = ax.bar(range(len(a)), a, align="edge",
               color=color_map(data_normalizer(range(n))))

# atur view limit dari x and y axes
ax.set_xlim(0, len(a))
ax.set_ylim(0, int(1.1*len(a)))

text = ax.text(0.01, 1.05, "", transform=ax.transAxes)
text2 = ax.text(0.40, 1.05, "", transform=ax.transAxes)
iteration = [0]

#fungsi animasi bar
def animate(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)

    iteration[0] += 1
    text.set_text("iterations: {}".format(iteration[0]))
    text2.set_text("Tn (sec): {}".format(str(time.time() - startTime), 1, (0, 0, 0)))


anim = FuncAnimation(fig, func=animate,
                     fargs=(rects, iteration), frames=generator, interval=50,
                     repeat=False)

plt.show()
