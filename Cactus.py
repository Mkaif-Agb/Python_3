import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Convolution2D, Dense, Flatten, Dropout, MaxPooling2D
from keras.models import Sequential

classifier = Sequential()

classifier.add(Convolution2D(64, 3, 3, input_shape=(32, 32, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Dropout(0.2))


classifier.add(Convolution2D(32,(3,3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Dropout(0.2))

classifier.add(Flatten())
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'softmax'))

classifier.compile(optimizer='adam', loss='mean_absolute_error', metrics=['mean_absolute_error'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('Cactus/train',
                                                 target_size = (32, 32),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('Cactus/test',
                                            target_size = (32, 32),
                                            batch_size = 32,
                                            class_mode = 'binary')

classifier.fit_generator(training_set,
                         samples_per_epoch = 17500,
                         nb_epoch = 25,
                         validation_data = test_set,
                         nb_val_samples = 4000)

