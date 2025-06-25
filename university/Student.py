from datetime import date, datetime


class Student:
    def __init__(self, vardas, pavarde, gimimo_data: datetime, studies):
        self.vardas = vardas.capitalize()
        self.pavarde = pavarde.capitalize()
        self.gimimo_data = gimimo_data
        self.studies = studies

    def get_age(self) -> str:
        now = date.today()
        delta = now - self.gimimo_data
        days = delta.days
        years = days // 365
        months = (days % 365) // 30
        remaining_days = (days % 365) % 30
        return f"{years} metai, {months} mėnesiai, {remaining_days} dienos"

    def __str__(self) -> str:
        output = f"Studentas: {self.vardas} {self.pavarde}\n"
        output += f"Gimimo data: {self.gimimo_data.strftime('%Y-%m-%d')}\n"
        output += f"Amžius: {self.get_age()}\n"
        return output