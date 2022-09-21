class CellPhone:
    def set_manufacturer(self, manufact):  #OOP change value called mutator
        self.__manufacturer = manufact

    def get_manufacturer(self):	         #OOP get data called accessor 
        return self.__manufacturer

    def set_model_number(self, model):
        self.__model_number = model

    def set_retail_price(self, retail):
        self.__retail_price = retail

    def get_model_number(self):
        return self.__model_number

    def get_retail_price(self):
        return self.__retail_price 
