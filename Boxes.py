import random


def gen(a, b):
    return random.uniform(a, b)


class Box:
    def __init__(self):
        self.height = gen(0.1, 3.0)
        self.width = gen(0.1, 3.0)
        self.length = gen(0.1, 10.0)

        self.volume = self.height * self.width * self.length
        self.mass = self.volume * gen(1.0, 4.0)


class Carriage:
    def __init__(self):
        self.height = gen(2.0, 3.0)
        self.width = gen(2.0, 3.0)
        self.length = gen(10.0, 20.0)

        self.volume = self.height * self.width * self.length
        self.carrying = self.volume * 750

    def load(self, load, quantity):
        volume_left = self.volume
        carrying_left = self.carrying
        i = 1
        for batch in range(quantity):
            if volume_left < load.volume:
                print(f"The box {i} will not fit: box volume {load.volume}, remaining volume in the carriage {volume_left}")
                break
            if carrying_left < load.mass:
                print(f"The box {i} will not fit: box mass {load.mass}, remaining carrying in the carriage {carrying_left}")
                break
            volume_left = volume_left - load.volume
            carrying_left = carrying_left - load.mass
            print(f"""The box {i} is shipped. Box parameters: 
            height: {load.height} 
            weight: {load.width}
            length: {load.length} 
            volume: {load.volume}
            mass: {load.mass}
            Left volume in the carriage {volume_left}, left carrying in the carriage {carrying_left}""")
            i += 1


if __name__ == '__main__':
    Carriage().load(Box(), 10)
