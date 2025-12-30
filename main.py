from stats import get_num_words, character_count

path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    text = get_book_text(path)
    
    word_count = get_num_words(text)
    print(word_count)

    char_count = character_count(text)
    print(char_count)

main()