def line_up(name, number):
    ordinal = 'th'

    str_number = str(number)
    if str_number[-1:] == '1' and str_number[-2:] != '11':
        ordinal = 'st'
    if str_number[-1:] == '2' and str_number[-2:] != '12':
        ordinal = 'nd'
    if str_number[-1:] == '3' and str_number[-2:] != '13':
        ordinal = 'rd'

    return f'{name}, you are the {number}{ordinal} customer we serve today. Thank you!'


print(line_up('Mary', 162))

