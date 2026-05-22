import re
class PhoneNumber:
    def __init__(self, number):
        raw = str(number)

        if any(ch.isalpha() for ch in raw):
            raise ValueError("letters not permitted")

        allowed = set("0123456789-+(). ")
        if any(ch not in allowed for ch in raw):
            raise ValueError("punctuations not permitted")

        digits = re.sub(r"\D", "", raw)

        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")

        if len(digits) == 11:
            if digits[0] != "1":
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]

        area_code = digits[0]
        exchange_code = digits[3]
        if area_code == "0":
            raise ValueError("area code cannot start with zero")
        if area_code == "1":
            raise ValueError("area code cannot start with one")
        if exchange_code == "0":
            raise ValueError("exchange code cannot start with zero")
        if exchange_code == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = digits
        self.area_code = digits[:3]

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
