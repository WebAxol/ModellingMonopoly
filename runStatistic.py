import numpy as np;
import matplotlib.pyplot as plt;
from init.rents import rents, colors;
from random import randrange;
from init.costs import COSTS;

rolls = 250
trials = 10

def iterateNTurns(n):

    history = []

    doubles = 0

    temp = COSTS.copy()

    total = np.asanyarray(temp.reshape(-1))
    
    propertyIndices = np.nonzero(np.array(rents))

    position = 0
    
    for i in range(n):

        numA = randrange(5)
        numB = randrange(5)

        diceSum = 2 + numA + numB

        position = (position + diceSum) % 40

        if numA == numB:
            doubles += 1
        else:
            doubles = 0

        if doubles >= 3:
            position = 30
            doubles = 0

        if(position == 20):
            position = 30


        total[position] += rents[position]

        history.append(total.tolist())
    
    matrix = np.matrix(history)

    transpose = np.transpose(matrix)

    filteredProperties = np.asarray(transpose)[propertyIndices]

    return np.matrix(filteredProperties)


def mergeProfit(results):

    results = np.asarray(results)

    brown   = sum(results[:2])
    skyblue = sum(results[2:5])
    pink    = sum(results[5:8])
    orange  = sum(results[8:11])
    red     = sum(results[11:14])
    yellow  = sum(results[14:17])
    green   = sum(results[17:20])
    blue    = sum(results[20:22])

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

    turns = np.arange(1,rolls + 1)

    index = 0

    for res in results:

        plt.plot(turns,res, color = colors[index])

        index += 1

    plt.xlabel('Dice rolls')
    plt.ylabel('Expected profit')
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    plt.title("Mean profit observed after simulating " + str(trials) + " trials of " + str(rolls) + " dice rolls")

    plt.show()

    #print(turns)


def makeMean(rollsPerTrial,trials):

    result = iterateNTurns(rollsPerTrial)

    for i in range(trials - 1):

        amount = iterateNTurns(rollsPerTrial)

        result = result + amount

    mean = (result / trials)

    return mean


results = makeMean(rolls,trials)

results = mergeProfit(results)

plotResults(results)
