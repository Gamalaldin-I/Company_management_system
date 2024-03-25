from Employee import Employee
class Volunteer(Employee):
      def __init__(self) -> None:
            super().__init__()

      def set_salary(self):
            self._salary = 500