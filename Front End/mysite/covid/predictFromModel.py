from tensorflow.keras.models import model_from_json
from tensorflow import keras
import tensorflow as tf

def load_model():
    global model
    # load json and create model
    json_file = open('covid/static/covid/savedModel/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("covid/static/covid/savedModel/model.h5")
    # print("Loaded model from disk")


def get_result(array):
    if array[0][0]:
        result = 'POSITIVE'
    else:
        result = 'NEGATIVE'
    return result


def make_prediction(img_dir):
    # printing prediction from loaded model
    img = keras.preprocessing.image.load_img(
        img_dir, target_size=(150, 150)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    return get_result(predictions)
