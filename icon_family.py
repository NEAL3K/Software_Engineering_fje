from abc import ABC, abstractmethod


class IconFamily(ABC):
    @abstractmethod
    def get_container_icon(self):
        pass

    @abstractmethod
    def get_leaf_icon(self):
        pass


class BasicIconFamily(IconFamily):
    def get_container_icon(self):
        return "●"

    def get_leaf_icon(self):
        return "○"


class PokerFaceIconFamily(IconFamily):
    def get_container_icon(self):
        return "♢"

    def get_leaf_icon(self):
        return "♤"


icon_families = {
    "basic": BasicIconFamily(),
    "poker": PokerFaceIconFamily(),
}
