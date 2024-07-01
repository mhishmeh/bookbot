

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    dictt = count_characters(text)
    final_report(dictt)

def sort_on(dict):
    return dict[1]
    
def final_report(dictt):
    filtered_dict = {k:v for k,v in dictt.items() if k.isalpha()} #dict comprehension sheesh!
    report_list = list(filtered_dict.items())
    report_list.sort(reverse=True, key=sort_on)
    for i in range(len(report_list)):
        print(f"The '{report_list[i][0]}' character was found {report_list[i][1]} times!")



def count_characters(text):
    character_dict = dict()
    real_text = text.lower()
    for character in range(len(real_text)):
        character_dict[real_text[character]] = 1 + character_dict.get(real_text[character],0)
    return character_dict




def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    counter = len(words)
    return counter
main()