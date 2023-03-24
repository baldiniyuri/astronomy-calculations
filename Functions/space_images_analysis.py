import cv2
import numpy as np
import multiprocessing as mp
from Functions.learning_calculations import LearningCalculation


class SpaceImagesAnalysis:

    def __init__(self, filename):
        self.filename = filename
        self.images = []  
        self.labels = [] 

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

        return num_stars
    

    def add_image(self):
        image = self.open_image()

        gray = self.gray_converter(image)

        binary = self.create_binary_image(gray)

        num_stars = self.analyze_image()
        self.images.append(binary)
        self.labels.append(num_stars)
        print(f"Images:{self.images}, Labels: {self.labels}")


    def image_object_builder(self):
        for i in self.images:
            print(i)
        
    
class SpaceImagesAnalysisLearning(SpaceImagesAnalysis):
    def train(self, num_epochs, learning_rate):
        weights = np.random.randn(1, 1) 
        b = np.zeros((1, 1))

        for i in range(num_epochs):
            for j in range(len(self.images)):
                x = self.images[j].flatten().reshape((-1, 1))
                y_true = self.labels[j]

                learning_model = LearningCalculation(x, weights, b, learning_rate)

                mse = learning_model.mean_squared_error(y_true)
                print(mse)

                dw = np.dot(x, (2 * (learning_model.linear_function() - y_true)))
                learning_model.update_weights(dw)

                weights = learning_model.w
                b = learning_model.b

        return weights, b
    

def analyze_image_multiprocessing(file, learning_rate):

    image_analysis = SpaceImagesAnalysisLearning(file)


    image_analysis.add_image()


    weights, bias = image_analysis.train(num_epochs=100, learning_rate=learning_rate)


    input_image = cv2.imread(file)
    input_image_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    input_image_binary = image_analysis.create_binary_image(input_image_gray)
    input_image_flattened = input_image_binary.flatten()


    learning_model = LearningCalculation(input_image_flattened, weights, bias, learning_rate)

    predicted_num_stars = learning_model.linear_function()
    print('Predicted number of stars:', predicted_num_stars)

    return weights, bias, predicted_num_stars



def start_image_analysis():
    print("Image Analysis.")
    print("Please, enter the path of the file")
    file = input()
    print("Please, enter the learning rate.")
    learning_rate = float(input())

    pool = mp.Pool(processes=4)

    result = pool.apply_async(analyze_image_multiprocessing, args=(file, learning_rate))

    weights, bias, predicted_num_stars = result.get()

    print("End of program.")
    print(f"wights {weights}, bias {bias}, predict_num_stars {predicted_num_stars}")
    return weights, bias, predicted_num_stars

    #test