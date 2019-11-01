from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import numpy
import data

(X_train, y_train), (X_test, y_test) = data.getDataset1()
Y_train = np_utils.to_categorical(y_train, n_classes)
Y_test = np_utils.to_categorical(y_test, n_classes)

model = Sequential()
model.add(Dense(512, input_shape= (784,) ,activation='sigmoid'))
model.add(Dense(512, activation='sigmoid'))
model.add(Dense(10, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, Y_train, epochs=10, batch_size=10)
accuracy = model.evaluate(X_test, Y_test)
print(accuracy)

