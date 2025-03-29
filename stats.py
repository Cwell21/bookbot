def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(document_text):
    if isinstance(document_text, str):
        word_count = len(document_text.split())
    else:
        raise ValueError('Input must be a string')
    return word_count

def get_char_count(document_text):
    char_count = {}

    if isinstance(document_text, str):
        words = document_text.split()
        for word in words:
            for char in word:

                char = char.lower()

                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1    
    else:
        raise ValueError('Input must be a string')


    return char_count

