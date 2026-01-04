import sys
from stats import get_num_words, get_book_text, get_character_count_map, get_sorted_character_count

def main():
    if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
      return
    
    book_path = sys.argv[1] 
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_map = get_character_count_map(text)
    characters_sorted = get_sorted_character_count(character_map)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in characters_sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()


