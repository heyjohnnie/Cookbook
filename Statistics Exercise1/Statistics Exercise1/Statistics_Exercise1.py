
def arrayFromFile ():
    import csv
    import numpy

    READ = "r"
    fileList = []

    #Open file more securely
    with open("Test.csv", READ) as myCSVFile:
        #Create list from file
        rowFromFile = csv.reader(myCSVFile)
        #Merge all values of all rows into a single list
        for row in rowFromFile:
            for value in row:
                fileList.append(value)
                
        #Transform list into an array
        numericData = numpy.array(fileList).astype("float")

    return numericData

firstArray = arrayFromFile()
print (firstArray)