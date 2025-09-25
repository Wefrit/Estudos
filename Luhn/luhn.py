class Luhn:
    def __init__(self, card_num):
        pass

    def valid(self):
        pass


card_num = "4539 3195 0343 6467"
card_num = card_num.replace(" ", "")
luhn = []
for i, d in enumerate(reversed(card_num)):
    n = int(d)
    if i % 2 == 1:  # "posição ímpar" a partir da direita
        n *= 2
        if n > 9:
            n -= 9
    luhn.append(n)
print(sum(luhn))