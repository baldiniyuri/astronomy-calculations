from fractions import Fraction


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



def start_astronomy_calculations():
    print("Astronomy Calculations.")
    print("Please, enter a value for Astronomical Units.")
    au = float(input())
    print("Please, enter a value for Light Years.")
    ly = float(input())
    print("Please, enter a value for parsec.")
    parsec = float(input())
    print("Please, chose conversion method:")
    print("1 for light year to kilometers conversion.")
    print("2 for astronomical unity to light_Year conversion")
    print("3 for astronomical unity to parsec")
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
    else:
        print("Invalid program input.")
        print("End of program...")

