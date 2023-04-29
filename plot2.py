import numpy as np
import math
import pandas as pd
from matplotlib import pyplot as plt


def show(fsize, color):
    fsize -= 5
    plt.rcParams["figure.figsize"] = (11, 7)
    cl = 'blue'
    if color == 1 or color == 2:
        cl = '#004C83'
    elif color == 3:
        cl = '#EE3168'

    columns = ["scourCriticalBridges", "snowfall", "freezethaw"]
    df = pd.read_csv("nebraska.csv", usecols=columns)

    scourScores = df.scourCriticalBridges.to_list()
    snow = df.snowfall.to_list()

    scourGood = list()
    snowGood = list()

    for i in range(len(scourScores)):
        if str(scourScores[i]).isnumeric():
            if not math.isnan(float(snow[i])):
                scourGood.append(int(scourScores[i]))
                snowGood.append(float(snow[i]))

    scores = [list(), list(), list(), list(), list(), list(), list(), list(), list(), list()]

    averages = list()
    count = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(len(snowGood)):
        scores[scourGood[i]].append(snowGood[i])

    for i in range(10):
        scores[i].sort()
        averages.append((scores[i][0] + scores[i][-1] + scores[i][len(scores[i]) // 2]) / 3.0)

    plt.scatter(count, averages, color=cl)

    m = np.poly1d(np.polyfit(count, averages, 1))
    eqn = np.array(m)
    label = "y = " + str((int(eqn[0] * 1000)) / 1000) + " x + " + str((int(eqn[1] * 1000)) / 1000)

    plt.plot(count, np.poly1d(np.polyfit(count, averages, 1))(count), label=label, color=cl)
    plt.legend(loc='lower right', fontsize=fsize)


    plt.xticks(fontsize=fsize-2)
    plt.yticks(fontsize=fsize-2)
    plt.xlabel("Scour Critical Values", fontsize=fsize)
    plt.ylabel("Average Snowfall Amounts", fontsize=fsize)
    plt.title('Correlation between Snowfall and Scour Scores', fontsize=fsize+2)
    plt.savefig("figure.png")
    plt.show()
