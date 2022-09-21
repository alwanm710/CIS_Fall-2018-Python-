# Table 4-1 Relational Operators Operator Meaning
# > Greater than    <= Less than or equal to
# < Less than       >= Greater than or equal to
#== Equal to        != Not equal to   <-- == why not just single '=' in if statement?
# The relational operators are used to create Boolean expressions (expression that has a result of true or false)
# and are commonly used with if statement
# The if clause begins with the word if, followed by a condition, which is an expression that will be evaluated
# as either true or false. A colon appears after the condition.
# Beginning at the next line is a block of statements. All of the statements in a block must be consistently indented.
# Should use tab key - note cannot mix tab and spaces must be consistent as well
# Brillant - in sll other lsnguages I have used in 50 years of programming the indenttion was highly recommended but had
#   no meaning - Python makes indentation mandatory
def example1():
    a=int(input('Input an integer number '))
    #simplest  - note no false condition
    if a < 5: 
        print ('the number you entered ia less than 5')
def example2():
    #if then else handles both true and false case
    a=int(input('Input an integer number '))
    if a >= 5:  
        print ('number you entered ia greater than or equal to 5') #true
    else:       #false
        print ('number you entered is less than 5')

def example3():
    # nested on if inside another - barrels
    a=int(input('Input an integer number '))
    if a < 5:
        if a < 0:
            print('number which is '+ a + ' is less than 0')
        else:
            print('number is btween 1 and 4')
    else:
        print ('number is 5 or greater than 5')
def example4():
    #grade if statement page 181 
    score = int(input('Input a test score '))
    if   score < 60:
        print('F')
    elif score < 70:
        print('D')
    else:
        print('A','B', 'or C')
def example5():
    #case or switch statement which other languages have - Python doesn't have but
    #does have something called Python dictionaries aka associative arrays
    #animal and sound - ala gandson Roger
    sound = input('input animal sound ')
    if   sound == 'moo':
        print('cow')
    elif sound == 'rivet':
        print('frog')
    elif sound == 'neigh':
        print('horse')
    else:
        print("don't know that sound")
def example6():
    def cow():
        print('cow')
    def frog():
        print('rivet')
    def horse():
        print('horse')
       
    options ={'moo'   : cow,
              'rivet' : frog,
              'neigh' : horse
              }
    #not so good if not in dictionary 
    try:
        options[sound]()
    except:
        print("don't know that sound")
def example7():
    #compound condition and, or , not
    a=int(input('Input an integer number '))
    if a == 5 and a == 6:
        print ('number you entered ia 5 and 6') # will this print statement ever execute?
    if a != 5 or a != 6:
        print ('number you entered ia 5 or 6') # will this print statement ever execute?    
    if a >= 5 and a%2 == 0: # here and makes sense - what is second condtion checking?
        print ('number you entered ia greater than 6 and a ____ number')
    else:
        print ('number you entered is less than 5 or is >= 5 but not _____')    
    if a >= 5 or a <= 2:
        print ('number you entered is between 2 and 5 inclusive')
    else:
        print ('number you  entered is 3 or 4')
    if not(a >= 5) : #talk in the negstive - friend who says I don't want nothing - doesn't this mean you want something?
        print ('number you entered is less than 5')    
    b=int(input('Input a second integer number '))
    # and with two vsriables most often
    if a >= 5 and b < 3:
        print ('The first number you entered is greater than or equal to 5 and the second number you entered is less than 3')
    else:
        print ('The first number you entered id less thsn 5 or the second number you entered is __________?')
def example8():
    a=int(input('Input an integer number '))
    #Be very careful with English and, or, with not
    if not(a == 5) and not(a == 6):
        print (' a is not equal 5 and a is not equal to 6')
    bool=True # boolean vsrisble is True or False
    if bool:
        print('bool is true')
    bool = a>5
    if not(bool):
        print('first number not > 5')
        
#Main
example1()
example2()
example3()
example4()
example5()
example6()
example7()
example8()

