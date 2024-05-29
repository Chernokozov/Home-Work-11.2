
def str_to_upper(string):
    """
    Функция преобразует строку к верхнему регистру.
    """
    return string.upper()


def uppercase_first_letters(input_string):
    """
    Функция преобразует каждое слово в строке, делая заглавными первые буквы.
    """
    return ' '.join(word.capitalize() for word in input_string.split())

