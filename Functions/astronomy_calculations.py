from fractions import Fraction


class AstronomyCalculations():

    def __init__(self, au, ly, parsec):
        self.astronomical_unity = au
        self.light_year = ly
        self.parsec = parsec

    
    def Light_Year_To_Kilometers(self, light_years: float):
        formula = Fraction(9.461e+12)
        return formula * light_years
    

    def Astronomical_Unity_To_Light_Year(self, units):
        formula = 63240
        return formula * units
    

    def Astronomical_Unity_To_Parsec(self, units):
        formula = 206300
        return formula / units