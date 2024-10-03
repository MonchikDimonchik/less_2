import random

# Базовый класс Person
class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    # Простой метод для подсчета урона с учетом брони противника
    def __calculate_damage(self, enemy, random_damage):
        reduced_damage = random_damage - enemy.armor  # Урон уменьшается на значение брони
        return max(0, reduced_damage)  # Урон не может быть отрицательным

    # Метод атаки, который вызывает упрощенный метод подсчета урона
    def attack(self, enemy):
        random_damage = random.randint(0, self.damage)  # Генерация случайного урона от 0 до максимального
        damage_dealt = self.__calculate_damage(enemy, random_damage)
        enemy.health -= damage_dealt
        print(f"{self.__class__.__name__} атакует {enemy.__class__.__name__} и наносит {damage_dealt:.2f} урона.")
        print(f"Здоровье {enemy.__class__.__name__}: {enemy.health:.2f}")
        if enemy.health <= 0:
            print(f"{enemy.__class__.__name__} был побеждён!")


# Класс Player, наследник Person
class Player(Person):
    def __init__(self, health=100, damage=20, armor=10):
        super().__init__(health, damage, armor)


# Класс Enemy, наследник Person
class Enemy(Person):
    def __init__(self, health=100, damage=20, armor=9):
        super().__init__(health, damage, armor)


# Класс для проведения боя
class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print("Бой начинается!")
        while self.player.health > 0 and self.enemy.health > 0:
            # Случайный выбор, кто атакует первым
            if random.choice([True, False]):
                self.player.attack(self.enemy)
                if self.enemy.health > 0:
                    self.enemy.attack(self.player)
            else:
                self.enemy.attack(self.player)
                if self.player.health > 0:
                    self.player.attack(self.enemy)

        if self.player.health > 0:
            print("Игрок победил!")
        else:
            print("Враг победил!")


# Пример использования
player = Player()
enemy = Enemy()

game = Game(player, enemy)
game.start_battle()