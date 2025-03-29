from stats import get_num_words, get_book_text
def main():
    # print(get_book_text('./books/frankenstein.txt'))
    full_text = get_book_text('./books/frankenstein.txt')
    doc_word_count = get_num_words(full_text)
    print(f'{doc_word_count} words found in the document')


main()