import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, accuracy_score
import data

(X_train, y_train), (X_test, y_test) = data.getDataset1()
svc = LinearSVC()
svc.fit(X_train, y_train)

y_pred = svc.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)
print(cm)
print(ac)
