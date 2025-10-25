class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: str):
        validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in validos:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return
        self.__tamanho = valor

    def show(self):
        print(f"size: ({self.__tamanho})")


def main():
    roupa = Roupa()
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
        if cmd[0] == "show":
            print(f"${line}")
            roupa.show()
        elif cmd[0] == "size":
            print(f"${line}")
            roupa.setTamanho(cmd[1])
        else:
            print(f"${line}")
            print("fail: comando invalido")


if __name__ == "__main__":
    main()
