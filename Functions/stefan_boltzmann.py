

class StefanBoltzmann:

    def __init__(self, temperature: float, area: float):
        self.temperature = temperature
        self.area = area
        self.stefan_boltzmann_constant = 5.670e-8

    
    def calculate_blackbody_power(self):
        power = self.stefan_boltzmann_constant * self.area * self.temperature**4
        return power
