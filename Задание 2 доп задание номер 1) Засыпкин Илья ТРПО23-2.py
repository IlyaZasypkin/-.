from num2words import num2words

def calc(expression):
    parts = expression.split("разделить на")
    dividend = parts[0]
    divisor = parts[1]

    dividend_number = float(num2words(dividend, lang='ru').replace(' и ', ' ').replace(' ', ''))
    divisor_number = float(num2words(divisor, lang='ru').replace(' и ', ' ').replace(' ', ''))

    result = dividend_number / divisor_number
    result_words = num2words(round(result, 3), lang='ru')

    return result_words.replace(' и ', ' ').replace(' ', ' ')

print(calc("сорок один и тридцать одна сотая разделить на семнадцать"))  # вывод: "два и сорок три сотых"
