from CellPhoneClass import CellPhone
def main():
     # Create a CellPhone object. The phone
     # variable will reference the object.
     phone = CellPhone()  #Python constuctor can't take multiple parms like book
     
     # Store values in the object's fields.
     phone.set_manufacturer("Motorola")
     phone.set_model_number("M1000")
     phone.set_retail_price(199.99)

     # Display the values stored in the fields.
     print('The manufacturer is', phone.get_manufacturer())
     print('The model number is', phone.get_model_number())
     print('The retail price is', phone.get_retail_price())

# Call the main function.
main()
