from Variables.astronomy_variables import ELEMENTS
from typing import List


class StarSpecter:

    def __init__(self, kelvin_temperature: float) -> None:
        self.kelvin = kelvin_temperature
        self.elements_list = []
    
    
    def check_elements(self) -> List[str]:
        if self.kelvin >= 20001:
            self.elements_list.append(ELEMENTS[0])
            self.elements_list.append(ELEMENTS[1])

        if self.kelvin > 10001 and self.kelvin <= 20000:
            self.elements_list.append(ELEMENTS[3])
            self.elements_list.append(ELEMENTS[4])
        
        if self.kelvin > 7001 and self.kelvin <= 10000:
            self.elements_list.append(ELEMENTS[5])
            self.elements_list.append(ELEMENTS[6])
        
        if self.kelvin > 6001 and self.kelvin <= 7000:
            self.elements_list.append(ELEMENTS[5])
            self.elements_list.append(ELEMENTS[6])
        
        if self.kelvin > 4001 and self.kelvin <= 6000:
            self.elements_list.append(ELEMENTS[6])
            self.elements_list.append(ELEMENTS[7])

        if self.kelvin > 3000 and self.kelvin <= 4000:
            self.elements_list.append(ELEMENTS[6])
            self.elements_list.append(ELEMENTS[7])

        else:
            self.elements_list.append(ELEMENTS[2])
            self.elements_list.append(ELEMENTS[7])
        
        return self.elements_list