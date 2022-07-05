import csv
 
f = open('D:\-19.5V.csv', 'r', encoding = 'utf-8',)
rdr = csv.reader(f, delimiter= ',')

for line in rdr:
    print(line)

f.close()
