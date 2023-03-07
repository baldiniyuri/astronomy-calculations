import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import sqlite3


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


class StoreResultsInDataBase:
        def __init__(self, directory, dbfile):
            self.directory = directory
            self.dbfile = dbfile
            self.conn = sqlite3.connect(self.dbfile)
            self.zeta = Zeta(self.directory)


        def connect_database(self):
            cursor = self.conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS results (filename TEXT, num_stars INT, pred_stars INT)")
            return cursor


        def disconnect_database(self, cursor):
            self.conn.commit()
            cursor.close()
            self.conn.close()


        def analyze_images_and_store(self):
            self.zeta.image_collector()
            features = self.zeta.preprocess_dataset()
            X_train, X_val, y_train, y_val = self.zeta.split_dataset(features)
            model = self.zeta.train_logistic(X_train, y_train)
            self.zeta.evaluate_performance(model, X_val, y_val)

            cursor = self.connect_database()

            for filename in os.listdir(self.directory):
                if filename.endswith(".jpg"):
                    image = cv2.imread(os.path.join(self.directory, filename), cv2.IMREAD_GRAYSCALE)
                    features = np.array([image.ravel()]) / 255.0
                    num_stars = int(filename.split("_")[0])
                    pred = model.predict(features)[0]
                    cursor.execute("INSERT INTO results (filename, num_stars, pred_stars) VALUES (?, ?, ?)", (filename, num_stars, pred))
            self.disconnect_database(cursor)