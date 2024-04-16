class Carro:
    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor

    def Ligar(self):
        return f"{self.ligar} seu carro está ligado!"
    
    def Desligar(self):
        return f"{self.desligar} seu carro está desligado!"
    
    def Acelerar(self):
        return f"{self.acelerar} você acelerou seu carro!"
    
if __name__ == "__main__":
    carro1 = Carro("Renault", "2024", "Vermelho")

    print(carro1.Ligar())
    print(carro1.Desligar())
    print(carro1.Acelerar())