class Vehicle:
    # Constructor
    def __init__(self):
        self.__fuelType = ""
        self.__maxPassengers = 0
        self.__age = 0
        self.__type = ""
        self.__speed = 0
    
    # Get-set FuelType
    def setFuelType(self, fuelType):
        self.__fuelType = fuelType

    def getFuelType(self):
        return self.__fuelType

    # Get-set MaxPassengers
    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers

    def getMaxPassengers(self):
        return self.__maxPassengers

    # Get-set Type
    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    # Get-set Age
    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    # Get-set Speed
    def setSpeed(self, speed):
        self.__speed = speed

    def getSpeed(self):
        return self.__speed

    # Methods
    def move(self):
        print("This vehicle is moving at " + str(self.getSpeed()) + " km/h.")

    def printVehicle(self):
        print("Type            : " + self.getType())
        print("Age             : " + str(self.getAge()))
        print("Fuel Type       : " + self.getFuelType())
        print("Max Passengers  : " + str(self.getMaxPassengers()))
        self.move()
        print("========================================")