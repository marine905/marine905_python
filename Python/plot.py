import csv
import matplotlib.pyplot as plt
import numpy as np


path = 'D:\Study\Programming\Marine905_git\Python\data.csv'

data = np.genfromtxt(path, delimiter=',', dtype=None, encoding='UTF-8')

print(data)
cmap = plt.get_cmap('bwr')

plt.matshow(data, cmap=cmap)
plt.colorbar()
plt.clim(0, 40)

plt.show()


#with open(path, newline='') as f:
#    reader = csv.reader(f)
#    data = list(reader)

#data1 = list(map(int, data))
#print(data1)

#fig = plt.figure(figsize=(8,6))
#plt.imshow(data,cmap="inferno")

#plt.show()

