import numpy as np;
import math;

def builtTransitionMatrix(dist = None, n = 40):

    dist    = [0, 1/18, 1/18, 1/9, 1/9, 1/6, 1/9, 1/9, 1/18, 1/18, 0]
    doubles = [1/36, 0, 1/36, 0, 1/36, 0, 1/36, 0, 1/36, 0, 1/36]

    if n <= 0 : return

    matrix = []

    # Create zero matrix of 3n x 3n 

    for y in range(n * 3): 
        
        row = [0] * (n * 3)

        matrix.append(row)

    # fill matrix cell by cell

    for y in range(n * 3):
        
        for x in range(n * 3):
            
            index = (y - x) % (n)

            prob = 0

            quadY = math.ceil((y + 1) / n) - 1
            quadX = math.ceil((x + 1) / n)

            if index >= 0 and index < len(dist): 
                
                if quadY > 0:

                    if(quadX == quadY): prob = doubles[index]

                else : prob = dist[index]

            matrix[y][x] = prob

    # "go to jail" probability adjustment

    for x in range(n * 3):

        for i in range(3):

            matrix[30 * (i + 1)][x] += matrix[20 * (i + 1)][x]
            matrix[20 * (i + 1)][x] = 0  

        if x >= n * 2: matrix[30][x] +=  1 / 6
            

    # visualise

    sum = np.array([0] * n * 3)

    for y in range(n * 3):

        #print(y,matrix[y])
        sum = sum + np.array(matrix[y])
    

#    print(sum)

    return np.matrix(matrix)


MATRIX = builtTransitionMatrix()
