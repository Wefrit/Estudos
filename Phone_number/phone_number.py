import re
import string
class PhoneNumber:
    def __init__(self, number):
        self.number = str(number)
        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(self.number) == 11 and self.number[0] != "1":
            raise ValueError("11 digits must start with 1")
        if self.number[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        if len(self.number) != 11 and self.number[0] == "1":
            raise ValueError("exchange code cannot start with one")
        if self.number[3] == "0":
            raise ValueError("area code cannot start with zero")
        if self.number[3] == "1":
            raise ValueError("area code cannot start with one")
        if any(ch in string.punctuation for ch in self.number):
            raise ValueError("punctuations not permitted")
        if  any(lt in string.ascii_letters for lt in self.number):
            raise ValueError("letters not permitted")

numero = PhoneNumber('6139950253')