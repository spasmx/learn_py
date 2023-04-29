class Employee:

    def __init__(self, first_name: str, last_name: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.year_salary = salary

    def give_raise(self, salary_increase: int = None):
        if salary_increase:
            self.year_salary += salary_increase
        else:
            self.year_salary += 5000
