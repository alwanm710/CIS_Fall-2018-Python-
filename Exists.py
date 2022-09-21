import sys,os
fileName = "numbers.txt"
if not os.path.exists(fileName):
    print(fileName,"does not exist")
    sys.exit(0)
else:
    print(fileName,"found")
    

