import csv
import numpy as np
import matplotlib.pyplot as plt
 
llist = []
klist = []
jlist = []
 
f = open('D:\Study\Programming\Marine905_git\Python\p2pnew.csv', 'r', encoding = 'utf-8')
data = csv.reader(f)
 
for i in data:
   llist.append(i)
 
#print(llist)
 
for j in llist:
   klist.append(list(map(float, j)))
 
#print(klist)
 
jlist = sum(klist, [])
 
#print(jlist)
print(max(jlist))
#plt.hist(jlist, range =(min(jlist), max(jlist)), bins=10)
#cmap = plt.get_cmap('bwr')
plt.nipy_spectral()
plt.matshow(klist)
plt.colorbar(shrink=0.8, aspect=10)
plt.clim(min(jlist), max(jlist))
plt.show()
 
f.close()