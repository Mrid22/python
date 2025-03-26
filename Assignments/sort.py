words = [
    "against",
    "forms",
    "belief",
    "government",
    "democratic",
    "movement",
    "understanding",
]
sorted = False
swap_count = 0


def count_starting_letters(list_of_strings, letter):
    starting_letters = 0
    for i in list_of_strings:
        if i[0] == letter:
            starting_letters += 1
    return starting_letters


def count_ending_letters(list_of_strings, letter):
    starting_letters = 0
    for i in list_of_strings:
        if i[-1] == letter:
            starting_letters += 1
    return starting_letters

def bubble_sort(list_of_strings, swap_count):
    while True:
        swap_count = 0
        for i in  range(len(list_of_strings)-1):
            if list_of_strings[i][0]>list_of_strings[i+1][0]:
                list_of_strings[i],list_of_strings[i+1] = list_of_strings[i+1],list_of_strings[i]
                swap_count += 1
        if swap_count == 0:
            break
    return list_of_strings

def insertion_sort(list_of_strings):
    swap_letter = ""
    for i in  range(len(list_of_strings)-1):
        for j in range(len(list_of_strings)-1):
            while j<i:
                if list_of_strings[j][0]>list_of_strings[i][0]:
                    swap_letter = list_of_strings[j]
                elif list_of_strings[j][0]>list_of_strings[i][0]:
                    swap_letter,list_of_strings[i]=list_of_strings[i],swap_letter          
        return list_of_strings

        

print(insertion_sort(words))