def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    print_report(book_path, word_count, char_count)   

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    letters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
    letter_counts = {}
    word_list = book_text.split()
    for word in word_list:
        lowered_string = word.lower()
        for char in lowered_string:
            if char in letters:
                if char not in letter_counts:
        
                    letter_counts[char] = 0
                letter_counts[char] += 1
    return letter_counts

def sort_on(dict):
    return dict["num"]

def print_report(path, words, chars):
    list_char_dictionaries = []
    for char in chars:
        list_char_dictionaries.append({"name": char, "num": chars[char]})
    list_char_dictionaries.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()
    for i in range(len(list_char_dictionaries)):
        print(f"The '{list_char_dictionaries[i]["name"]}' character was found {list_char_dictionaries[i]["num"]} times")
    print("--- End report ---")
 
 

main()