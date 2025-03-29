from stats import get_num_words, get_book_text, get_char_count, print_report
def main():
    book_to_analyze = 'frankenstein'
    file_path = f'./books/{book_to_analyze}.txt'
    # print(get_book_text(file_path))

    full_text = get_book_text(file_path)
    
    doc_word_count = get_num_words(full_text)
    char_count = get_char_count(full_text)

    # print(f'{doc_word_count} words found in the document')
    # print(char_count)
    print_report(char_count, file_path, doc_word_count)

main()