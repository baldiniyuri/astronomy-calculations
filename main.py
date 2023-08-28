from Functions.spherical_trigonometry import start_trigonometry
from Functions.astronomy_calculations import start_astronomy_calculations
from Functions.space_images_analysis import start_image_analysis 
from Functions.decay_calculations import start_decay_calculation


def main():
    print("Running...")
    print("Select program.")
    print("1 For Spherical Trigonometry.")
    print("2 For Astronomical Calculations.")
    print("3 For Image Analysis.")
    print("4 For Zeta Analysis *** under development.")
    print("5 For Decay Calculations")
    
    program = int(input())
    
    if program == 1:
        start_trigonometry()
    elif program == 2:
        start_astronomy_calculations()
    elif program == 3:
        start_image_analysis()
    elif program == 4:
        print("To start Zeta, enter the following command.")
        print('start_zeta_analysis("/path/to/directory", "/path/to/dbfile")')
    elif program == 5:
        start_decay_calculation()
    else:
        print("Invalid program input.")
        print("Terminating program.")

if __name__ == '__main__':
    main()