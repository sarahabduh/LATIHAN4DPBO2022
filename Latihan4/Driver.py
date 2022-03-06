from Person import Person
from Job import Job

class Driver(Person, Job):
    # Constructor
    def __init__(self):
        self.__licenseID = 0
        self.__activeUntil = ""
        self.__vehicleType = ""
    
    # Get-set LicenseID
    def setLicenseID(self, licenseID):
        self.__licenseID = licenseID

    def getLicenseID(self):
        return self.__licenseID

    # Get-set ActiveUntil
    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def getActiveUntil(self):
        return self.__activeUntil

    # Get-set VehicleType
    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType

    def getVehicleType(self):
        return self.__vehicleType

    # Method
    def printDriver(self):
        print("NIK          : " + str(self.getNIK()))
        print("Name         : " + self.getName())
        print("Gender       : " + self.getGender())
        print("NIP          : " + str(self.getNIP()))
        print("Company Name : " + self.getCompanyName())
        print("Position     : " + self.getPosition())
        print("License ID   : " + str(self.getLicenseID()))
        print("Active Until : " + self.getActiveUntil())
        print("Vehicle Type : " + self.getVehicleType())
        print("========================================")