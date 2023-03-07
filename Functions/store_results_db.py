import sqlite3, os, cv2
import numpy as np
from Functions.zeta_training import Zeta


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