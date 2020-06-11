import tensorflow as tf
import pandas as pd
import numpy as np
import sklearn.model_selection as sk
import time
import os
import sys

tf.random.set_seed(2)
np.random.seed(2)
SK_RANDOM_STATE = 42

#DEFAULT PARAMETERS
NB_OF_BITS = 18 #(Max value: 262143)
NB_OF_SAMPLES = 50000
NB_OF_ITERATIONS = 200
TEST_DATA_SIZE = 20 #(%)
MODEL_NAME = time.strftime("%a %d %b %Y %Hh%Mm%Ss", time.gmtime()) #Renvoie la date et l'heure formatés
#OUTPUT INDICES
NUMBER = 0
FIZZ = 1
BUZZ = 2
FIZZBUZZ = 3

#GET OPTIONS
dir_path = os.path.dirname(os.path.realpath(__file__))
full_path = os.path.join(dir_path, '../options.py')
exec(open(full_path).read())
get_opts()


decimal_data = np.random.randint((2 ** (NB_OF_BITS)), size=NB_OF_SAMPLES)
y = np.zeros((NB_OF_SAMPLES, 4))

binary_data = []
for i in range (0, NB_OF_SAMPLES):
    decimal_nb = decimal_data[i]
    bits = [int(bit) for bit in np.binary_repr(decimal_nb, NB_OF_BITS)]
    binary_data.append(bits)

    output = y[i]
    if (decimal_nb % 5 == 0 and decimal_nb % 3 == 0):
        output[FIZZBUZZ] = 1
    elif (decimal_nb % 3 == 0):
        output[FIZZ] = 1
    elif (decimal_nb % 5 == 0):
        output[BUZZ] = 1
    else:
        output[NUMBER] = 1

X = pd.DataFrame(binary_data)
Y = pd.DataFrame(y, columns=['number', 'fizz', 'buzz', 'fizzbuzz'])

X_train, X_test, y_train, y_test = sk.train_test_split(X, Y, 
 test_size=TEST_DATA_SIZE / 100, stratify=Y.values, random_state=SK_RANDOM_STATE)
 

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(30, activation='relu', input_shape=(NB_OF_BITS,)),
    tf.keras.layers.Dense(60, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax')
])

model.compile(optimizer="adam",loss='binary_crossentropy')

model.fit(X_train, y_train, epochs=NB_OF_ITERATIONS)

loss = model.evaluate(X_test, y_test)


save_dir = os.path.join(dir_path, os.path.join('..', 'fizzbuzz_models'))
save_path = os.path.join(save_dir, MODEL_NAME)
model.save(save_path)
model_review = open(os.path.join(save_path, 'model_review.txt'),"a+")
model_review.write("method = binary encoding, loss = " + str(loss))
model_review.close()
