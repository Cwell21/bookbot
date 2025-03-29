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


