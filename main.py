from stats import get_num_words, character_count, sort_on, dictionary_sort

path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    text = get_book_text(path)
    
    word_count = get_num_words(text)
    

    char_count = character_count(text)
    

    dict_sort = dictionary_sort(char_count)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...") 
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for item in dict_sort:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue

    print("============= END ===============")

main()