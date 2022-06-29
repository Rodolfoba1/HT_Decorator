from fighter import Fighter

class Batman(Fighter):
    def __init__(self, hp: float, attack: float, defence: float, speed: float):
        self.__hp: float = hp
        self.__attack: float = attack
        self.__defence: float = defence
        self.__speed: float = speed

    def get_speed(self) -> float:
        pass

    def get_attack(self) -> float:
        pass

    def get_defence(self) -> float:
        pass

    def get_hp(self) -> float:
        pass

    def reduce_hp(self, damage: float):
        pass

    def compute_damage(self, enemy: Fighter) -> float:
        pass



