def showSum(num1, num2):
    result = num1 + num2;
    print("result is",result)
    num1 = num1 + 1;
    num2 = num2 + 1;
    return result,num1,num2


def main():
    int1=4;
    int2=8;
    print("before call of showSum int1 =",int1, "int2 =",int2)
    result,int1,int2 = showSum(int1,int2);
    print("after call of showSum int1 =",int1,"int2 =",int2,"result =",result)

main()




#Personal Note:
    #ch03.pptx, Slide 32
