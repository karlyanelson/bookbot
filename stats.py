def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)
    

def get_character_count(text):
    characters = text.lower()
    character_count = {}
    for character in characters:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count