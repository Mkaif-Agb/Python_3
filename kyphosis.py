import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("kyphosis.csv")

sns.pairplot(data=df,hue='Kyphosis')
sns.heatmap(df.isnull(),cbar=False,yticklabels=False,cmap='viridis')

X = df.drop("Kyphosis",axis=1)
y = df.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

y_pred = dtree.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
print(cm)
print("\n")
print(classification_report(y_test, y_pred))


rtree = RandomForestClassifier(n_estimators=300)
rtree.fit(X_train, y_train)
y_pred1 = rtree.predict(X_test)

cm = confusion_matrix(y_test, y_pred1)
print(cm)
print("\n")
print(classification_report(y_test, y_pred1))


