class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca 
        self.modello = modello 

    def scheda(self):
        return f"Marca: {self.__marca}, Modello: {self.__modello}"
        
class AutoPorte(Veicolo):
    def __init__(self, marca, modello, numero_porte):
        super().__init__(marca, modello)
        self.__numero_porte = numero_porte 

    def scheda(self):
        return f"{super().scheda()}, Numero porte: {self.__numero_porte}"

class MotoCilindrata(Veicolo):
    def __init__(self, marca, modello, cilindrata):
        super().__init__(marca, modello)
        self.__cilindrata = cilindrata

    def scheda(self):
        return f"{super().scheda()}, Cilindrata: {self.__cilindrata}"