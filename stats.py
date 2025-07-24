def count_words(file_contents): #function that will count the words
	words = file_contents.split() #splits the contents of the document and adds every word to a list
	num_words = len(words) #counts the items in the list and stores in a variable
	return num_words #it returns the value so it can be later used

def count_each_charater(file_contents): #function that will count each charater recurrence
	import collections #imports collections so I can use them
	lower_contents = file_contents.lower() #lower each character so we don't have duplicates
	character_counts = collections.Counter(lower_contents) #uses a collection to to count the character
	return character_counts

def sort_characters(character_counts): #function that will sort the characters
	character_entries = [] #creates an empty list to populate with the alphabetical characters
	for char, count in character_counts.items(): #this will check if each character is an alphabetical character
		if char.isalpha(): #checks if the character is alphabetical
			character_entries.append(f"{char}: {count}") #appends alphabetical characters with its count
	character_entries.sort(reverse=False) #sorting the list so when the funciton returns the list it's already as intended
	return	character_entries #returns the list with the characters already sorted