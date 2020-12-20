import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mp
import numpy as np
import random
import time

startTime = time.time()

def mergesort(A, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1

    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)

# function untuk merge random array
def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i in range(len(merged)):
        A[start + i] = merged[i]
        yield A

# fungsi untuk plot bar
def showGraph():
# n = jumlah array
    print('Masukkan nilai n (maksimal 100 untuk mengurangi waktu tunggu):')
    n = int(input())
    a = [i for i in range(1, n+1)]
    #random arry
    random.shuffle(a)
    datasetName = 'Random'

    # objek generator yang direturn berdasarkan fungsinya
    generator = mergesort(a, 0, len(a)-1)
    algoName = 'Merge Sort'

    # setting style yang akan dipakai
    plt.style.use('fivethirtyeight')

    # set warna bar
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

    # bar container
    bar_rects = ax.bar(range(len(a)), a, align="edge",
                       color=color_map(data_normalizer(range(n))))

    # atur view limit dari x and y axes
    ax.set_xlim(0, len(a))
    ax.set_ylim(0, int(1.1*len(a)))

    text = ax.text(0.01, 1.05, "", transform=ax.transAxes, color="#E4365D")
    text2 = ax.text(0.40, 1.05, "", transform=ax.transAxes, color="#E4365D")
    iteration = [0]

    def animate(A, rects, iteration):
        for rect, val in zip(rects, A):

            rect.set_height(val)
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))
        text2.set_text("Tn (sec): {}".format(
            str(time.time() - startTime), 1, (0, 0, 0)))

    # panggil fungsi animate secara berulang
    anim = FuncAnimation(fig, func=animate,
                         fargs=(
                             bar_rects, iteration), frames=generator, interval=50,
                         repeat=False)
    plt.show()
showGraph()
