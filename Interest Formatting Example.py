#rounding, formatting which includes rounding and truncating stealing example
INTEREST_RATE = .049  # what percentage is this?

moneyInBank = 12.00 
interest = moneyInBank * INTEREST_RATE
print ("interest is",interest)
print ("interest is $", round(interest,2))
print ("interest is $", format(interest,'>.2f'))

interestTruncated = int(interest * 100)/100.00 # person won't notice penny
print("Your interest is $",format(interestTruncated,'>.2f'))
putInMyAccount = interest - interestTruncated
print("put in my account", format(putInMyAccount,'>.3f'),
      "cause you'll never check your bank account for rounding to nearest penny")
