import serial as sr
import csv as csv


# ------------------------------------------------
# Sample variables
# ------------------------------------------------
samples = 120
print_labels = False
line = 0
sensor_data = []
filename = "test.csv"

# ------------------------------------------------
# Connects to the serial port and baud.
# ------------------------------------------------
arduinoData = sr.Serial('COM3', 115200)
arduinoData.close()
arduinoData.open()

# ------------------------------------------------
# Arduino readings
# ------------------------------------------------
while line <= samples:
    read_data = arduinoData.readline()
    data_string = read_data.decode('utf-8')
    data = data_string[0:][:-2]
    readings = data.split(",")
    sensor_data.append(readings)
    line = line+1
    # print(sensor_data)
    #x.append(float(readings[0]))
    #y.append(float(readings[1]))
    #z.append(float(readings[2]))

    # CSV
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(sensor_data)
    f.close()
    

