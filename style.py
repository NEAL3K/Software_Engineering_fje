from abc import ABC, abstractmethod


class Style(ABC):
    @abstractmethod
    def render_container(self, container, icon, prefix, icon_family, is_last):
        pass

    @abstractmethod
    def render_leaf(self, leaf, icon, prefix, is_last):
        pass


class TreeStyle(Style):
    def render_container(self, container, icon, prefix, icon_family, is_last):
        # 构建当前容器节点的字符串表示
        result = f"{prefix}{'└─' if is_last else '├─'} {icon} {container.name}\n"
        for i, child in enumerate(container.children):
            # 根据是否是最后一个子节点选择不同的前缀
            new_prefix = prefix + ("    " if is_last else "│   ")
            # 递归渲染子节点
            result += child.draw(
                self, icon_family, new_prefix, i == len(container.children) - 1
            )
        return result

    def render_leaf(self, leaf, icon, prefix, is_last):
        # 构建叶子节点的字符串表示
        result = (
            f"{prefix}{'└─' if is_last else '├─'} {icon} {leaf.name}: {leaf.value}\n"
            if leaf.value is not None
            else f"{prefix}{'└─' if is_last else '├─'} {icon} {leaf.name}\n"
        )
        return result


class RectangleStyle(Style):
    def render_container(self, container, icon, prefix, icon_family, is_last):
        level = len(prefix) // 3  # 计算当前层级
        firstline = (
            "─" * (64 - len(f"{prefix}┌─ {icon} {container.name}") - level)
            + "┐"
            + "│" * level
        )
        result = f"{prefix}┌─ {icon} {container.name} {firstline}\n"
        for i, child in enumerate(container.children):
            new_prefix = prefix + "│  "
            result += child.draw(
                self, icon_family, new_prefix, i == len(container.children) - 1
            )
        lastline = "└" + "─" * (64 - len(f"{prefix}") - level) + "┘" + "│" * level
        result += f"{prefix}{lastline}\n"
        return result

    def render_leaf(self, leaf, icon, prefix, is_last):
        Leaf_Result = (
            f"{prefix}├─ {icon} {leaf.name}: {leaf.value} "
            if leaf.value is not None
            else f"{prefix}├─ {icon} {leaf.name} "
        )
        if is_last:
            Leaf_Result = Leaf_Result.replace("├─", "└─")
        level = len(prefix) // 3  # 计算当前层级
        return (
            Leaf_Result + "─" * (64 - len(Leaf_Result) - level + 2) + "│" * level + "\n"
        )


class StyleFactory(ABC):
    @abstractmethod
    def create_style(self):
        pass


class TreeStyleFactory(StyleFactory):
    def create_style(self):
        return TreeStyle()


class RectangleStyleFactory(StyleFactory):
    def create_style(self):
        return RectangleStyle()
