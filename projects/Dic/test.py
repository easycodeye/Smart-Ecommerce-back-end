from keras.datasets import mnist
from keras import layers, models, utils

from gym import envs


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))
network.add(layers.LSTM(10, activation='softmax'))
network.add(layers.Conv3D(10, activation='softmax'))

network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


# train_images = train_images.reshape((60000, 28 * 28))
# train_images = train_images.astype('float32') / 255
# test_images = test_images.reshape((10000, 28 * 28))
# test_images = test_images.astype('float32') / 255

# train_labels = utils.to_categorical(train_labels)
# test_labels = utils.to_categorical(test_labels)

# test_loss, test_acc = network.evaluate(test_images, test_labels)
# print('test_acc:', test_acc)
