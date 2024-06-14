class computador:   #classe nao dinamica (pior)
    def __init__(self):
        self.marca = "LG"
        self.memoria = "8gb"
        self.placa_video = "gtx1650"
print(computador().marca, computador().memoria, computador().placa_video)
print("=" * 100)

class computador1:    #Classe dinamica (melhor)
    def __init__(self, marca, memoria, placa_video):   
        self.marca = marca     #propriedade
        self.memoria = memoria      #propriedade
        self.placa_video = placa_video   #propriedade

    def ligar(self):    #metodo
        print("ligando")
    
    def desligar(self):   #metodo
        print("desligando")
    
    def informações(self):   #metodo
        print(self.marca, self.memoria, self.placa_video)

print(computador1("DELL", "16gb", "NVidia").marca, computador1("DELL", "16gb", "NVidia").memoria, computador1("DELL", "16gb", "NVidia").placa_video)
print("=" * 100)

computador1("DELL", "24GB", "AMD").informações()
