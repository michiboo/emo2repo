import pandas as pd
import numpy as np


width = 48
height = 48
data = pd.read_csv('fer2013.csv')
points = data['pixels'].tolist()

x = []
for i in points:
    temp = [int(x_val) for x_val in i.split(' ')]
    temp = np.asarray(temp).reshape(width, height)
    x.append(temp.astype('float32'))

x = np.asarray(x)
x = np.expand_dims(x, -1)


y = pd.get_dummies(data['emotion']).as_matrix()
np.save('Pixels', x)
np.save('Labels', y)






