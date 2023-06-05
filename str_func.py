def big_letter(smal_string):



    big = smal_string.upper()

    return big

def cap_letter(big_string):
""" делает заглавными первые буквы каждого слова в строке, поступившей на вход функции
"""

    string_list = big_string.split(" ")
    new_list = []
    for item in string_list:
        new_list.append(item.capitalize())
    new_str = ' '.join(new_list)
    return new_str




