import serial as sr
import matplotlib.pyplot as plt
import csv as csv
import time as ts

filename = "test.csv"

# Samples
samples = 10
print_labels = False
line = 0
sensor_data = []
print(sensor_data)

# Variables for plotting
plt.ion()

# Pop up with graph
# fig = plt.figure()
i = 0
x = list()
y = list()

# Connects to the serial port and baud
arduinoData = sr.Serial('COM3', 115200)
arduinoData.close()
arduinoData.open()

# Continous plotting
# Readings
while line <= samples:
    read_data = arduinoData.readline()
    data_string = read_data.decode('utf-8')
    data = data_string[0:][:-2]
    readings = data.split(",")

    sensor_data.append(readings)
    #print(sensor_data)
    #print(sensor_data[0][0]) #Possibility for individual values
    line = line+1

    # Log variables
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(sensor_data)
    f.close()    

    #plt.scatter(i, float(data.decode()))
    #i += 1
    # plt.show()
    # plt.pause(0.1)


# TODO show live plotting for ten seconds and then reset
# TODO calculate offset
# TODO log all data into a csv file --> DONE
