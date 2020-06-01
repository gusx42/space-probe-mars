import core


class Probe():

    horizontal_postion = 0
    vertical_position = 0
    side = 'N'

    def __move_forward(self, moviment):

        if self.side == 'N':
            self.horizontal_postion += 1
        elif self.side == 'W':
            self.vertical_position += 1
        elif self.side == "S":
            self.horizontal_postion -= 1
        elif self.side == 'E':
            self.vertical_position -= 1

    def __rote(self, command):

        moviments = {
            "N": {"L": "W", "R": "E"},
            "W": {"L": "S", "R": "N"},
            "S": {"L": "E", "R": "W"},
            "E": {"L": "N", "R": "S"}
        }

        self.side = moviments.get(self.side).get(command, "Wrong moviment")

    def imput_receiver(self, command):
        if command == "M":
            self.__move_forward(command)
        elif command == "L" or command == "R":
            self.__rote(command)

        postion = {
            'horizontal_postion': self.horizontal_postion,
            'vertical_position': self.vertical_position,
            'side': self.side
        }

        return postion


if __name__ == "__main__":

    side = ""
    probe = Probe()

    while side != "exit":
        side = input("moviment? ")
        print(probe.imput_receiver(side))
