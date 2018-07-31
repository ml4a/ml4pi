import time
import numpy as np
import cv2
import picamera
import picamera.array
from PIL import Image
import keras
from keras import backend as K
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Model
from keras.applications import imagenet_utils
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Input

NUM_CLASSES = 2
LEARNING_RATE = 0.0001
EPOCHS = 20
DENSE_UNITS = 100

TRAINING_DATA = [] # Example array to be trained
TRAINING_LABELS = [] # Label array


# Load mobilenet model
def loadModel():
    mobilenet = keras.applications.mobilenet.MobileNet()
    flatten = Flatten(input_shape=(7,7,1024))(mobilenet.get_layer('conv_pw_13_relu').output)
    fc1 = Dense(DENSE_UNITS, activation='relu')(flatten)
    fc2 = Dense(NUM_CLASSES)(flatten)
    output = Activation('softmax')(fc2)
    model = Model(mobilenet.input, output)
    # make all layers untrainable by freezing weights (except for last two layers)
    for l, layer in enumerate(model.layers[:-3]):
        layer.trainable = False
    # ensure the last layer is trainable/not frozen
    for l, layer in enumerate(model.layers[-3:]):
        layer.trainable = True
    return model

# function prepares an image to keras
def prepare_frame(frame):
    img = Image.fromarray(frame, 'RGB')
    img = img.resize((224,224))
    img_array = np.array(img)
    img_array_extended = np.expand_dims(img_array, axis=0).astype('float32')
    processed = keras.applications.mobilenet.preprocess_input(img_array_extended)
    return processed


def addExample(example, label): # add examples to training data set
    encoded_y = keras.utils.np_utils.to_categorical(label,num_classes=NUM_CLASSES) # make one-hot
    TRAINING_LABELS.append(encoded_y)
    TRAINING_DATA.append(example[0])
    print('add example for label %d'%label)

 
# load the model
model = loadModel()
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# start camera
with picamera.PiCamera() as camera:
     with picamera.array.PiRGBArray(camera) as output:
        while True:
            camera.capture(output, 'rgb')
            print('Captured %dx%d image' % (output.array.shape[1], output.array.shape[0]))

            frame = output.array

            cv2.imshow('capturing',frame)
            key=cv2.waitKey(1)

            if key == ord('1'): # add example in class 0
                addExample(prepare_frame(frame), 0)

            if key == ord('2'): # add example in class 1
                addExample(prepare_frame(frame), 1)

            if key == ord('t'): # train
                model.fit(np.array(TRAINING_DATA), np.array(TRAINING_LABELS), epochs=EPOCHS, batch_size=8)

            if key == ord('p'): # predict
                processed_image = prepare_frame(frame) # prepare frame
                prediction = model.predict(processed_image)
                result = np.argmax(prediction) #imagenet_utils.decode_predictions(prediction)
                print('predict %d'%result)

            if key == ord('q'): # quit
                break

            output.truncate(0)

