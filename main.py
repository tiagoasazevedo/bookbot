def get_book_text(book): #function that will open and fetch the document contents
	with open(book) as f: #opens the book and stores it temporarly in f
		file_contents = f.read() #reads the content and stores in the new variable to be used later
	return file_contents #returns the value so it can be used

from stats import count_words #imports the fucntion stored in the stats.py file
from stats import count_each_charater #imports the function in the stats.py file
from stats import sort_characters #imports the function in the stats.py file

def main(): #the funcion that will do the work to communicate the final results
	book_content = get_book_text("books/frankenstein.txt") #it uses the function that will fetch the document and tells it which document to use
	num_words = count_words(book_content) #counts the words and stores the value in a variable for later usage
	character_counts = count_each_charater(book_content) #counts the sorted character and stores the value in a variable for later usage
	character_entries = sort_characters(character_counts) #sorts the characters and stores the entries in a variable for later usage
	print("============ BOOKBOT ============") #prints the intended header
	print("Analyzing book found at books/frankenstein.txt...") #prints the intended header
	print("----------- Word Count ----------") #prints the intended header
	print(f"Found {num_words} total words") #prints the result with the desired message
	print("--------- Character Count -------") #prints another header
	for entry in character_entries: #loops the list and for each dictionary it only prints the items
		print(f"{entry['char']}: {entry['num']}") #prints the characters as intended
	print("============= END ===============") #prints the foot

main() #calls the function that communicates the desired end result
