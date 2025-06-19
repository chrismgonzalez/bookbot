import sys
from stats import get_num_words, get_char_count, build_char_dicts

def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
    return file_contents


def main():

  if len(sys.argv) < 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)
    
  book_text = get_book_text(sys.argv[1])
  num_words = get_num_words(book_text)
  char_count = get_char_count(book_text)
  char_dicts = build_char_dicts(char_count)

  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("------------ Word Count --------------")
  print(f"Found {num_words} total words")
  print("------------ Character Count -------------")
  ordered_char_dicts = char_dicts

  for dict in ordered_char_dicts:
      char = dict["char"]
      count = dict["num"]
      print(f"{char}: {count}")
    


main()