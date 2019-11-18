from keras.datasets import mnist
from sklearn import datasets
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
import pandas
import json
import re

def byte_analysis_dataset(json_name):
    with open(json_name) as f:
        datajson = json.load(f)
    file_info_list = json.loads(datajson['fileinfo'])
    df = pandas.DataFrame(file_info_list)
    byte_distribution_df = df.iloc[:,df.columns.get_loc("0x0"):df.columns.get_loc("0xff")+1]
    isMalware_df = df['isMalware']
    byte_analysis_df = byte_distribution_df.join(isMalware_df)

    train, test = train_test_split(byte_analysis_df, test_size=0.2)
    y_train = train.pop('isMalware').values
    y_test = test.pop('isMalware').values
    X_train = train.values
    X_test = test.values

    return [(X_train, y_train), (X_test, y_test)]

def printable_strs_analysis_dataset(json_name):
    raw_str_list = []
    with open(json_name) as f:
        datajson = json.load(f)
    file_info_list = json.loads(datajson['fileinfo'])

    for file_info in file_info_list:
        printable_str_list = file_info['printable_strs']
        for printable_str in printable_str_list:
            raw_str_list.append(printable_str)

    phase1_str_list = []
    for temp_str in raw_str_list:
        is_meaningless = re.search('^[\W]+$',temp_str)
        if not is_meaningless:
            phase1_str_list.append(temp_str)
    
    diff = list(set(raw_str_list) - set(phase1_str_list))
    print("Differences: {}".format(diff))
    print("No of differences:{}".format(len(diff)))
    print("length of raw_str_list: {}".format(len(raw_str_list)))
    print("length of phase1_str_list: {}".format(len(phase1_str_list)))
    #print(file_info_list[0]['printable_strs'][-1])

def test_dataset():
    df = pandas.read_excel('analysis_data.xlsx')
    train, test = train_test_split(df, test_size=0.2)
    y_train = train.pop('score').values
    y_test = test.pop('score').values
    X_train = train.values
    X_test = test.values
    return [(X_train, y_train), (X_test, y_test)]


if __name__ == '__main__':
    #(X_train, y_train), (X_test, y_test) = byte_analysis_dataset('data.json')
    printable_strs_analysis_dataset('data.json')
    