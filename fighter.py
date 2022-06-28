from abc import ABCMeta, abstractmethod
from __future__ import annotations

class Fighter(metaclass=ABCMeta):
    @abstractmethod
    def get_speed(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_attack(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_defence(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_hp(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def reduce_hp(self, damage: float):
        raise NotImplementedError

    @abstractmethod
    def compute_damage(self, enemy: Fighter) -> float:
        raise NotImplementedError
