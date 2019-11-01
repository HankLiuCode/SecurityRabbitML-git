from sklearn import tree
from sklearn.metrics import confusion_matrix, accuracy_score
import data

(X_train, y_train), (X_test, y_test) = data.getDataset1()

clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)
print(cm)
print(ac)