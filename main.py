def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    reports = report(num_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in reports:
        print(f"{item[0]} character was found {item[1]} times")
    print("---End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    low_words = text.lower()
    letter_dic = {}
    for char in low_words:
        if char in letter_dic:
            letter_dic[char] += 1
        else:
            letter_dic[char] = 1
    return letter_dic

def report(dic):
    new_list = []
    for key, val in dic.items():
        new_list.append([key, val])
    def sort_on(list):
        return list[1]
    new_list.sort(reverse=True, key=sort_on)
    sorted_alpha_list=[]
    for i in range(len(new_list)):
        isalpha = new_list[i][0].isalpha()
        if isalpha == True:
            sorted_alpha_list.append(new_list[i])
    return sorted_alpha_list
        


main()