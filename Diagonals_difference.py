import numpy as np

matrix = np.array([ [11,2,4], [4,5,6], [10,8,-12] ])
rows = matrix.shape[0]
columns = matrix.shape[1]

sum1 = 0
sum2 = 0

for i in range(rows):
    for j in range(rows):
        if i==j:
            sum1 += matrix[i][j]
        
        if i== (rows - j - 1):
            sum2 += matrix[i][j]

abs_diff= abs(sum2- sum1)    
print(abs_diff)
