def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_path):
    with open(file_path) as f:
        document_text = f.read()
    word_count = len(document_text.split())
    return word_count