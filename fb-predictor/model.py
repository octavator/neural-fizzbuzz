import os
import tensorflow as tf

class Model:
  def __init__(self):
    self.model = None

  def get_last_modified_model(self, folder):
    files = [ folder + file for file in os.listdir(path=folder) ]
    latest_model = max(files, key=os.path.getmtime)
    return latest_model

  def load(self, model_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    model_path = os.path.join(dir_path, '../fizzbuzz_models/')
    if model_name != None:
        self.model = tf.keras.models.load_model(model_path + model_name)
        print("Imported model from 'fizzbuzz_models/" + model_name + "'\n")
    else:
        last_model_path = self.get_last_modified_model(model_path)
        self.model = tf.keras.models.load_model(last_model_path)
        print("Imported model from '" + last_model_path + "'\n")

  def predict(self, binary_nb):
    result = self.model.predict(binary_nb)
    for i, rows in enumerate(result):
        for k, cols in enumerate(rows):
            if (tf.argmax(rows) == k):
                result[i][k] = 1
            else:
                result[i][k] = 0
    return result
