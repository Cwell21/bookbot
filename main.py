def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file_path):
    with open(file_path) as f:
        document_text = f.read()
    word_count = len(document_text.split())
    return word_count

def main():
    # print(get_book_text('./books/frankenstein.txt'))
    doc_word_count = get_word_count('./books/frankenstein.txt')
    print(f'{doc_word_count} words found in the document')


main()