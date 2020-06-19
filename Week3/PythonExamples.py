# Variables

exampleString = "Hello World"
exampleString2 = 'Hello World'
exampleString3 = "Hello, Shawn O' Conner"
exampleString4 = "Hello, Shawn O'Conner"

print (exampleString)
print(type(exampleString))


print(type(7))
print(type(7.0))
print(type('7.0'))

#Python Booleans are True and False
print(type(True))
print(type(False))


print(type(None))


myName = "Rahul Madarapu"
myAgeThatIWantToBe = 46
myBirthDay = '06/18/1974'

myIntroduction = f"""
Hello, my name is {myName} and I am {myAgeThatIWantToBe}.  I was born on {myBirthDay}.
""" # String Interpolation

print(myIntroduction)

# Lists

ListOfDifferentType = [0,1.0,"SomeString",[0,2,3,[exampleString,exampleString2]]]
print(ListOfDifferentType)

someListOfIntegers = [9,8,7,6,5,4,3,2,1,0]

print(someListOfIntegers[0]) #9
print(someListOfIntegers[3]) #6
#someListOfIntegers[11] #OutOfRange

print(len(someListOfIntegers))
print(exampleString[0])
print(type(exampleString[0]))

for theInteger in someListOfIntegers:
    print(theInteger)

for theCharacter in exampleString:
        print(theCharacter)

someListOfIntegers.remove(5)

for theInteger in someListOfIntegers:
    print(theInteger)

if 6 in someListOfIntegers:
    print(True)


if "H" in exampleString or "P" in exampleString:
    print(True)

# A is the statement == "H" in exampleString
# B is the statement == "P" in exampleString

## Truth Table for Or
# A B Q
#T T T
#T F T
#F T T
#F F F

## Truth Table for And
# A B Q
# T T T
# T F F
# F T F
# F F F

## XOR, Not, NAND
