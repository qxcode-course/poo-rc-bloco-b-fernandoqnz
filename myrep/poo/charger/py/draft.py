class Battery:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__charge = capacity

    def use(self, minutes: int):
        self.__charge -= minutes
        if self.__charge <= 0:
            self.__charge = 0
            return False
        return True

    def charge(self, power: int, minutes: int):
        self.__charge += power * minutes
        if self.__charge > self.__capacity:
            self.__charge = self.__capacity

    def __str__(self):
        return f"Bateria {self.__charge}/{self.__capacity}"

    def get_charge(self):
        return self.__charge

    def get_capacity(self):
        return self.__capacity


class Charger:
    def __init__(self, power: int):
        self.__power = power

    def get_power(self):
        return self.__power

    def __str__(self):
        return f"Carregador {self.__power}W"


class Notebook:
    def __init__(self):
        self.__on = False
        self.__time_on = 0
        self.__battery = None
        self.__charger = None

    def turn_on(self):
        if self.__on:
            return
        if (self.__battery and self.__battery.get_charge() > 0) or self.__charger:
            self.__on = True
        else:
            print("fail: não foi possível ligar")

    def turn_off(self):
        self.__on = False

    def use(self, minutes: int):
        if not self.__on:
            print("fail: desligado")
            return

        if self.__battery and not self.__charger:
            if not self.__battery.use(minutes):
                print("fail: descarregou")
                self.__on = False
                return

        elif self.__charger and not self.__battery:
            pass  # usa indefinidamente

        elif self.__battery and self.__charger:
            self.__battery.charge(self.__charger.get_power(), minutes)

        else:
            print("fail: sem energia")
            self.__on = False
            return

        self.__time_on += minutes

    def set_battery(self, capacity: int):
        if self.__battery is not None:
            print("fail: bateria já conectada")
            return
        self.__battery = Battery(capacity)

    def rm_battery(self):
        if self.__battery is None:
            print("fail: Sem bateria")
            return
        print(f"Removido {self.__battery.get_charge()}/{self.__battery.get_capacity()}")
        self.__battery = None
        self.__on = False

    def set_charger(self, power: int):
        if self.__charger is not None:
            print("fail: carregador já conectado")
            return
        self.__charger = Charger(power)

    def rm_charger(self):
        if self.__charger is None:
            print("fail: Sem carregador")
            return
        print(f"Removido {self.__charger.get_power()}W")
        self.__charger = None
        self.__on = False

    def show(self):
        parts = []
        if self.__on:
            parts.append(f"Notebook: ligado por {self.__time_on} min")
        else:
            parts.append("Notebook: desligado")
        if self.__charger:
            parts.append(str(self.__charger))
        if self.__battery:
            parts.append(str(self.__battery))
        print(", ".join(parts))


def main():
    nb = Notebook()

    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            continue

        print(f"${line}")
        parts = line.split()
        cmd = parts[0]

        if cmd == "end":
            break
        elif cmd == "show":
            nb.show()
        elif cmd == "turn_on":
            nb.turn_on()
        elif cmd == "turn_off":
            nb.turn_off()
        elif cmd == "use":
            nb.use(int(parts[1]))
        elif cmd == "set_charger":
            nb.set_charger(int(parts[1]))
        elif cmd == "rm_charger":
            nb.rm_charger()
        elif cmd == "set_battery":
            nb.set_battery(int(parts[1]))
        elif cmd == "rm_battery":
            nb.rm_battery()
        else:
            print("fail: comando inválido")


if __name__ == "__main__":
    main()
