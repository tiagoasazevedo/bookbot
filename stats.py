def count_words(file_contents): #function that will count the words
	words = file_contents.split() #splits the contents of the document and adds every word to a list
	num_words = len(words) #counts the items in the list and stores in a variable
	return num_words #it returns the value so it can be later used