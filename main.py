from stats import get_num_words, get_book_text, get_character_count

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    num_characters = get_character_count(text)
    print(f"Found {num_words} total words")
    print(num_characters)

main()


