from Functions.spherical_trigonometry import start_trigonometry
from Functions.astronomy_calculations import start_astronomy_calculations


def main():
    print("Running...")
    print("Select program.")
    print("1 For Spherical Trigonometry")
    print("2 For Astronomical Calculations")
    program = int(input())
    if program == 1:
        start_trigonometry()
    elif program == 2:
        start_astronomy_calculations()
    else:
        print("Invalid program input.")
        print("Terminating program.")

if __name__ == '__main__':
    main()