from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def draw(self, style, icon_family, prefix='', is_last=False):
        pass

class Leaf(Component):
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def draw(self, style, icon_family, prefix='', is_last=False):
        icon = icon_family.get_leaf_icon()
        return style.render_leaf(self, icon, prefix, is_last)

class Container(Component):
    def __init__(self, name, level=0):
        self.name = name
        self.level = level
        self.children = []

    def add(self, component):
        self.children.append(component)
        
    def draw(self, style, icon_family, prefix='', is_last=False):
        icon = icon_family.get_container_icon()
        return style.render_container(self, icon, prefix, icon_family, is_last)
