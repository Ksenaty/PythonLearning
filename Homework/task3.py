class Worker:
    name = ""
    lastname = ""
    position = ""
    _income = {}


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя сотрудника {self.name}, {self.lastname}")

    def get_total_income(self):
        print(f"Зарплата сотрудника {self._income['wage'] + self._income['bonus']}")


a = Position()
a.name = "Yaroslav"
a.lastname = "Bond"
a._income = {"wage": 50000, "bonus": 3500}
a.get_full_name()
a.get_total_income()
