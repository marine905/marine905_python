import csv
import matplotlib.pyplot as plt
import numpy as np
 

path = 'D:\Study\Programming\Marine905_git\Python\twenty.csv'

data1 = np.genfromtxt(path, delimiter=',', dtype=None, encoding='UTF-8')

print(data1)
cmap = plt.get_cmap('bwr')


plt.matshow(data1, cmap=cmap)
plt.clim(0, 0.5)
plt.colorbar(shrink=0.8, aspect=10)




plt.show()


#with open(path, newline='') as f:
#    reader = csv.reader(f)
#    data = list(reader)

#data1 = list(map(int, data))
#print(data1)

#fig = plt.figure(figsize=(8,6))
#plt.imshow(data,cmap="inferno")

#plt.show()

