def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)
    

def get_character_count_map(text):
    characters = text.lower()
    character_count = {}
    for character in characters:
        if character.isalpha() == False:
            continue  
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def get_sorted_character_count(characters_map):
    def sort_on(items):
      return items["num"]
    
    sorted_characters = []
    for character in characters_map:
        sorted_characters.append({"char": character, "num": characters_map[character]})
    
    sorted_characters.sort(reverse=True, key=sort_on)

    return sorted_characters