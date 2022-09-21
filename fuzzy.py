# A PROGRAM FOR FUZZY DECISION MAKING BY C.P. WHALEY 1979
# converted to Python by R Burrows 11/2018 for Dayton

# global constants functions and declarations

####110 DEFINT I-N
##static int I,J,K,M,N,NS,CH,X,Y;
##static double TS,SM,LM,Q,MU,MX;
import math

NEWLINE = '\n';
def getValidInteger(l,u,name,enterMessage):   #integer.py Class 8 Notes & Materials
        valid = False; #assume guilty until proven innocent
        while not valid:
            i =input(enterMessage+" between "+str(l)+" and "+str(u)+": ")
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
                
def is_int(s):  #valid int
    try:
        int(s)
        return True
    except ValueError:
        return False

####140 DIM A(10, 10), B(10), C(10), E(10), R(10)

A = [[0.0]*10  for i in range(10)]
B = [0.0]*10
C = [0.0]*10
D = [0.0]*10
E = [0.0]*10
R = [0.0]*10
DC = [0.0]*10

##145 DIM L$(10), S$(10, 10), DC(10)

L = [" "]*10
S = [[0.0]*10  for i in range(10)]


OutBuf = ""
SInput = ""

C1 =[" "]*10
GetNumber=""

def compute(OutBuf): 
## Method Compute

##150 GOTO 1000
##160 REM EIGEN ANALYSIS SUBROUTINE
##180 FOR I = 1 TO M
##182     E(I) = 1 / M
##184     B(I) = E(I)
##186 NEXT I
##
    for I in range (1,M+1):
        E[I] = 1.0/M
        B[I] = E[I]
##
##190 FOR I = 1 TO M
##191     TS = 0
##192     FOR J = 1 TO M
##193             TS = TS + B(J) * A(I, J)
##194     NEXT J
##195     R(I) = TS
##196 NEXT I
##
    for I in range (1,M+1):
        TS=0;
        for J in range(1,M+1):
             TS = TS + B[J] * A[I][J]
        R[I] = TS
##
##200 SM = 0
##201 FOR I = 1 TO M
##202     SM = SM + R(I)
##203 NEXT I
##210 FOR I = 1 TO M
##211     E(I) = R(I) / SM
##212 NEXT I
##220 FOR I = 1 TO M
##221     C(I) = ABS(B(I) - E(I))
##222     IF (C(I) - .001) > 0 GOTO 240
##223 NEXT I
##230 GOTO 260
##240 FOR I = 1 TO M
##241     B(I) = E(I)
##242 NEXT I
##
## get rid of go tos in Python
    SM = 0
    for I in range (1,M+1):
        SM=SM + R[I]
    for I in range (1,M+1):
        E[I] = R[I] / SM
    for I in range (1,M+1):
        C[I] = abs(B[I] - E[I])
        if ((C[I] - .001) > 0 ):
            for J in range (1,M+1):
                B[J] = E[J];
            break;## get out of for loop go to outer loop go back to top loop
##250 GOTO 190
##
##260 LM = SM
##270 PRINT
##271 PRINT "EIGENVALUE = "; LM
##
    LM=SM;
    OutBuf = OutBuf + "FUZZY DECISION MAKING OUTPUT\n\nEIGENVALUE = " + str(LM) + "\n\n"
##
##280 FOR I = 1 TO M
##281      D(I) = E(I) * M
##282 NEXT I
##
    for I in range (1,M+1):
        D[I]= E[I] * M

##
##290 PRINT
##291 PRINT "EIGENVECTOR ..."
##292 PRINT
##300 FOR I = 1 TO M
##301     PRINT E(I)
##302 NEXT I
##310 PRINT
##
    OutBuf= OutBuf + "EIGENVECTOR ..." +"\n"
    for I in range (1,M+1):
        OutBuf = OutBuf + str(E[I]) + "\n"

##
##311 PRINT "ALPHA-VECTOR ..."
##312 PRINT
##320 FOR I = 1 TO M
##321     PRINT D(I)
##322 NEXT I
##330 MU = (LM - M) / (M - 1)
##334 Q = SQR(MU / 2)
##335 PRINT
##340 PRINT
##341 PRINT "CONSISTENCY OF THE PAIRED-COMPARISON MATRIX = "; Q
##
    OutBuf= OutBuf + "\nALPHA-VECTOR ..." +"\n"
    for I in range (1,M+1):
        OutBuf = OutBuf + str(D[I]) + "\n"

    MU = (LM - M) / (M - 1)
    Q = math.sqrt(MU / 2)
    OutBuf= OutBuf + "\nCONSISTENCY OF THE PAIRED-COMPARISON MATRIX = " + str(Q) +"\n"
    return OutBuf
##
##350 RETURN
##

#main
intro=""
while not(intro.upper()=="Y" or intro.upper()=="N"):
    intro = input("Would you like to see an introduction? Enter Y or N: ");
if (intro.upper()==("Y")):
    print("                     Introduction to Fuzzy Decision Making"+ NEWLINE \
                              + "     Often at work, as in life, we are faced with a tough decision between several seemingly " + NEWLINE \
                              + "equal alternatives.  Let's take the common example of buying a car.  After visiting many" + NEWLINE \
                              + "dealers, the three cars you like are made by Saturn, Buick and Lexus.  Your decision depends on" + NEWLINE \
                              + "several factors, or criteria, important to you.  Let's say these are cost, style, comfort, safety," + NEWLINE\
                              + "gas mileage and pollution the car emits.  For each factor you can rate each car from a scale of" + NEWLINE\
                              + "1 to 10, where 10 is better.  In this example since cost is likely higher for a Lexus, The Lexus" +NEWLINE\
                              + "would get a lower rating on cost than either the Saturn or the Buick.  Conversely, the style of" + NEWLINE\
                              + "Lexus might have a higher rating than either of the other two cars.  Just doing these ratings only," + NEWLINE\
                              + "does not give all the input we need to make the decision.  The importance or weight of each" + NEWLINE\
                              + "criteria in comparison to all other criteria factors into your decision.  For example, you may" + NEWLINE\
                              + "be on a tight budget and cost is more important to you than style, but since you've also been" + NEWLINE\
                              + "in several big accidents in the past few years perhaps safety is even more important than cost." + NEWLINE\
                              + "Keeping all this information in your head, let alone synthesizing it, is simply impossible." + NEWLINE\
                              + "You can now see why you sometimes agonize over a decision, and once made still often question or" + NEWLINE\
                              + "try to justify your choice." + NEWLINE\
                              + "     But have no fear, for all your 'fuzzy' decisions, this program FUZZY is here to help.  Based" + NEWLINE\
                              + "on work by several scientists in decision theory an algorithm was developed to help you decide." + NEWLINE\
                              + "If you are interested in the algorithm you can read the documentation by Michael O'Hagan at the site:" + NEWLINE\
                              + "http:##www.fuzzysys.com/fdmtheor.pdf   This program is a java adaptation of the original program" + NEWLINE\
                              + "done by C.P.Waley (1979) in the BASIC language."\
                              + "Click on OK below to begin entering your decision alternatives.  Have fun!"+NEWLINE)
                              

## 1000 REM **************** MAIN ROUTINE ******************
##   1100 CLEAR
##   1101 INPUT "NO. OF ALTERNATIVES:  "; NS
##


OutBuf += "FUZZY DECISION MAKING INPUT \n\n"

NS = getValidInteger(1,10,"NO. OF ALTERNATIVES:","INPUT NO. OF ALTERNATIVES")

OutBuf += "INPUT NO. OF ALTERNATIVES:  "+ str(NS) + "\n"

#### 1110 PRINT
##1111 PRINT "ENTER LABELS FOR ALTERNATIVES ..."
##1120 FOR I = 1 TO NS
##1123    INPUT L$(I)
##1124 NEXT I ##

for I in range (1,NS+1):
    L[I] = input("INPUT LABEL FOR ALTERNATIVE "+ str(I)+": ")
    OutBuf += L[I] +"\n"

####
##1130 PRINT
##1132 INPUT "NO. OF CRITERIA FOR THE DECISION: "; M
##1140 PRINT
##1141 PRINT "ENTER LABELS FOR CRITERIA ..."
##1150 FOR I = 1 TO M
##1151    A(I, I) = 1!
##1152    INPUT C$(I)
##1153 NEXT I
####

M = getValidInteger(1,10,"NO. OF CRITERION","INPUT NO. OF CRITERION FOR DECISION")
OutBuf += "\n INPUT NO. OF CRITERION FOR DECISION: " + str(M) +"\n"
for I in range(1,M+1):
    A[I][I]=1.0
    C1[I] = input("INPUT LABELS FOR CRITERIA "+ str(I)+ ": ")
    OutBuf += str(C1[I]) +"\n"
##
##1154 PRINT "**********************": PRINT
##1156 PRINT "IN EACH CASE ENTER A VALUE BETWEEN 0 AND 10"
##1158 PRINT "WHERE A HIGHER VALUE MEANS BETTER": PRINT
##1160 PRINT
##
print("      Criteria Ranking --> 0 = WORST 10 = BEST"+ NEWLINE+
      "YOU WILL NOW RANK THE HOW IMPORTANT EACH CRITERIA IS TO YOU." +"\n" +\
      "IN EACH CASE ENTER A VALUE BETWEEN 0 AND 10" + "\n" + \
      "WHERE A HIGHER VALUE MEANS BETTER ")
OutBuf += "\n CRITERIA RANKING --> 0 = WORST, 10 = BEST :\n"

##
##1161 FOR I = 1 TO M
##1162    FOR J = 1 TO NS
##1170            PRINT "ENTER "; C$(I); " RATING FOR "; L$(J); "  ";
##1172            INPUT S(I, J): PRINT
##1173            S(I, J) = S(I, J) / 10!
##1181    NEXT J
##1182 NEXT I
##
for I in range(1,M+1):
    for J in range(1,NS+1):
        K = getValidInteger(0,10,"RATING",("ENTER "+ str(C1[I]) + " RATING FOR " + L[J]))
        OutBuf += str(C1[I]) + " RATING FOR " + L[J] + " = " + str(K) + "\n"
        S[I][J] = K/10.0
##
##1190 PRINT : PRINT : PRINT
##1200 PRINT 'RATINGS OF THE CRITERIA"
##1210 PRINT "**********************": PRINT
##1220 PRINT "FOR EACH PAIR OF THE CRITERIA ENTER 1 OR 2 TO INDICATE WHICH IS"
##1225 PRINT "MORE IMPORTANT, FOLLOWED BY A COMMA, FOLLOWED BY A NUMBER BETWEEN"
##1230 PRINT "1 AND 9 TO INDICATE HOW MUCH MORE IMPORTANT, DEFINITIONS FOR SOME"
##1235 PRINT "OF THE VALUES ARE:"
##1237 PRINT
##1240 PRINT "    1 - EQUAL IMPORTANCE"
##1245 PRINT "    3 - WEAK IMPORTANCE OF ONE OVER THE OTHER"
##1250 PRINT "    5 - STRONG IMPORTANCE OF ONE OVER THE OTHER"
##1255 PRINT "    7 - DEMONSTRATED IMPORTANCE OF ONE OVER THE OTHER"
##1260 PRINT "    9 - ABSOLUTE IMPORTANCE OF ONE OVER THE OTHER"
##1265 PRINT
##1266 PRINT "USE 2, 4, 6 & 8 WHEN THE DEGREES OF IMPORTANCE FALLS BETWEEN"
##1270 PRINT "THE VALUES ASSIGNED ABOVE.": PRINT
##1290 PRINT
##
print("                  Criteria Comparison\n" + \
 "FOR EACH PAIR OF THE CRITERIA ENTER 1 OR 2 TO INDICATE WHICH IS\n"   + \
 "MORE IMPORTANT, FOLLOWED BY A COMMA, FOLLOWED BY A NUMBER BETWEEN\n" + \
 "1 AND 9 TO INDICATE HOW MUCH MORE IMPORTANT, DEFINITIONS FOR SOME\n" + \
 "OF THE VALUES ARE:\n\n"  + \
 "    1 - EQUAL IMPORTANCE\n" + \
 "    3 - WEAK IMPORTANCE OF ONE OVER THE OTHER\n" + \
 "    5 - STRONG IMPORTANCE OF ONE OVER THE OTHER\n" + \
 "    7 - DEMONSTRATED IMPORTANCE OF ONE OVER THE OTHER\n" + \
 "    9 - ABSOLUTE IMPORTANCE OF ONE OVER THE OTHER\n\n" + \
 "USE 2, 4, 6 & 8 WHEN THE DEGREES OF IMPORTANCE FALLS BETWEEN\n" + \
 "THE VALUES ASSIGNED ABOVE.")
##
##1400 FOR I = 2 TO M
##1410    FOR J = 1 TO I - 1
##1420            PRINT
##1421            PRINT "(1) "; C$(J), " -- ", "(2) "; C$(I)
##1430            PRINT
##1431            INPUT X, Y
##1435            IF X = 2 THEN
##1436                     A(I, J) = Y
##1437                     A(J, I) = 1 / Y
##1438            ELSE
##1440                          A(J, I) = Y
##1441                          A(I, J) = 1 / Y
##1442            END IF
##1450    NEXT J
##1451 NEXT I
##
## don't show all this

OutBuf += "\n COMPARING CRITERIA - Winner and by how much 1-9\n";
##
##FOR EACH PAIR OF THE CRITERIA ENTER 1 OR 2 TO INDICATE WHICH IS\n"   +
## "MORE IMPORTANT, FOLLOWED BY A COMMA, FOLLOWED BY A NUMBER BETWEEN\n" +
## "1 AND 9 TO INDICATE HOW MUCH MORE IMPORTANT, DEFINITIONS FOR SOME\n" +
## "OF THE VALUES ARE:\n\n"  +
##
## "    1 - EQUAL IMPORTANCE\n" +
## "    3 - WEAK IMPORTANCE OF ONE OVER THE OTHER\n" +
## "    5 - STRONG IMPORTANCE OF ONE OVER THE OTHER\n" +
## "    7 - DEMONSTRATED IMPORTANCE OF ONE OVER THE OTHER\n" +
## "    9 - ABSOLUTE IMPORTANCE OF ONE OVER THE OTHER\n\n" +
##
## "USE 2, 4, 6 & 8 WHEN THE DEGREES OF IMPORTANCE FALLS BETWEEN\n" +
## "THE VALUES ASSIGNED ABOVE.\n\n";
##
for I in range(2,M+1):
    for J in range(1,I):
        ##NEED TO ADD ERROR CHECKING
        validXCR = False #validate criteria rating
        validYCR = False
        while not(validXCR and validYCR):
            GetNumber = input("(1) "+ str(C1[J]) + " -- " + "(2) " + str(C1[I])+": ")
            ##  <parse input to comma>
            endX = GetNumber.find(",")
            if endX != -1: # found a comma
                if is_int(GetNumber[0:endX]):
                    X=int(GetNumber[0:endX])
                    if (1<=X<=2):
                        validXCR=True
                    else:
                        validXCR=False
                else:
                    validXCR=False
                if is_int(GetNumber[endX+1:len(GetNumber)]):
                    Y=int(GetNumber[endX+1:len(GetNumber)])
                    if (1<=Y<=9):
                        validYCR=True
                    else:
                        validYCR=False
                else:
                    validYCR=False
            if not(validXCR and validYCR):
                print("Invalid criteria entry try again")
        ## process it's good
        if (X == 2):
            A[I][J] = Y
            A[J][I] = 1.0 / Y
        else:
            A[J][I] = Y;
            A[I][J] = 1.0 / Y
        OutBuf += "(1) "+ str(C1[J]) + " -- " + "(2) " + str(C1[I]) + " = " + GetNumber + "\n"
##
##1460 PRINT : PRINT : PRINT "FUZZY DECISION MAKING PROGRAM OUTPUT"
##1465 PRINT "************************************": PRINT
##1470 GOSUB 160
##
SInput = OutBuf
OutBuf = ""
OutBuf=compute(SInput)
##
##1500 REM *********** PRINT RESULTS ******************
##1510 FOR J = 1 TO NS
##1515    DC(J) = 999999!
##1520    FOR I = 1 TO M
##1530            S(I, J) = S(I, J) ^ D(I)
##1531            IF S(I, J) < DC(J) THEN DC(J) = S(I, J)
##1540    NEXT I
##1541 NEXT J
##1550 PRINT
##1560 PRINT "WEIGHTED FUZZY SETS ...": PRINT
##
for J in range(1,NS+1):
    DC[J] = 999999.0
    for I in range(1,M+1):
        S[I][J] = pow(S[I][J],D[I])
        if (S[I][J] < DC[J]):
            DC[J] = S[I][J]
OutBuf = OutBuf + "WEIGHTED FUZZY SETS ...\n";
##
##1570 FOR I = 1 TO M
##1580    FOR J = 1 TO NS
##1581            PRINT S(I, J);
##1582    NEXT J
##1583    PRINT : PRINT
##1590 NEXT I
##1600 PRINT : PRINT "DECISION VALUES ...": PRINT
##
for I in range(1,M+1):
    for J in range(1,NS+1):
              OutBuf= OutBuf + str(S[I][J]) + "  "
	     
    OutBuf += "\n";
OutBuf = OutBuf + "\nDECISION VALUES ...\n";
##
##1605 MX = -9999
##1610 FOR I = 1 TO NS
##1611    PRINT L$(I); " - "; DC(I)
##1612    IF DC(I) > MX THEN MX = DC(I): CH = I
##1615 NEXT I
##1616 PRINT
##1650 PRINT "**** L$(CH); " IS THE BEST CHOICE ****\n ACCORDING TO THE DATA YOU HAVE ENTERED"
##1699 END
##
MX = -9999
for I in range(1,NS+1):
    OutBuf = OutBuf + L[I] + " - " + str(DC[I]) + "\n"
    if (DC[I] > MX): 
            MX = DC[I]
            CH = I
OutBuf = OutBuf + "\n****  " + L[CH] + " IS THE BEST CHOICE ****\nACCORDING TO THE DATA YOU HAVE ENTERED"
print(OutBuf)

