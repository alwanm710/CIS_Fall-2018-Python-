def getValidInteger(l,u,name,enterMessage):   #note changed function name 
        valid = False; #assume guilty until proven innocent
        while not valid:
            i =input(enterMessage+" between "+str(l)+" and "+str(u)+":")
            try:
                i =int(i)
                isInt = True
            except:
                isInt = False
            if isInt:
               if l <= i <= u:
                   return i
               else:
                   print("Error -", name, "must be between", 1, "and" ,u)
            else:
                print("Oops",i,"is not a valid integer - try again")
class Account:
    def __init__(self,acctNumber): #acct number mandatory ew account
        if not isinstance(acctNumber, int): #Python doesn't declare type of class variable
            raise TypeError("account number must be set to an integer")
        elif not (acctNumber >=1 and acctNumber <= 9999999):
            raise TypeError("account number must be between 1 and 9999999")
        else:
            self.__account_number = acctNumber 
    def get_account_number(self):
        return self.__account_number

# call to input a midterm score.
#what programmer should do and also check database not a duplicate account number
inputAcct = getValidInteger(1,9999999,"account number","Please enter account number" )
#inputAcct = int(input("enter new account number:")) #note this misses 0 
acct_id = Account(inputAcct)
print("acct number is",acct_id.get_account_number())
