class Animal: # standard example for Polymorphism - inheritance
    def show_species(self):
        print('I am just a regular animal.')
        
    def make_sound(self):
        print('Grrrrrr')
            
class Dog(Animal): #Dog superclass of animal
    def show_species(self):
        print('I am a dog.')
    def make_sound(self):
        print('Woof! Woof!')

class Cat(Animal): #Cat superclass too
    def show_species(self):
        print('I am a cat.')
    def make_sound(self):
        print('Meow')

# The show_animal_info function accepts an Animal
    # object as an argument and displays information
    # about it. changes to class methods based on which object using
def show_animal_info(creature):
    creature.show_species()  #polymorphism, Python calls the appropriate
    creature.make_sound()    #functions for kind of animal it is don't need
                             # if type dog do this or if type cat do that    
    
# Here is the main function.
def main():
# Create an animal object, a Dog object, and 26 # a Cat object.
    my_animal = Animal()
    my_dog = Dog()
    my_cat = Cat()
# Show info about an animal.
    print('Here is info about an animal.')
    show_animal_info(my_animal)
    print()
    # Show info about a dog.
    print('Here is info about a dog.')
    show_animal_info(my_dog)
    print()
    # Show info about a cat.
    print('Here is info about a cat.')
    show_animal_info(my_cat)
    # The show_animal_info function accepts an Animal
    # object as an argument and displays information
    # about it.

# Call the main function.
main()
