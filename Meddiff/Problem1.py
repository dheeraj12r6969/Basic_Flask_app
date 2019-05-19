def group_by_owners(data):     
    tempDict=dict();
    for book,author in data.items():
    	# print(author in tempDict)
    	if (author in tempDict)==False:
    		tempDict[author]=list()    #assignment list for values
    	books=tempDict[author]
    	books.append(book)
    	tempDict[author]=books
    print(tempDict)

if __name__ == '__main__':
	DemoDict = dict()
	TotalNumberOfKeyValuePair = int(input("Enter number of key value pair : "))
	while TotalNumberOfKeyValuePair > 0:
		ConsoleData  = input("Enter FileName {} and OwnerName separated by comma (,): ".format(TotalNumberOfKeyValuePair))    
		key, value = ConsoleData.split(",")
		DemoDict[key] = value
		TotalNumberOfKeyValuePair -= 1
	#DemoDict={ "5 point someone":"dheeraj","11 minutes":"dheeraj","Ramayan":"piyush"}
	group_by_owners(DemoDict)