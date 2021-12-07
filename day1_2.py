import numpy as np
import pandas as pd
import os

os.chdir('/Users/jehlokhande/Documents/adventofcode2021')
print(os.getcwd())

input = pd.read_csv('day1_1.txt', header = None)
test_input= pd.DataFrame([199,200,208,210,200,207,240,269,260,263])

input_sum = input + input.shift(1) + input.shift(2)

counter = 0
for i in range(0, len(input_sum)):
    if input_sum.iloc[i][0] > input_sum.iloc[i-1][0]:
        counter+=1

print(counter)
