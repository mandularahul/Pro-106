import csv
import numpy as np
with open('Data4.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][0]
    new_data.append(float(n_num))

new_data1=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data1.append(float(n_num))

r=np.corrcoef(new_data,new_data1)
print(r)
