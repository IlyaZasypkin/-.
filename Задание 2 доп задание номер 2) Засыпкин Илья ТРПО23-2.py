def calc(fraction_str):
    parts = fraction_str.split('разделить на')
    numerator = float(sum(map(lambda x: int(x), parts[0].split(' и ')))
    denominator = float(sum(map(lambda x: int(x), parts[1].split(' ')))

    result = numerator / denominator
    result_str = str(result - int(result))[2:]

    period = ''
    for i in range(1, 5):
        if result_str[:i] == result_str[i:i*2]:
            period = result_str[:i]
            break

    if period:
        return f"ноль и {result_str[:i]} в периоде"
    else:
        return f"ноль и {result_str} без периода"
