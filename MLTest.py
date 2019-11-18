from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
import pandas
import numpy
import data

from sklearn.svm import LinearSVC
from sklearn import tree
from sklearn.metrics import confusion_matrix, accuracy_score

def NNTest(dataset):
    (X_train, y_train), (X_test, y_test) = dataset
    model = Sequential()
    model.add(Dense(512, input_dim=256,activation='sigmoid'))
    model.add(Dense(512, activation='sigmoid'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=10)

    accuracy = model.evaluate(X_test, y_test)
    print("NN Result:")
    print(accuracy)
    print(model.metrics_names)

def SVMTest(dataset):
    (X_train, y_train), (X_test, y_test) = dataset
    svc = LinearSVC()
    svc.fit(X_train, y_train)

    y_pred = svc.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    ac = accuracy_score(y_test, y_pred)
    print("SVM Result:")
    print(cm)
    print(ac)

def DecisionTreeTest(dataset):
    (X_train, y_train), (X_test, y_test) = dataset
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    ac = accuracy_score(y_test, y_pred)
    print("DecisionTree Result:")
    print(cm)
    print(ac)
    
if __name__ == '__main__':
    dataset = data.byte_analysis_dataset('data.json')
    #NNTest(dataset)
    #SVMTest(dataset)
    #DecisionTreeTest(dataset)

