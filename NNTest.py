from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import numpy

dataset = loadtxt('test.csv', delimiter=',')
X_train = dataset[:600,0:8]
y_train = dataset[:600,8]

X_test = dataset[600:,0:8]
y_test = dataset[600:,8]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=150, batch_size=10)
accuracy = model.evaluate(X_test, y_test)
print(accuracy)

