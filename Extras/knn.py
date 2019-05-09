from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Load dataset
df = pd.read_csv('log3.csv')

#Inputs
X = df.drop('Label', axis=1).values

#Classes
y = df['Label'].values

#Split dataset into train and test
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42, stratify=y)

# Declare an of the classifiers class with the value with neighbors.
knn = KNeighborsClassifier(n_neighbors=5)
clf = SVC(kernel='rbf')
dt = DecisionTreeClassifier(max_depth=5)

# Fit the model with training data and target values
knn.fit(X_train, y_train)
clf.fit(X_train, y_train)
dt.fit(X_train, y_train)

# Provide data whose class labels are to be predicted
#X = [[1, 5]]
# Store predicted class labels of X
knnPrediction = knn.predict(X_test)
svmPrediction = clf.predict(X_test)
dtPrediction = clf.predict(X_test)

# Prints the predicted class labels of X
print('knn Prdict\n')
print(knnPrediction)
print('svm Prdict\n')
print(svmPrediction)
print('dt Prdict\n')
print(dtPrediction)

#Print scores
""" print('Knn= ' + str(knn.score(X_test,y_test)))
print('SVM= ' + str(clf.score(X_test,y_test)))
print('DT= ' + str(dt.score(X_test,y_test))) """

print('KNN:\n')
print(classification_report(knnPrediction, y_test))
print('SVM:\n')
print(classification_report(svmPrediction, y_test))
print('DT:\n')
print(classification_report(dtPrediction, y_test))