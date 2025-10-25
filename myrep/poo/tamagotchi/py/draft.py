class Tamagochi:
    def __init__(self, energyMax: int, cleanMax: int):
        self.energyMax = energyMax
        self.cleanMax = cleanMax
        self.energy = energyMax
        self.clean = cleanMax
        self.age = 0
        self.alive = True

    def set_energy(self, value: int):
        if not self.alive:
            return
        self.energy = max(0, min(self.energyMax, value))
        if self.energy == 0:
            self.alive = False
            print("fail: pet morreu de fraqueza")

    def set_clean(self, value: int):
        if not self.alive:
            return
        self.clean = max(0, min(self.cleanMax, value))
        if self.clean == 0:
            self.alive = False
            print("fail: pet morreu de sujeira")

    def set_age(self, value: int):
        if not self.alive:
            return
        self.age = max(0, value)

    def is_alive(self):
        return self.alive


class Game:
    def __init__(self):
        self.pet = None

    def init_pet(self, energyMax: int, cleanMax: int):
        self.pet = Tamagochi(energyMax, cleanMax)
        print(f"$init {energyMax} {cleanMax}")

    def show(self):
        p = self.pet
        print("$show")
        print(f"E:{p.energy}/{p.energyMax}, L:{p.clean}/{p.cleanMax}, I:{p.age}")

    def play(self):
        p = self.pet
        print("$play")
        if not p.alive:
            print("fail: pet esta morto")
            return
        p.set_energy(p.energy - 2)
        p.set_clean(p.clean - 3)
        p.set_age(p.age + 1)

    def sleep(self):
        p = self.pet
        print("$sleep")
        if not p.alive:
            print("fail: pet esta morto")
            return
        if p.energy > p.energyMax - 5:
            print("fail: nao esta com sono")
            return
        missing_energy = p.energyMax - p.energy
        p.set_energy(p.energyMax)
        p.set_age(p.age + missing_energy)

    def shower(self):
        p = self.pet
        print("$shower")
        if not p.alive:
            print("fail: pet esta morto")
            return
        p.set_energy(p.energy - 3)
        p.set_clean(p.cleanMax)
        p.set_age(p.age + 2)


def main():
    game = Game()
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            continue
        if line == "end":
            print("$end")
            break
        cmd = line.split()
        if cmd[0] == "init":
            game.init_pet(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "show":
            game.show()
        elif cmd[0] == "play":
            game.play()
        elif cmd[0] == "sleep":
            game.sleep()
        elif cmd[0] == "shower":
            game.shower()
        else:
            print("fail: comando invalido")


if __name__ == "__main__":
    main()
