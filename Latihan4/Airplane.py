from Vehicle import Vehicle

class Airplane(Vehicle):
    # Constructor
    def __init__(self):
        self.__wingsLength = 0
        self.__longestDistance = 0

    # Get-set WingsLength
    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength

    def getWingsLength(self):
        return self.__wingsLength

    # Get-set LongestDistance
    def setLongestDistance(self, longestDistance):
        self.__longestDistance = longestDistance

    def getLongestDistance(self):
        return self.__longestDistance

    # Method
    def printAirplane(self):
        print("Type                  : " + self.getType())
        print("Age                   : " + str(self.getAge()))
        print("Fuel Type             : " + self.getFuelType())
        print("Max Passengers        : " + str(self.getMaxPassengers()))
        print("Wings Length (m)      : " + str(self.getWingsLength()))
        print("Longest Distance (km) : " + str(self.getLongestDistance()))
        print("========================================")