def main():
    book_path = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        
    word_count = get_word_count(file_contents)
    character_count = get_character_count(file_contents)
    sorted_chars = char_sort(character_count)
    
    print(f"--Beginning report of {book_path}--")
    print(f"There are {word_count} words in this document.")
    for item in sorted_chars:
        print(f"The {item['char']} character was found {item['num']} times.")
    

def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)
    
def get_character_count(file_contents):
    letters = {}
    lowered_text = file_contents.lower()
    for letter in lowered_text:
        if letter.isalpha():
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
    return letters

def char_sort(character_count):
    character_list = [{'char': k, 'num': v} for k, v in character_count.items()]
    character_list.sort(reverse=True, key=lambda d: d['num'])
    return character_list
    
    

    


if __name__ == '__main__':
    main ()