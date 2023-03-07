import cv2


class ImagesAnalysis:

    def __init__(self, filename):
        self.filename = filename
    

    def open_image(self):
        return cv2.imread(self.filename)


    def gray_converter(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    def create_binary_image(self, gray):
        ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        return binary
    

    def count_black_and_white_pixels(self, binary):
        count_black_pixels = cv2.countNonZero(binary)
        count_white_pixels = binary.size - count_black_pixels
        return {'black': count_black_pixels, 'white': count_white_pixels}


    def filter_size(self, contours):
        min_size = 3
        max_size = 30
        contours = [c for c in contours if len(c) >= min_size and len(c) <= max_size]
        return contours


    def apply_binary_threshold(self, image):
        return cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
    

    def draw_contours(self, binary):
        return cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    

    def count_stars(self, image):
        _, binary = self.apply_binary_threshold(image)

        contours, _ = self.draw_contours(binary)
        contours = self.filter_size(contours)

        result = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        cv2.drawContours(result, contours, -1, (0, 0, 255), 1)

        return len(contours), result
        
    def display_image(self, image, result_image):
        cv2.imshow("Original Image", image)
        cv2.imshow("Result Image", result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def analyze_image(self):
        image = self.open_image()
   
        gray = self.gray_converter(image)

        binary = self.create_binary_image(gray)

        result = self.count_black_and_white_pixels(binary)
        print(result)

        num_stars, result_image = self.count_stars(gray)
        print("Number of stars:", num_stars)

        self.display_image(image, result_image)


def start_image_analysis():
    print("Image Analysis.")
    print("Please, enter the path of the file")
    file = input()

    image_analysis = ImagesAnalysis(file)
    image_analysis.analyze_image()
    print("End of program.")