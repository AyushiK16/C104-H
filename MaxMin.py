import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
currentMax = 0
currentMin = 0


for i in range(len(file_data)):
    #Finding the maximun weight.
    if currentMax > float(file_data[i][2]):
        currentMax = currentMax
    else: 
        currentMax = float(file_data[i][2])
    
    #Initiating the variable currentMin with some value (the first one)
    if i == 1:
        currentMin = float(file_data[i][2])

    #Finding the minimun weight
    if currentMin < float(file_data[i][2]):
        currentMin = currentMin
    else:
        currentMin = float(file_data[i][2])

print('Maximum Weight =', currentMax)
print('Minimum Weight = ', currentMin)

