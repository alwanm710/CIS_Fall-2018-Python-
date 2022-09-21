class Pet:
    def set_NameOfPet(self, Name):  #OOP change value called mutator
        self.__NameOfPet = Name

    def get_NameOfPet(self):	         #OOP get data called accessor 
        return self.__NameOfPet

    def set_TypeOfPet(self, Type):
        self.__TypeOfPet = Type

    def set_AgeOfPet(self, Age):
        self.__AgeOfPet = Age

    def get_TypeOfPet(self):
        return self.__TypeOfPet

    def get_AgeOfPet(self):
        return self.__AgeOfPet
