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


def print_report(char_count, file_path, word_count):
    
    char_count_list = []

    for ch in char_count:
        char_count_list.append({'char': ch, 'number': char_count[ch]})
    
    char_count_list.sort(key=lambda x: x['number'], reverse=True)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count -----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char in char_count_list:
        if not char['char'].isalpha():
            continue
        print(f'{char["char"]}: {char["number"]}')
    print('============= END ===============')
    return