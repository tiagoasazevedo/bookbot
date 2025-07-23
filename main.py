def get_book_text(book): #function that will open and fetch the document contents
	with open(book) as f: #opens the book and stores it temporarly in f
		file_contents = f.read() #reads the content and stores in the new variable to be used later
	return file_contents #returns the value so it can be used

from stats import count_words #imports the fucntion stored in the stats.py file

def main(): #the funcion that will do the work to communicate the final results
	book_content = get_book_text("books/frankenstein.txt") #it uses the function that will fetch the document and tells it which document to use
	num_words = count_words(book_content)
	print(f"{num_words} words found in the document")

main()
