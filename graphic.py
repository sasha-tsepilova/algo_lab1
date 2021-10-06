import numpy as np
import json
import matplotlib.pyplot as plt

with open('res.json') as json_file:
    data = json.load(json_file)
    sorts = ["selection_sort", "insertion_sort", "merge_sort", "shell_sort"]

    generators = ["generator_1", "generator_2", "generator_3", "generator_4"]

    for generator in generators:
        x_axe = []
        y_axes = {}
        plt.xlim(left = 2**7, right = 2**15)
        for x in data:
            x_axe.append(int(x))
            for sorting in sorts:
                if sorting in y_axes:
                    y_axes[sorting].append(data[x][generator][sorting]['time'])
                else:
                    y_axes[sorting] = [data[x][generator][sorting]['time']]
        
        for sorting in sorts:
            plt.plot(x_axe, y_axes[sorting])
        
        plt.legend(labels = sorts, loc = 'upper left')
        plt.xscale("log", base = 2)
        plt.yscale("log")
        plt.xlabel('Array length')
        plt.ylabel('Time taken')
        plt.show()
        plt.savefig(generator+'.png')
        
