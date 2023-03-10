
class WienDisplacement:

    def __init__(self, celsius: float):
        self.wien_constant = 2.898e-3
        self.celsius = celsius


    def celsius_to_kelvin_converter(self):
        return self.celsius + 273.15


    def calculate_displacement(self):
        temperature_kelvin= self.celsius_to_kelvin_converter()
        return self.wien_constant / temperature_kelvin
    
