from stats import *
import sys


def get_book_text(filePath):
    with open(filePath) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    num_word = num_words(get_book_text(path_to_book))
    new_count = sort_dict(count_characters(get_book_text(path_to_book)))
    print(f"{num_word} words found in the document")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")
    for char, count in new_count:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")

main()
