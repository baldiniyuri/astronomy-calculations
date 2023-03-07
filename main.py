from Functions.spherical_trigonometry import start_trigonometry
from Functions.astronomy_calculations import start_astronomy_calculations
from Functions.images_analysis import start_image_analysis

def main():
    print("Running...")
    print("Select program.")
    print("1 For Spherical Trigonometry.")
    print("2 For Astronomical Calculations.")
    print("3 For Image Analysis.")
    program = int(input())
    
    if program == 1:
        start_trigonometry()
    elif program == 2:
        start_astronomy_calculations()
    elif program == 3:
        start_image_analysis()
    else:
        print("Invalid program input.")
        print("Terminating program.")

if __name__ == '__main__':
    main()