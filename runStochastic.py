import numpy as np;
import matplotlib.pyplot as plt;

from numpy.linalg import matrix_power;

from init.transitionMatrix import MATRIX;
from init.rents            import RENTS, rents;
from init.colors           import colors;
from init.costs            import COSTS;

_positions = [0] * 40 * 3
_positions[0] = 1

POSITIONS = np.row_stack(_positions)

def projectRevenue(n):

    history = []

    total = COSTS / 3

    propertyIndices = np.nonzero(np.array(rents * 3))

    for t in range(n):

        revenue = RENTS * matrix_power(MATRIX,t + 1) * POSITIONS

        temp = total = total + revenue

        summary = total.reshape(-1)

        toArray = summary.tolist()[0]

        filtered = np.array(toArray)[propertyIndices]

        history.append(filtered)

    history = np.matrix(history)

    transposed = np.transpose(history)

    return transposed

def mergeProfit(results):

    results = np.asarray(results)

    length = len(results) // 3

    part1 = results[:length]
    part2 = results[length:2 * length]
    part3 = results[2 * length:]

    merged = part1 + part2 + part3

    brown  = sum(merged[:2])
    skyblue = sum(merged[2:5])
    pink    = sum(merged[5:8])
    orange  = sum(merged[8:11])
    red     = sum(merged[11:14])
    yellow  = sum(merged[14:17])
    green   = sum(merged[17:20])
    blue    = sum(merged[20:22])

    summary = [
        brown,
        skyblue,
        pink,
        orange,
        red,
        yellow,
        green,
        blue
    ]

    return np.matrix(summary)


def plotResults(results):
    
    results = np.asarray(results)

    #print(results)

    turns = np.arange(1,250 + 1)

    index = 0

    for res in results:

        plt.plot(turns,res, color = colors[index])

        index += 1

    plt.show()

results = projectRevenue(250)

results = mergeProfit(results)

plotResults(results)
