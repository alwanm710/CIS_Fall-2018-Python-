#prog 6-7 Test Average and Grade - redo with arrays
NUM_TESTS=5
def calcAverage(t):
    sum = 0
    for index in range (1,NUM_TESTS + 1):
       sum=sum+t[index]
    average = sum/(NUM_TESTS) 
    return average

def determineGrade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else: #below 60 "F"
        grade = "F"
    return(grade)
        
#main index is testNum short for testNumber
test=[0]*(NUM_TESTS + 1)  #initialize an array of noOfTests variables to 0 - [0]
for testNum in range(1,NUM_TESTS + 1):
    test[testNum] = int(input("Test "+ str(testNum) + ": "))
for testNum in range(1,NUM_TESTS + 1):
    print("test ",testNum," score is ",test[testNum]," letter grade ",determineGrade(test[testNum]),sep="")
average = calcAverage(test)
print("Average test Grade:",average,"letter grade",determineGrade(average))        
#add to program

max = test[1]
min = test[1]

for i in range(2,NUM_TESTS):  #why start index at 2?
     if test[i] > max:
         max = test[i]
     if test[i] < min:
         min = test[i]
print ("max =",max,"min =",min)    
print(test)
test.sort()
print(test)
