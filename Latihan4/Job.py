class Job:
    # Constructor
    def __init__(self):
        self.__NIP = 0
        self.__companyName = ""
        self.__position = ""
    
    # Get-set NIP
    def setNIP(self, NIP):
        self.__NIP = NIP

    def getNIP(self):
        return self.__NIP

    # Get-set Company Name
    def setCompanyName(self, companyName):
        self.__companyName = companyName

    def getCompanyName(self):
        return self.__companyName

    # Get-set Position
    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    # Method
    def printJob(self):
        print("NIP          : " + str(self.getNIP()))
        print("Company Name : " + self.getCompanyName())
        print("Position     : " + self.getPosition())
        print("========================================")