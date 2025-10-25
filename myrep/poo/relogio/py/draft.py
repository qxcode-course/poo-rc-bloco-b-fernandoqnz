class Watch:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
        self.set(hour, minute, second)

    def set(self, hour, minute, second):
        fails = []
        if not (0 <= hour <= 23):
            fails.append("fail: hora invalida")
        else:
            self.__hour = hour
        if not (0 <= minute <= 59):
            fails.append("fail: minuto invalido")
        else:
            self.__minute = minute
        if not (0 <= second <= 59):
            fails.append("fail: segundo invalido")
        else:
            self.__second = second
        return fails

    def toString(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")

    def nextSecond(self):
        self.__second += 1
        if self.__second >= 60:
            self.__second = 0
            self.__minute += 1
            if self.__minute >= 60:
                self.__minute = 0
                self.__hour += 1
                if self.__hour >= 24:
                    self.__hour = 0


def main():
    watch = Watch()

    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            continue

        cmd = line.split()
        print(f"${line}")  

        if cmd[0] == "end":
            break
        elif cmd[0] == "show":
            watch.toString()
        elif cmd[0] in ["set", "init"]:
            h, m, s = map(int, cmd[1:])
            fails = watch.set(h, m, s)
            for f in fails:
                print(f)
        elif cmd[0] == "next":
            watch.nextSecond()
        else:
            print("fail: comando invalido")


if __name__ == "__main__":
    main()
