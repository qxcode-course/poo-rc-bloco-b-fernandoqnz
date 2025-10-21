class Camisa:
    def __init__(self):  # Construtor
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in tamanhos_validos:
            print("Erro: o tamanho deve ser entre: PP, P, M, G, GG e XG.")
            return
        
        self.__tamanho = valor


# Programa principal
roupa = Camisa()

while roupa.getTamanho() == "":
    print("Digite seu tamanho de roupa:")
    tamanho = input().strip().upper()  # deixa maiúsculo e remove espaços
    roupa.setTamanho(tamanho)

print("Parabéns, você comprou uma roupa tamanho", roupa.getTamanho())
