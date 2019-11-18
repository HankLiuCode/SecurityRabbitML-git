import json
import pandas
import re



if __name__ == '__main__':
    test = "abcdcatabcd"
    result = re.search("cat",test)
    print(result)
    if not result:
        print(True)