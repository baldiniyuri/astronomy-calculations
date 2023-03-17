from fractions import Fraction
import math

class AstronomyCalculations():

    def __init__(self, au: float, ly: float, parsec: float):
        self.astronomical_unity = au
        self.light_year = ly
        self.parsec = parsec

    
    def Light_Year_To_Kilometers(self):
        formula = Fraction(9.461e+12)
        return formula * self.light_year
    

    def Astronomical_Unity_To_Light_Year(self):
        formula = 63240
        return formula * self.astronomical_unity
    

    def Astronomical_Unity_To_Parsec(self):
        formula = 206300
        return formula / self.parsec
    

    def binary_star_mass(a, p):
        G = 6.67430e-11 
        m = 4 * math.pi**2 * a**3 / (G * p**2)
        return m
    

    def convert_period_to_seconds(self, period:int):
        return period * 365.25 * 24 * 3600 



def start_astronomy_calculations():
    print("Astronomy Calculations.")
    print("Please, enter a value for Astronomical Units.")
    au = float(input())
    print("Please, enter a value for Light Years.")
    ly = float(input())
    print("Please, enter a value for parsec.")
    parsec = float(input())
    print("Please, chose conversion method:")
    print("1 for Light year to kilometers conversion.")
    print("2 for Astronomical unity to light_Year conversion")
    print("3 for Astronomical unity to parsec")
    print("4 for Binary Mass Calculator")
    program = int(input())

    astronomy_calculations = AstronomyCalculations(au, ly, parsec)

    if program == 1:
        result = astronomy_calculations.Light_Year_To_Kilometers()
        print(f"The result of conversion of {ly} light years to kilometers is {result}")
    elif program == 2:
        result = astronomy_calculations.Astronomical_Unity_To_Light_Year()
        print(f"The result of conversion of {au} astronomical units to light year is {result}")
    elif program == 3:
        result = astronomy_calculations.Astronomical_Unity_To_Parsec()
        print(f"The result of conversion of {au} astronomical units to parsec is {result}")
    elif program == 4:
        print("Binary Mass Calculator")
        print("Enter a value for the semi-major axis. (in meters)")
        axis = float(input())
        print("Enter the orbital period value in years")
        period = int(period)
        orbital_period = astronomy_calculations.convert_period_to_seconds(period) 
        result = astronomy_calculations.binary_star_mass(axis, orbital_period)
        print(f"Combined mass of the binary star system is", {result}, "kg")
    else:
        print("Invalid program input.")
        print("End of program...")

