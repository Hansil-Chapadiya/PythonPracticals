MyDict = {
    "Fast" : "Quickly",
    "Hansil" : "A software Developer",
    "produce" : "generate",
    "Marks" : "[1,2,3,4]",
    "anotherDict" : {"pick" : "elect"},
}
print(MyDict['Fast'])
print(MyDict["Hansil"])
print(MyDict["Marks"])
print(MyDict["anotherDict"]["pick"])

#Dictonary Methods

print(list(MyDict.keys()))
print(MyDict.values())
print(MyDict.items())

updateDict = {

    "Advance" : "a work before",
    "battle" : "a war",
}
#MyDict.update(updateDict)
#print(MyDict)

print(MyDict.get("Hansil"))#print value assosiated with key "Hansil"
print(MyDict["Hansil"])#print value assosiated with key "Hansil"

#The Difference Between .get and [] is below

print(MyDict.get("hansil1"))#return none for "hansil1" which non present in dict.
print(MyDict["hansil1"])#throw error for "hansil1" which is non present in dict.