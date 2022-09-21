def showMessage(message):
	print(message)
	message = "Mohammad said " + message
	print (message)
	return(message)
    
messageToDisplay = input("Enter message you want to display: ")
newMessage = showMessage(messageToDisplay) #main
print (newMessage)
