def func(array,real):
    for i in range(0,len(array)):
        array[i] = array[i] + 1
    real = round((real + .1),2)
    print(array,real)

x = [1, 2, 3]
r = 1.1
print (x,r) 
func(x,r)
print (x,r)




#Personal Note:
##ch08_(1).pptx, Slide 28
