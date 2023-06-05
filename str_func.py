def big_letter(smal_string):

    """функция  принимает на вход строку
    и возвращает ее со всеми заглавными буквами """

    big = smal_string.upper()

    return big

def cap_letter(big_string):


    string_list = big_string.split(" ")
    new_list = []
    for item in string_list:
        new_list.append(item.capitalize())
    new_str = ' '.join(new_list)
    return new_str




