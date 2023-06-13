import math


class SphericalTrigonometry:


    def __init__(self, lat1: float, lon1: float, lat2: float, lon2: float, radius: float) -> None:
        self.latitude_1 = math.radians(lat1)
        self.latitude_2 = math.radians(lat2)
        self.longitude_1 = math.radians(lon1)
        self.longitude_2 = math.radians(lon2)
        self.radius = radius
    

    def angle_calculator(self) -> float:
        difference_latitude = self.latitude_1 - self.latitude_2
        difference_longitude = self.longitude_1 - self.longitude_2

        haversine = math.sin(difference_latitude/2)**2 + math.cos(self.latitude_1) * math.cos(self.latitude_2) * math.sin(difference_longitude/2)**2

        central_angle = 2 * math.asin(math.sqrt(haversine))

        return central_angle
    

    def haversine_distance(self) -> float:
        central_angle = self.angle_calculator()

        distance = self.radius * central_angle

        return round(distance, 2)
    


def start_trigonometry() -> None:
    print("Spherical Trigonometry")
    print("Please, enter with first latitude.")
    latitude_1 = float(input())
    print("Please, enter with first longitude.")
    longitude_1 = float(input())
    print("Please, enter with second latitude.")
    latitude_2 = float(input())
    print("Please, enter with second longitude.")
    longitude_2 = float(input())
    print("Please enter the radius (Earth radius is 6371)")
    radius = float(input())

    spherical_trigonometry = SphericalTrigonometry(latitude_1, longitude_1, latitude_2, longitude_2, radius)
    
    result = spherical_trigonometry.haversine_distance()
    print(f"The distance between location 1 and location 2 is {result} Kilometers")
    print("End of program...")