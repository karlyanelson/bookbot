def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)
    

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    

main()


