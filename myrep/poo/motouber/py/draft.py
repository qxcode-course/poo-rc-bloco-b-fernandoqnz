class Pessoa:
    def __init__(self, name: str, money: int):
        self.__name = name
        self.__money = money

    def getName(self) -> str:
        return self.__name

    def getMoney(self) -> int:
        return self.__money

    def pay(self, amount: int) -> int:
        if self.__money >= amount:
            self.__money -= amount
            return amount
        else:
            paid = self.__money
            self.__money = 0
            return paid

    def receive(self, amount: int):
        self.__money += amount

    def __str__(self):
        return f"{self.__name}:{self.__money}"


class Moto:
    def __init__(self):
        self.__cost = 0
        self.__driver = None
        self.__passenger = None

    def setDriver(self, name: str, money: int):
        self.__driver = Pessoa(name, money)

    def setPassenger(self, name: str, money: int):
        if self.__driver is None:
            print("fail: no driver")
            return
        self.__passenger = Pessoa(name, money)

    def drive(self, km: int):
        if self.__passenger is None:
            print("fail: no passenger")
            return
        self.__cost += km

    def leavePassenger(self):
        if self.__passenger is None:
            print("fail: no passenger")
            return
        passenger = self.__passenger
        driver = self.__driver
        amount = self.__cost
        paid = passenger.pay(amount)
        if paid < amount:
            print("fail: Passenger does not have enough money")
            driver.receive(amount)
        else:
            driver.receive(paid)
        print(f"{passenger.getName()}:{passenger.getMoney()} left")
        self.__passenger = None
        self.__cost = 0

    def __str__(self):
        driver_str = str(self.__driver) if self.__driver else "None"
        passenger_str = str(self.__passenger) if self.__passenger else "None"
        return f"Cost: {self.__cost}, Driver: {driver_str}, Passenger: {passenger_str}"


def main():
    moto = Moto()
    while True:
        line = input().strip()
        if line == "":
            continue
        print(f"${line}")
        cmd = line.split()

        if cmd[0] == "end":
            break
        elif cmd[0] == "show":
            print(moto)
        elif cmd[0] == "setDriver":
            moto.setDriver(cmd[1], int(cmd[2]))
        elif cmd[0] == "setPass":
            moto.setPassenger(cmd[1], int(cmd[2]))
        elif cmd[0] == "drive":
            moto.drive(int(cmd[1]))
        elif cmd[0] == "leavePass":
            moto.leavePassenger()
        else:
            print("fail: invalid command")


if __name__ == "__main__":
    main()
