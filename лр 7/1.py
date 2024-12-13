class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"ID сотрудника: {self.id}, Имя: {self.name}"


class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self, project_name):
        return f"Менеджер {self.name} управляет проектом {project_name}"

    def get_info(self):
        return f"{Employee.get_info(self)}, Отдел: {self.department}"


class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} - специализация - {self.specialization}"

    def get_info(self):
        return f"{Employee.get_info(self)}, Специализация: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return f"У технического менеджера {self.name} нет людей в команде."
        info = f"Команда технического менеджера {self.name}:\n"
        for emp in self.team:
            info += f"  - {emp.get_info()}\n"
        return info

    def get_info(self):
        return f"{Manager.get_info(self)}, Специализация: {self.specialization}"


emp1 = Employee('Иванов Пётр', 100)
manager = Manager('Сидоров Иван', 101, 'ИТ')
tech = Technician('Петров Алексей', 102, 'Кибербезопасность')
tech_manager = TechManager('Измайлов Сергей', 103, 'ИТ', 'Разработка системных приложений')

print(emp1.get_info())
print(manager.get_info())
print(manager.manage_project("Дизайн сайтов"))
print(tech.perform_maintenance())
print(tech_manager.get_info())

tech_manager.add_employee(emp1)
tech_manager.add_employee(manager)
tech_manager.add_employee(tech)
print(tech_manager.get_team_info())
