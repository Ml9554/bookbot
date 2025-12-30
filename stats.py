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

def sort_on(counts):
      return counts["num"]

def dictionary_sort(counts):
      list_of_char_counts = []
      for char, count in counts.items():
            list_of_char_counts.append({"char": char, "num": count})
    
      list_of_char_counts.sort(reverse=True, key=sort_on)
      return list_of_char_counts
      