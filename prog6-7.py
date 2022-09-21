#prog 6-7 Test Average and Grade - redo with arrays

def calcAverage(t1,t2,t3,t4,t5,t6):
    totalTests = t1+t2+t3+t4+t5
    average = totalTests/5
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
        
#main
print("Enter your test scores numbers 0 to 100")
test1 = int(input("Test 1: "))
test2 = int(input("Test 2: "))
test3 = int(input("Test 3: "))
test4 = int(input("Test 4: "))
test5 = int(input("Test 5: "))
test6 = int(input("Test 6: "))
grade1 = determineGrade(test1)
print("test 1 score is",test1,"letter grade", grade1)
grade2 = determineGrade(test2)
print("test 2 score is",test2,"letter grade", grade2)
grade3 = determineGrade(test3)
print("test 3 score is",test3,"letter grade", grade3)
grade4 = determineGrade(test4)
print("test 4 score is",test4,"letter grade", grade4)
grade5 = determineGrade(test5)
print("test 5 score is",test5,"letter grade", grade5)
grade6 = determineGrade(test6)
print("test 6 score is",test6,"letter grade", grade6)
gradeAvg = calcAverage(test1,test2,test3,test4,test5,test6)
print("Average test Grade:",gradeAvg,"letter grade",determineGrade(gradeAvg))


    
        
    
