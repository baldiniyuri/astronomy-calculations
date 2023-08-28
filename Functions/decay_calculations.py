import math
from Variables.elements_decay import ELEMENTS_SAMPLE


class DecayCalculations:
    def __init__(self, N:float, NO: float, decay_constant: float) -> None:
        self.undecayed_atoms: float = N
        self.original_atoms: float = NO
        self.decay_constant: float = decay_constant


    def verify_values(self) -> None:
        if self.undecayed_atoms <= 0 or self.original_atoms <= 0 or self.decay_constant <= 0:
            raise ValueError("All input values should be positive and non-zero.")
    

    def calculate_age(self) -> float:
        self.verify_values()
        return math.log(self.original_atoms / self.undecayed_atoms) / self.decay_constant


    def format_age_result(self, result):   
        age_rounded = round(result, 2)

        if result >= 1e9:  
            return f"{round(result / 1e9, 2)} billion years"
        elif result >= 1e6: 
            return f"{round(result / 1e6, 2)} million years"
        else:
            return f"{age_rounded} years"


def start_decay_calculation() -> None:
    print("Decay Calculations")
    print("Elements Sample")
    for i in ELEMENTS_SAMPLE:
        print(i)
    print("Enter a value for Undecayed Atoms")
    n = float(input())
    print("Enter a value for the Original Atoms count")
    no = float(input())
    print("Enter a value for Element Decay")
    decay_constant = float(input())
    calculate = DecayCalculations(N=n, NO=no, decay_constant=decay_constant)
    result = calculate.calculate_age()
    age = calculate.format_age_result(result=result)
    print(f"Age of the sample is: {age}")