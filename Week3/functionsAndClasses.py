

someListOfInts = [55,22,11,33,44,10,93]

def calculateMean(someList) -> float:
        summator = 0
        for number in someList:
            summator = summator + number
        return summator/len(someList)

print(calculateMean(someListOfInts))


# Classes - are objects that have attributes and methos associated with its definitions

class Animal():

    def __init__(self, animalType):
        self.animalType = animalType

    def printAnimalType(self):
        print(self.animalType)


parrot = Animal("Parrot")
parrot.printAnimalType()

dog = Animal("Dog")
dog.printAnimalType()


class Mammal(Animal):

    def __init__(self, animalType: str, hasFur: bool) -> None:
        self.animalType = animalType
        self.hasFur = hasFur

    def isAFurryMammal(self):
        if self.hasFur:
            print("Furry Mammal")
        else:
            print("Hairless")

sphinxCat = Mammal(hasFur= False,animalType = "not furry cat")
print(sphinxCat.animalType)
print(sphinxCat.hasFur)
sphinxCat.isAFurryMammal()
