class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        print(f'Информация о транспортном средстве', f'Марка: {self.make}', f'Модель: {self.model}', sep='\n')

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        base_info = super().get_info()
        print(base_info, f'Тип топлива: {self.fuel_type}', sep='\n')
