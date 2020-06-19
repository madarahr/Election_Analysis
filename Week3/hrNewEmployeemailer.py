import os
import csv

filePath = os.path.join(' .\Week3\exercises\hrSystem','newEmployee.csv')

fileData = []

with open(file=filepath, newline='') as fileObject: #fileObject is a textIOWrapper
    -fileObject = csv.reader(fileObject,demiliter=',') # _fileObject is a csvObject
    print(_fileObject)
    next(_fileObject)
    #fileData = _fileObject.read()
    for eachRow in _fileObject[1:]:
        fileData.append(eachRow)

    print(fileData)