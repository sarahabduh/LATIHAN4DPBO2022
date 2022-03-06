from Vehicle import Vehicle

class Ship(Vehicle):
    # Constructor
    def __init__(self):
        self.__name = ""
        self.__countryOfManufacture = ""

    # Get-set Name
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    # Get-set CountryOfManufacture
    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture

    def getCountryOfManufacture(self):
        return self.__countryOfManufacture

    # Method
    def printShip(self):
        print("Name                  : " + str(self.getName()))
        print("Type                  : " + self.getType())
        print("Age                   : " + str(self.getAge()))
        print("Fuel Type             : " + self.getFuelType())
        print("Max Passengers        : " + str(self.getMaxPassengers()))
        print("County of Manufacture : " + self.getCountryOfManufacture())
        print("========================================")