class bicicleta:
   def __init__(self, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo    
    self.ano = ano
    self.valor = valor
    def buzinar(self):
      print("fon fon")

    def parar(self):
      print ("parando bike ")
      print ("bike parada ")

    def correr(self):
      print("acelerando")

    def __str__(self):
      return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave , valor in self.__dict__.items() ])}"


b1 = bicicleta("vermelha", "caloi", 2022, 600)

print (b1.cor, b1.modelo, b1.ano,)  