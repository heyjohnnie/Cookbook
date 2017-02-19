import numpy as np

def arrayFromFile ():
    #Import data from file, sort and flatten the array, then return the array.
    dataFromFile = np.sort(np.genfromtxt("Test.csv", delimiter = ",", dtype = str), axis = None)
    return dataFromFile

def nonGrupedData(data):
    #Find common values and their frequency, create a 2D array
    commonValues = np.unique(data)
    frequency = commonValues.searchsorted(data)
    return commonValues, np.bincount(frequency)

sampleData = arrayFromFile()
sampleSize = sampleData.size
sampleFrequency = nonGrupedData(sampleData)

#The dataTable variable prepares the info before being saved into a CVS file
dataTable = np.transpose(sampleFrequency)
np.savetxt("result.csv", dataTable, delimiter = ",", fmt = "%s")
print ("File saved!")