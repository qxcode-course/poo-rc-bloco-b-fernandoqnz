class Pessoa:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def getName(self) -> str:
        return self.__name

    def getAge(self) -> int:
        return self.__age

    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"


class Motoca:
    def __init__(self, power: int = 1):
        self.power = power
        self.time = 0
        self.person: Pessoa | None = None

    def inserir(self, person: Pessoa) -> bool:
        if self.person is not None:
            print("fail: busy motorcycle")
            return False
        self.person = person
        return True

    def remover(self) -> Pessoa | None:
        if self.person is None:
            print("fail: empty motorcycle")
            return None
        temp = self.person
        self.person = None
        return temp

    def buyTime(self, time: int):
        self.time += time

    def drive(self, time: int):
        if self.time <= 0:
            print("fail: buy time first")
            return
        if self.person is None:
            print("fail: empty motorcycle")
            return
        if self.person.getAge() > 10:
            print("fail: too old to drive")
            return
        if time > self.time:
            print(f"fail: time finished after {self.time} minutes")
            self.time = 0
        else:
            self.time -= time

    def honk(self) -> str:
        return "P" + ("e" * self.power) + "m"

    def __str__(self) -> str:
        person_str = str(self.person) if self.person else "empty"
        return f"power:{self.power}, time:{self.time}, person:({person_str})"


def main():
    moto = Motoca()
    while True:
        line = input().strip()
        if line == "":
            continue
        print(f"${line}")
        args = line.split()
        cmd = args[0]
        if cmd == "end":
            break
        elif cmd == "show":
            print(moto)
        elif cmd == "init":
            power = int(args[1]) if len(args) > 1 else 1
            moto = Motoca(power)
        elif cmd == "enter":
            if len(args) < 3:
                print("fail: missing arguments")
                continue
            nome, idade = args[1], int(args[2])
            moto.inserir(Pessoa(nome, idade))
        elif cmd == "leave":
            p = moto.remover()
            if p:
                print(p)
        elif cmd == "buy":
            if len(args) < 2:
                print("fail: missing time")
                continue
            moto.buyTime(int(args[1]))
        elif cmd == "drive":
            if len(args) < 2:
                print("fail: missing time")
                continue
            moto.drive(int(args[1]))
        elif cmd == "honk":
            print(moto.honk())
        else:
            print("fail: invalid command")


if __name__ == "__main__":
    main()
