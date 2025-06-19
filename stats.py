def get_num_words(book_text):
    return len(book_text.split())

def get_char_count(book_text):
    chars = {}
    for i, char in enumerate(book_text):
        char = char.lower()
        # if the char is not found, add it and set it to 1
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def build_char_dicts(dicts):
    char_dicts = []

    for char in dicts:
        if char.isalpha():
          count = dicts[char]
          char_dicts.append({"char": char, "num": count})
    
    # sort them
    char_dicts.sort(reverse=True, key=sort_on)
    return char_dicts

