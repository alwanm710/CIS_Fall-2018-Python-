def getValidInteger(l,u,name,enterMessage):   
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
                print("Oops",i,"is not a valid integer - try again\n")
#main
menuSelection = getValidInteger(1,3,"menu selection","Please enter menu choice")
