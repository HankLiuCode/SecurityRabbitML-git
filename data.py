from keras.datasets import mnist
from sklearn import datasets
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
import pandas


def byte_analysis_dataset():
    df = pandas.read_excel('analysis_data.xlsx')
    train, test = train_test_split(df, test_size=0.2)
    y_train = train.pop('score').values
    y_test = test.pop('score').values
    X_train = train.values
    X_test = test.values
    return [(X_train, y_train), (X_test, y_test)]


if __name__ == '__main__':
    (X_train, y_train), (X_test, y_test) = byte_analysis_dataset()
    