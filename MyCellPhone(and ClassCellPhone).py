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
     

def main():
     # Create a CellPhone object. The phone
     # variable will reference the object.
     phone = CellPhone( )  # instantiates or creates a new instance or object of CellPhone
                                         # named phone
     # Store values in the object's fields.
     phone.set_manufacturer("Motorola")  #note only one parameter but class has 2 –why?
     phone.set_model_number("M1000")  #self gets parameter of object name
     phone.set_retail_price(199.99)

     # Display the values stored in the fields.
     print('The manufacturer is', phone.get_manufacturer())
     print('The model number is', phone.get_model_number())
     print('The retail price is', phone.get_retail_price())
# Call the main function.
main()  #cool your own class to import
