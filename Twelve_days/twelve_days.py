verses = {12 : "twelve Drummers Drumming, ", 11 : "eleven Pipers Piping, ", 10 : "ten Lords-a-Leaping, ",
          9 : "nine Ladies Dancing, ", 8 : "eight Maids-a-Milking, ",
          7 : "seven Swans-a-Swimming, ", 6 : "six Geese-a-Laying, ", 5 : "five Gold Rings, ", 4 : "four Calling Birds, ",
          3 : "three French Hens, ", 2 : "two Turtle Doves ", 1 : "and a Partridge in a Pear Tree."}

day = {2 : "second", 3 : "third", 4 : "fifth", 6 : "sixth", 7 : "seventh", 
       8 : "eight", 9 : "ninth", 10 : "tenth", 11 : "eleventh", 12 : "twelfth" }

def recite(start_verse, end_verse):
    if end_verse == 1:
        return "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."
    else:
        return [f"On the {day[end_verse]} day of Christmas my true love gave to me: "  + " ".join(verses[verse] for verse in range(end_verse, start_verse - 1, -1))]
    

print(recite(2,2))