class Worker:

  def __init__(self, name, surname, position, wage, bonus):
    self.name = name
    self.surname = surname
    self.position = position
    self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
  def __init__(self, name, surname, position, wage, bonus):
    super().__init__(name, surname, position, wage, bonus)
  def get_full_name(self, name, surname):
    self.name = name
    self.surname = surname
    print(f'Полное имя: {self.name} {self.surname}')
  def get_total_income(self, _income):
    self.income = _income
    a = self._income.get("wage")
    b = self._income.get("bonus")
    _income = a + b
    print(_income)

worker1 = Position('Peter', 'Popov', 'manager', 25000, 5000)
print(worker1.get_full_name)
print(worker1.position)
print(worker1.get_total_income)



# worker1 = Position()
# print(Position.get_full_name)

