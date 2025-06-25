from datetime import date


class Student:
    def __init__(self, vardas, pavarde, gimimo_data, studies):
        self.vardas = vardas.capitalize()
        self.pavarde = pavarde.capitalize()
        self.gimimo_data = gimimo_data
        self.studies = studies


date_str = "2024-12-01"
date_format = "%Y-%m-%d"

parsed_date = datetime.strptime(date_str, date_format)
now = datetime.now()

delta = now - parsed_date
print("Difference:", delta)

