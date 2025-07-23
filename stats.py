def count_words(file_contents): #function that will count the words
	words = file_contents.split() #splits the contents of the document and adds every word to a list
	num_words = len(words) #counts the items in the list and stores in a variable
	return num_words #it returns the value so it can be later used

def count_each_charater(file_contents): #function that will count each charater recurrence
	import collections #imports collections so I can use them
	lower_contents = file_contents.lower() #lower each character so we don't have duplicates
	character_counts = collections.Counter(lower_contents) #uses a collection to to count the character
	return character_counts