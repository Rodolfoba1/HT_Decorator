from fighter import Fighter


class Batman(Fighter):

    def __init__(self, hp: float, attack: float, defence: float, speed: float):
        self.__hp: float = hp
        self.__attack: float = attack
        self.__defence: float = defence
        self.__speed: float = speed

    def get_speed(self) -> float:
        return self.__speed

    def get_attack(self) -> float:
        return self.__attack

    def get_defence(self) -> float:
        return self.__defence

    def get_hp(self) -> float:
        return self.__hp

    def reduce_hp(self, damage: float):
        self.__hp = self.__hp - damage

    def compute_damage(self, enemy: Fighter) -> float:
        damage: float = enemy.get_attack()
        return damage
