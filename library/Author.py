class Author():
    def __init__(self, name = "", surname = "", birth_year = 0):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def _str_(self):
        return f"{self.name} {self.surname} {self.birth_year}"
