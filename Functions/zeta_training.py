import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


class Zeta:
    def __init__(self, directory):
        self.directory = directory
        self.images = []
        self.labels = []
    

    def image_collector(self):
        for filename in os.listdir(self.directory):
            if filename.endswith(".jpg"):
                image = cv2.imread(os.path.join(self.directory, filename), cv2.IMREAD_GRAYSCALE)
                num_stars = int(filename.split("_")[0])
                self.images.append(image)
                self.labels.append(num_stars)


    def preprocess_dataset(self):
        features = np.array(self.images).reshape(len(self.images), -1)
        features = features / 255.0  
        self.labels = np.array(self.labels)
        return features

    
    def split_dataset(self, features):
        return train_test_split(features, self.labels, test_size=0.2)


    def train_logistic(self, X_train, y_train):
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        return model
    

    def evaluate_performance(self, model, X_val, y_val):
        y_pred = model.predict(X_val)
        acc = accuracy_score(y_val, y_pred)
        print(f"Validation accuracy: {acc:.2f}")


    def analyze_images(self):
        features = self.preprocess_dataset()

        X_train, X_val, y_train, y_val = self.split_dataset(features)

        model = self.train_logistic(X_train, y_train)

        self.evaluate_performance(self, model, X_val, y_val)


