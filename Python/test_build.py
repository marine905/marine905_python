import csv
 
data =[]

f = open('D:\-19.5V.csv', 'r', encoding = 'utf-8',)
rdr = csv.reader(f)

for i in rdr:
    data.append(i)

f.close()

llist = []

for j in data:
    for k in j:
        llist.append(float(k))
    
    klist.append(llist)

            
print(klist)
        
        
        
    


