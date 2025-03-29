from stats import get_num_words

def main():
    # print(get_book_text('./books/frankenstein.txt'))
    doc_word_count = get_num_words('./books/frankenstein.txt')
    print(f'{doc_word_count} words found in the document')


main()