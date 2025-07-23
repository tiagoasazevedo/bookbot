def get_book_text(book):
	with open(book) as f:
		file_contents = f.read()
	return file_contents

from stats import count_words

def main():
	book_content = get_book_text("books/frankenstein.txt")
	num_words = count_words(book_content)
	print(f"{num_words} words found in the document")

main()
