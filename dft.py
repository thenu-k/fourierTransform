# This programme calculate and visualizes the DFT of a set of frequencies. 
import math 
import matplotlib.pyplot as plt
import csv 
import numpy as np

#Importing csv data
samples = []
with open("input.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for value in reader:
        samples.append(value)
samples = samples[0] #Make sure that all the data in the csv is in the same row
numSamples = len(samples)
samplingRate = len(samples)

# Calculating the real coefficients
outerCount = 0
realSums = []
k = 0
while(outerCount < numSamples):
    #For Each k
    realSum = 0
    innerCount = 0
    while(innerCount<numSamples):
        realSum += samples[innerCount] * math.cos((2 * math.pi * innerCount * k)/numSamples)
        innerCount += 1
    realSums.append(realSum)
    k += 1
    outerCount += 1

# Calculating the imaginary coefficients
outerCount = 0
imaginarySums = []
k = 0
while(outerCount < numSamples):
    #For Each k
    imaginarySum = 0
    innerCount = 0
    while(innerCount<numSamples):
        imaginarySum +=  -samples[innerCount] * math.sin((2 * math.pi * innerCount * k)/numSamples)
        innerCount += 1
    imaginarySums.append(imaginarySum)
    k += 1
    outerCount += 1

#Extracting Amplitude Information
ampCount = 0
amplitudes = []
while(ampCount<numSamples/2+1):
    amplitudes.append((math.pow(  (math.pow(realSums[ampCount], 2) + math.pow(imaginarySums[ampCount], 2))  ,0.5))/numSamples  )
    ampCount+= 1

#Setting the x axis for the transform and the normal graph
frequencyResolution = samplingRate / numSamples
xAxisTransform = []
axisSum = 0
axisCount = 0
while(axisCount< numSamples/2 +1):
    xAxisTransform.append(axisSum)
    axisSum += frequencyResolution
    axisCount += 1 

xAxisInit = []
axisSum = 0
axisCount = 0
resolution = 1/samplingRate
while(axisCount< numSamples):
    xAxisInit.append((axisSum))
    axisSum += resolution
    axisCount+= 1


# Visualisation
# f1 = plt.figure(1)
# plt.plot(xAxisTransform, amplitudes, marker='o')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# f2 = plt.figure(2)
# plt.plot(xAxisInit, samples, marker='x')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.show()

fig, axis = plt.subplots(2)
axis[0].plot(xAxisInit, samples, marker='o')
axis[0].set_ylabel('Amplitude')
axis[0].set_xlabel('Time')
axis[1].plot(xAxisTransform, amplitudes, marker='o')
axis[1].set_ylabel('Magnitude')
axis[1].set_xlabel('Frequency')
plt.show()