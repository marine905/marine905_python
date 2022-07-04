import csv
import matplotlib.pyplot as plt
import numpy as np


path = 'D:\Study\Programming\Marine905_git\Python\data.csv'

data = np.genfromtxt(path, delimiter=',', dtype=None, encoding='UTF-8')

print(data)


plt.matshow(data)
plt.colorbar()

plt.show()


#with open(path, newline='') as f:
#    reader = csv.reader(f)
#    data = list(reader)

#data1 = list(map(int, data))
#print(data1)

#fig = plt.figure(figsize=(8,6))
#plt.imshow(data,cmap="inferno")

#plt.show()

