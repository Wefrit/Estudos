import random
import string

class Robot:
    used_names = set()

    def __init__(self):
        self.name = self._generate_name()
    
    def _generate_name(self):
        while True:
            letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
            numbers = ''.join(str(random.randint(0, 9)) for _ in range(3))
            new_name = letters + numbers

            if new_name not in Robot.used_names:
                Robot.used_names.add(new_name)
                return new_name

    def reset(self):
        self.name = self._generate_name()
