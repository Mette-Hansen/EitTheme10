import serial as sr
import matplotlib.pyplot as plt
import csv as csv

filename = "test.csv"

# Variables for plotting
# plt.ion()
#fig = plt.figure()
i = 0
x = list()
y = list()

# Connects to the serial port and baud
arduinoData = sr.Serial('COM3', 115200)
arduinoData.close()
arduinoData.open()
# Continous plotting
while True:
    data = arduinoData.readline()
    print(data.decode())
    x.append(i)
    y.append(data.decode)

    # Log variables
    fields = ['X', 'Y', 'Z']
    rows = [data.decode()]
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, dialect='excel')
        csvwriter.writerow(fields)
        csvwriter.writerow(rows)

    #plt.scatter(i, float(data.decode()))
    #i += 1
    # plt.show()
    # plt.pause(0.1)


# TODO show live plotting for ten seconds and then reset
# TODO calculate offset
# TODO log all data into a csv file
