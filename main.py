from stats import get_num_words, get_book_text, get_character_count_map, get_sorted_character_count

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    character_map = get_character_count_map(text)
    characters_sorted = get_sorted_character_count(character_map)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in characters_sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()


