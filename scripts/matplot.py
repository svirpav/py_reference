import matplotlib.pyplot as plt
import math
import numpy as np


class Plot:

    def data_plot(self):
        # self.mul_fig()
        # self.my_subplot()
        # self.__plot_01()
        self.__mul_bar_plot()

    def my_subplot(self):
        y = [3, 10, 0, -9, 12, 45]
        x = ['a', 'b', 'c', 'd', 'e', 'f']
        col = 3
        rows = math.ceil(4 / col)
        print(col, rows)
        fig, axs = plt.subplots(rows, col)
        print(axs)
        axs = self.__trim_axes(axs, 4)
        print(axs)
        for ax in axs:
            ax.plot(x, y)
        plt.show()

    def __trim_axes(self, axs, N):
        axs = axs.flat
        for ax in axs[N:]:
            ax.remove()
        return axs[:N]

    def mul_fig(self):
        fig = plt.figure(1)
        fig.suptitle("Hang")
        gs = fig.add_gridspec(2, 2)
        ax = fig.add_subplot(gs[0, 0])
        ax_2 = fig.add_subplot(gs[0, 1])
        plt.show()

    def __plot_01(self):
        x = [1, 2, 3, 4, 5]
        y = [35, 15, 16, 19]
        if len(x) > len(y):
            y.insert(0, 0)
        plt.plot(x, y)
        plt.show()

    def __mul_bar_plot(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]
        x = np.arange(len(labels))
        width = 0.35
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, men_means, width, label='Men')
        rects2 = ax.bar(x + width/2, women_means, width, label='Women')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        fig.tight_layout()
        plt.show()
