import math


class SphericalTrigonometry:


    def __init__(self, lat1, lon1, lat2, lon2, radius):
        self.latitude_1 = math.radians(lat1)
        self.latitude_2 = math.radians(lat2)
        self.longitude_1 = math.radians(lon1)
        self.longitude_2 = math.radians(lon2)
        self.radius = radius
    

    def angle_calculator(self):
        difference_latitude = self.latitude_1 - self.latitude_2
        difference_longitude = self.longitude_1 - self.longitude_2

        haversine = math.sin(difference_latitude/2)**2 + math.cos(self.latitude_1) * math.cos(self.latitude_2) * math.sin(difference_longitude/2)**2

        central_angle = 2 * math.asin(math.sqrt(haversine))

        return central_angle
    

    def haversine_distance(self):
        central_angle = central_angle()

        distance = self.radius * central_angle

        return distance