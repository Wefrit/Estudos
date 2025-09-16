names = {"0" : "zero", "1": "one", "2" : "two", "3" : "three", "4" : "four", "5" : "five", 
         "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine", "10" : "ten", "11" : "eleven", 
         "12" : "twelve", "13" : "thirteen", "14" : "fourteen", "15" : "fifteen", "16" : "sixteen",
        "17" : "seventeen", "18" : "eighteen", "19" : "nineteen", "20" : "twenty", "30": "thirty", 
        "40" : "forty", "50" : "fifty", "60" : "sixty", "70" : "seventy", "80" : "eighty", "90" : "ninety"}



def say(number):
    dozen = (number // 10)
    hundred = (number // 100)
    thousand = (number // 1_000) * 1_000
    million = (number // 1_000_000) * 1_000_000
    billion = (number // 1_000_000_000) * 1_000_000_000
    str_number = str(number)
    if len(str_number) <= 2 and number <= 20:
        print(names[str_number])
    if 20 < number < 100:
        print(names[str(dozen * 10)], names[str_number[-1]])
    if 100 <= number <= 999:
        print(names[str(hundred * 100)[0]], "hundred", names[number % 10])
    


print (say(202))
