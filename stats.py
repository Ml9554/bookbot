def get_num_words(text):
        num_count = text.split()
        num_words = len(num_count)
        return num_words

def character_count(text):
        lower_content = text.lower()
        counts = {}
        for character in lower_content:
            if character in counts:
                counts[character] = counts[character] + 1
            else:
                counts[character] = 1
        return counts