class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getCarga(self) -> int:
        return self.__carga

    def getCapacidade(self) -> int:
        return self.__capacidade

    def usar(self, tempo: int) -> int:
        gasto = min(self.__carga, tempo)
        self.__carga -= gasto
        return gasto

    def carregar(self, tempo: int, potencia: int):
        self.__carga = min(self.__capacidade, self.__carga + tempo * potencia)

    def __str__(self):
        return f"({self.__carga}/{self.__capacidade})"

    def mostrar(self):
        print(str(self))


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def getPotencia(self) -> int:
        return self.__potencia

    def __str__(self):
        return f"(Potência {self.__potencia})"

    def mostrar(self):
        print(str(self))


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria

    def rmBateria(self) -> Bateria | None:
        bateria = self.__bateria
        self.__bateria = None
        print("bateria removida")
        return bateria

    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador

    def ligar(self):
        if (self.__bateria and self.__bateria.getCarga() > 0) or self.__carregador:
            self.__ligado = True
            print("notebook ligado")
        else:
            print("não foi possível ligar")

    def desligar(self):
        self.__ligado = False
        print("notebook desligado")

    def usar(self, tempo: int):
        if not self.__ligado:
            print("erro: ligue o notebook primeiro")
            return
        if not self.__bateria and not self.__carregador:
            print("erro: sem fonte de energia")
            self.__ligado = False
            return

        tempo_restante = tempo
        if self.__bateria:
            if self.__carregador:
                # bateria carrega durante o uso
                self.__bateria.carregar(tempo, self.__carregador.getPotencia())
            else:
                gasto = self.__bateria.usar(tempo)
                tempo_restante -= gasto
                if gasto < tempo:
                    print(f"Usando por {gasto} minutos, notebook descarregou")
                    self.__ligado = False
                    return
        print(f"Usando por {tempo} minutos")

    def mostrar(self):
        status = "Ligado" if self.__ligado else "Desligado"
        bateria = str(self.__bateria) if self.__bateria else "Nenhuma"
        carregador = str(self.__carregador) if self.__carregador else "Desconectado"
        print(f"Status: {status}, Bateria: {bateria}, Carregador: {carregador}")
