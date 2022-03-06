class Person:
    # Constructor
    def __init__(self):
        self.__NIK = 0
        self.__name = ""
        self.__gender = ""
    
    # Get-set NIK
    def setNIK(self, NIK):
        self.__NIK = NIK

    def getNIK(self):
        return self.__NIK

    # Get-set Name
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    # Get-set Gender
    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender
    
    #Methods
    def sleep(self):
        print(self.getName() + " is currently sleeping.")
    
    def printPerson(self):
        print("NIK      : " + str(self.getNIK()))
        print("Name     : " + self.getName())
        print("Gender   : " + self.getGender())
        self.sleep()
        print("========================================")