class Car:
    #Set yearModel, make, and speed
    def set_YearModel(self, yearModel):
        self.__YearModel = yearModel
    def set_MakeOfCar(self, Make):
        self.__MakeOfCar = Make
    def set_SpeedOfCar(self, Speed):
        self.__SpeedOfCar = Speed

    #Program for Constructor, Accessors, Accelerate, and Brake
    def __init__(self, yearModel, Make):
        self.__SpeedOfCar = 0
        self.__MakeOfCar = Make
        self.__YearModel = yearModel
    def Accelerate(self):
        self.__SpeedOfCar = self.__SpeedOfCar + 5
    def Brake(self):
        self.__SpeedOfCar = self.__SpeedOfCar - 5

    #Get yearModel, make, and speed
    def get_SpeedOfCar(self):
        return self.__SpeedOfCar
    def get_MakeOfCar(self):
        return self.__MakeOfCar
    def get_YearModel(self):
        return self.__YearModel
    

    
#main
myCar = Car(1998, "JEEP")
for index in range(0,5):
    myCar.Accelerate()
    print(myCar.get_SpeedOfCar())
for index in range(0,5):
    myCar.Brake()
    print(myCar.get_SpeedOfCar())
print(myCar.get_MakeOfCar())
print(myCar.get_YearModel())

