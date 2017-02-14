import numpy as np

def arrayFromFile ():
    #Import data from file, sort and flatten the array, then return the array.
    dataFromFile = np.sort(np.genfromtxt("Test.csv", delimiter = ","), axis = None)
    return dataFromFile

def nonGrupedData(data):
    #Find common values and their frequency, create a 2D array
    commonValues = np.unique(data)
    frequency = commonValues.searchsorted(data)
    return commonValues, np.bincount(frequency)


sampleData = arrayFromFile()
sampleSize = sampleData.size

#The traspose method switches rows into columns.
sampleFrequency = np.transpose(nonGrupedData(sampleData))
np.savetxt("result.csv", sampleFrequency, delimiter = ",", fmt = "%10.5f")
print ("File saved!")