import math


class StarDistance:
    def __init__(self, luminosity: float, brightness: float):
        self.luminosity = luminosity #watts value
        self.brightness = brightness #watts value
        self.sun_watts = 3.828e26 # Value of sun luminosity in watts.


    def convert_luminosity_from_watts_to_solar_luminosity(self):
        return self.luminosity / self.sun_watts
    

    def inverse_square(self, L_solar):
        return math.sqrt(L_solar / (4 * math.pi * self.brightness))
    
    
    def calculate_star_distance(self):
        L_solar = self.convert_luminosity_from_watts_to_solar_luminosity()
        
        distance_parsecs = self.inverse_square(L_solar)
        
        return distance_parsecs