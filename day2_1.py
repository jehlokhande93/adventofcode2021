import numpy as np
import pandas as pd
import os

os.chdir('/Users/jehlokhande/Documents/adventofcode2021')
print(os.getcwd())

input = pd.read_csv('day2_2.txt', header = None, delimiter=' ')
input.columns = ['direction', 'units']
# test_input= pd.DataFrame([199,200,208,210,200,207,240,269,260,263])

#change down to negative up

input['units'] = input.apply(lambda x: -x['units'] if x['direction'] == 'up' else x['units'], axis = 1)
input['direction'] = input['direction'].apply(lambda x: 'down' if x == 'up' else x)

print(np.sum(input.query('direction == "down"')['units'])*np.sum(input.query('direction == "forward"')['units']))
