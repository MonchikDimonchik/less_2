#Игрушка
class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f"{self.toy_type} - {self.name}, Цвет: {self.color}"


class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, "Животное")


# Класс для игрушек типа Персонаж мультфильма
class CartoonCharacterToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, "Персонаж мультфильма")


#Фабрика
class ToyFactory:
    def materials(self):
        print('Закупаем материал для игрушки...')

    def make_toys(self):
        print('Шьем игрушку...')

    def paint_toys(self, color):
        print(f'Окрашиваем игрушку в цвет: {color}')

    #Создание игрушки
    def create_toy(self, name, color, toy_type):
        self.materials()
        self.make_toys()
        self.paint_toys(color)
        return Toy(name, color, toy_type)


class AdvancedToyFactory:
    def __init__(self):
        pass

    def purchase_materials(self):
        print("Закупаем материалы для игрушки...")

    def sew_toy(self):
        print("Шьем игрушку...")

    def paint_toy(self, color):
        print(f"Окрашиваем игрушку в цвет: {color}...")

    # Метод создания игрушки в зависимости от типа
    def create_toy(self, name, color, toy_type):
        self.purchase_materials()
        self.sew_toy()
        self.paint_toy(color)

        if toy_type == "Животное":
            return AnimalToy(name, color)
        elif toy_type == "Персонаж мультфильма":
            return CartoonCharacterToy(name, color)
        else:
            return f'Не известное животное {toy_type}'


advanced_factory = AdvancedToyFactory()
cartoon_character_toy = advanced_factory.create_toy('Микки Маус', 'Черный', 'Персонаж мультфильма')
animal_toy = advanced_factory.create_toy('Лев', 'Золотой', 'Животное')
any_toy = advanced_factory.create_toy('Восьмирукий', 'Зеленый', 'чупакабра')

print(animal_toy)
print(cartoon_character_toy)
print(any_toy)