from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def floor_preparation(self):
        pass

    @abstractmethod
    def laying_tiles(self):
        pass

    @abstractmethod
    def apply_putty(self):
        pass

    @abstractmethod
    def plaster_the_walls(self):
        pass

    @abstractmethod
    def prime_the_wall(self):
        pass

    @abstractmethod
    def paint_the_wall(self):
        pass

    @abstractmethod
    def make_floors(self):
        pass

    @abstractmethod
    def align_the_walls(self):
        pass

    @abstractmethod
    def paint_the_walls(self):
        pass

    @abstractmethod
    def get_turnkey_work(self):
        pass


class TilerBuilder(Builder):

    def floor_preparation(self):
        print(f"Подготовка пола.")

    def laying_tiles(self):
        print(f"Укладка плитки.")


    def apply_putty(self):
        pass


    def plaster_the_walls(self):
        pass


    def prime_the_wall(self):
        pass


    def paint_the_wall(self):
        pass


    def make_floors(self):
        pass


    def align_the_walls(self):
        pass


    def paint_the_walls(self):
        pass


    def get_turnkey_work(self):
        pass



class FinisherBuilder(Builder):

    def apply_putty(self):
        print(f"Нанесли шпатлевку.")

    def plaster_the_walls(self):
        print(f"Отштукатурили стену.")


    def floor_preparation(self):
        pass


    def laying_tiles(self):
        pass


    def prime_the_wall(self):
        pass


    def paint_the_wall(self):
        pass


    def make_floors(self):
        pass


    def align_the_walls(self):
        pass


    def paint_the_walls(self):
        pass


    def get_turnkey_work(self):
        pass



class PainterBuilder(Builder):

    def prime_the_wall(self):
        print(f"Загрунтовали стену.")

    def paint_the_wall(self):
        print(f"Покрасили стену.")

    def floor_preparation(self):
        pass

    def laying_tiles(self):
        pass

    def apply_putty(self):
        pass

    def plaster_the_walls(self):
        pass


    def make_floors(self):
        pass

    def align_the_walls(self):
        pass

    def paint_the_walls(self):
        pass

    def get_turnkey_work(self):
        pass


class Director:
    def __int__(self):
        self.builder = None

    def construct_builder(self, builder):
        self.builder = builder

    def make_floors(self):
        self.builder.floor_preparation()
        self.builder.laying_tiles()
        print(f"Сделали полы.")

    def align_the_walls(self):
        self.builder.apply_putty()
        self.builder.plaster_the_walls()
        print(f"Выровнили стены.")

    def paint_the_walls(self):
        self.builder.prime_the_wall()
        self.builder.paint_the_wall()
        print(f"Покрасили стены.")

    def get_turnkey_work(self):
        self.builder.floor_preparation()
        self.builder.laying_tiles()
        self.builder.apply_putty()
        self.builder.plaster_the_walls()
        self.builder.prime_the_wall()
        self.builder.paint_the_wall()


if __name__ == '__main__':

    tiler = TilerBuilder()
    finisher = FinisherBuilder()
    painter = PainterBuilder()
    director = Director()
    director.construct_builder(tiler)
    director.get_turnkey_work()
    print()
    director.construct_builder(finisher)
    director.get_turnkey_work()
    print()
    director.construct_builder(painter)
    director.get_turnkey_work()