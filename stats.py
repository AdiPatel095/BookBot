def num_words(text):
    return len(text.split())

def count_characters(text):
    char_counts = {}
    for char in text:
        if char.lower() in char_counts:
            char_counts[char.lower()] += 1
        else:
            char_counts[char.lower()] = 1
    return char_counts

def sort_dict(char_counts):
    return sorted(char_counts.items(), key=lambda x: x[1], reverse=True)