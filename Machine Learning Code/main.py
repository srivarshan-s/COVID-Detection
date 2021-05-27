import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json


def load_model():
    global model
    # load json and create model
    json_file = open('savedModel/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("savedModel/model.h5")
    # print("Loaded model from disk")


def print_result(array):
    print(array)
    if array[0][0]:
        print('COVID')
    else:
        print('NORMAL')


def make_prediction(img_dir):
    # printing prediction from loaded model
    img = keras.preprocessing.image.load_img(
        img_dir, target_size=(150, 150)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    print_result(predictions)

def main():
    load_model()
    img_path = 'userData/NORMAL(1266).jpg'
    make_prediction(img_path)
    img_path = 'userData/COVID19(460).jpg'
    make_prediction(img_path)


if __name__ == '__main__':
    main()
