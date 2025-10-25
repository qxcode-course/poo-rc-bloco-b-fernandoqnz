class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def usagePerSheet(self) -> int:
        gasto = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}
        return gasto.get(self.hardness, 1)

    def __str__(self):
        return f"[{self.thickness}:{self.hardness}:{self.size}]"


class Pencil:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.tip = None

    def hasGrafite(self) -> bool:
        return self.tip is not None

    def insert(self, lead: Lead):
        if lead.thickness != self.thickness:
            print("fail: calibre incompativel")
            return
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return
        self.tip = lead

    def remove(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return None
        self.tip = None

    def writePage(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return
        gasto = self.tip.usagePerSheet()

        if self.tip.size <= 10:
            print("fail: tamanho insuficiente")
            return

        if self.tip.size - gasto < 10:
            self.tip.size = 10
            print("fail: folha incompleta")
            return

        self.tip.size -= gasto

    def __str__(self):
        grafite = str(self.tip) if self.tip else "null"
        return f"calibre: {self.thickness}, grafite: {grafite}"


def main():
    pencil = None
    while True:
        line = input().strip()
        if line == "":
            continue
        print(f"${line}")  # imprime o $ antes do comando
        cmd = line.split()

        if cmd[0] == "end":
            break
        elif cmd[0] == "init":
            pencil = Pencil(float(cmd[1]))
        elif cmd[0] == "insert":
            lead = Lead(float(cmd[1]), cmd[2], int(cmd[3]))
            pencil.insert(lead)
        elif cmd[0] == "remove":
            pencil.remove()
        elif cmd[0] == "write":
            pencil.writePage()
        elif cmd[0] == "show":
            print(pencil)
        else:
            print("fail: comando invalido")




if __name__ == "__main__":
    main()
