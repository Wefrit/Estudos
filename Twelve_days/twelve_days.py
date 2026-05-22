days = [
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
]

gifts = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming"
]


def recite(start_verse, end_verse):
    verses = []
    for n in range(start_verse, end_verse + 1):
        verse = f"On the {days[n-1]} day of Christmas my true love gave to me: "
        presents = []
        for i in range(n, 0, -1):
            if i == 1 and n > 1:
                presents.append("and " + gifts[0])
            else:
                presents.append(gifts[i-1])
        verses.append(verse + ", ".join(presents))
    return verses
