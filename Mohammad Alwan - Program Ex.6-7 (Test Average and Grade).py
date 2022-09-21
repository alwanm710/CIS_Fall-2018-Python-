#Mohammad Alwan, Program Ex.6-7 (Test Average and Grade)

def CaclAverage(Test1, Test2, Test3, Test4, Test5):
    Average = (Test1 + Test2 + Test3 + Test4 + Test5) / 5
    return(Average)


def DetermineGrade(s):
    if s >= 90:
        return("A")
    elif s >= 80:
        return("B")
    elif s >= 70:
        return("C")
    elif s >= 60:
        return("D")
    else: #Most be 59 or lower
        return("F")


#Main
test1 = int(input("Enter socre for test 1(Between 1 and 100):"))
test2 = int(input("Enter socre for test 2(Between 1 and 100):"))
test3 = int(input("Enter socre for test 3(Between 1 and 100):"))
test4 = int(input("Enter socre for test 4(Between 1 and 100):"))
test5 = int(input("Enter socre for test 5(Between 1 and 100):"))

    #Printing out the test scores and grades of each the 5 tests
print("Your score for test 1 is",test1,"out of 100, So your grade for test 1 is",DetermineGrade(test1))
print("Your score for test 2 is",test2,"out of 100, So your grade for test 2 is",DetermineGrade(test2))
print("Your score for test 3 is",test3,"out of 100, So your grade for test 3 is",DetermineGrade(test3))
print("Your score for test 4 is",test4,"out of 100, So your grade for test 4 is",DetermineGrade(test4))
print("Your score for test 5 is",test5,"out of 100, So your grade for test 5 is",DetermineGrade(test5))

    #Printing out the average test scores and grades of all the 5 tests
AverageTestScore = CaclAverage(test1, test2, test3, test4, test5)
print("Your average test score is",AverageTestScore,"out of 100, So your average grade for all 5 test is",DetermineGrade(AverageTestScore))
