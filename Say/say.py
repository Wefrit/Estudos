names = {
    "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
    "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten", "11": "eleven",
    "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen", "16": "sixteen",
    "17": "seventeen", "18": "eighteen", "19": "nineteen", "20": "twenty", "30": "thirty",
    "40": "forty", "50": "fifty", "60": "sixty", "70": "seventy", "80": "eighty", "90": "ninety"
}

scales = ["", "thousand", "million", "billion"]

def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return names["0"]
    
    def three_digits_to_words(n):
        words = []
        hundred = n // 100
        rest = n % 100
        
        if hundred:
            words.append(names[str(hundred)])
            words.append("hundred")
        
        if rest:  # só processa o resto se não for zero
            if rest < 20:
                words.append(names[str(rest)])
            else:
                dozen = rest // 10 * 10
                unity = rest % 10
                if unity:
                    words.append(names[str(dozen)] + "-" + names[str(unity)])
                else:
                    words.append(names[str(dozen)])
        
        return " ".join(words)
    
    parts = []
    scale_index = 0
    
    while number > 0:
        n = number % 1000
        if n:
            part = three_digits_to_words(n)
            if scales[scale_index]:
                part += " " + scales[scale_index]
            parts.append(part)
        number //= 1000
        scale_index += 1
    
    return " ".join(reversed(parts))
