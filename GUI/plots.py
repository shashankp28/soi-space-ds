import matplotlib.pyplot as plt
import numpy as np


def create_plot(n):
    figl = []
    for i in range(6):
        arr = np.random.normal(1, 1, size=100)
        fig, ax = plt.subplots()
        ax.hist(arr, bins=20)
        figl.append(fig)
    return figl
