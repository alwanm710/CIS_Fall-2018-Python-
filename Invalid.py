def is_float(s):    #better  with type of error which is ValueError
    try:
       float(s)
       return True
    except ValueError:
        return False
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
s5='-1.23'
s6='-1300'
if is_float(s5):
    print(s5,'is a float')
if is_float(s6):
    print(s6,'is a float')
if is_integer(s5):
    print(s5,'is an integer')
else:
    print(s5,'is not an integer')


#Personal Note:
    #ch07.pptx, Slide 10
