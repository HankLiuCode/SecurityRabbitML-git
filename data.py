from keras.datasets import mnist
from sklearn import datasets
from sklearn.model_selection import train_test_split
from matplotlib import pyplot

def showplot(image):
    pyplot.figure(figsize=(3,3))
    pyplot.imshow(image)
    pyplot.show()

def getDataset1():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    n_classes = 10
    X_train = X_train.reshape(60000, 784)
    X_test = X_test.reshape(10000, 784)
    return [(X_train, y_train), (X_test, y_test)]

def getDataset2():
    digits = datasets.load_digits()
    X_train, X_test, y_train, y_test = train_test_split(digits)

    return [(X_train, y_train), (X_test, y_test)]

if __name__ == '__main__':
    getDataset1()
    