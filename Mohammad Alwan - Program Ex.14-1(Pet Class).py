from PetClass import Pet
def main():

     pet = Pet()
     Name = input("What is your pets name? ")
     Type = input("What type of animal is your pet? ")
     Age = input("How old is your pet? ")


     
     # Store values in the object's fields.
     pet.set_NameOfPet(Name)
     pet.set_TypeOfPet(Type)
     pet.set_AgeOfPet(Age)

     # Display the values stored in the fields.
     print("Your pet's name is", pet.get_NameOfPet())
     print("Your pet is a", pet.get_TypeOfPet())
     print("Your pet is", pet.get_AgeOfPet(),"years old")

# Call the main function.
main()
