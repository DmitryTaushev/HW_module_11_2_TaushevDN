from abc import ABC, abstractmethod

class Pasta(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_filling(self):
        pass

    @abstractmethod
    def get_additions(self):
        pass

class Bolognese(Pasta):
    def get_type(self):
        return "Спагетти"

    def get_sauce(self):
        return "Томатный соус"

    def get_filling(self):
        return "Мясной фарш"

    def get_additions(self):
        return "Пармезан"

class Carbonara(Pasta):
    def get_type(self):
        return "Тальятеле"

    def get_sauce(self):
        return "Сливочный соус"

    def get_filling(self):
        return "Бекон"

    def get_additions(self):
        return "Помидоры черри"

class Penne_with_beef(Pasta):
    def get_type(self):
        return "Пенне"

    def get_sauce(self):
        return "Томатный соус"

    def get_filling(self):
        return "Говядина"

    def get_additions(self):
        return "Пармезан"

# Фабрика для создания пасты
class FactoryPasta:

    @staticmethod
    def make_pasta(pasta):
        if pasta == "bolognese":
            return Bolognese()
        elif pasta == "carbonara":
            return Carbonara()
        elif pasta == "penne with beef":
            return Penne_with_beef()
        else:
            raise ValueError("Unknown pasta type")


if __name__ == "__main__":
    pasta_type = input("Введите тип пасты (bolognese,carbonara,penne with beef): ")
    pasta = FactoryPasta.make_pasta(pasta_type)

    print(pasta.get_type())
    print(pasta.get_sauce())
    print(pasta.get_filling())
    print(pasta.get_additions())
