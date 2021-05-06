import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("titanic_train.csv")


# Visualizing The Data
sns.pairplot(df, palette='Dark2')
plt.show()
sns.heatmap(df.isnull(),cbar=False,cmap='viridis')
plt.show()
sns.set_style("whitegrid")
sns.countplot(x='Survived',data=df,hue='Sex')
sns.countplot(x='Survived',data=df,hue='Pclass')
sns.distplot(df['Age'].dropna(),bins=30,kde=False)
sns.distplot(df['Fare'],bins=30,kde=False)

# Cleaning The Data

plt.figure(figsize=(12,9))
sns.boxplot(x='Pclass',y='Age',data=df)

def imputeage(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        if Pclass==1:
            return 37
        elif Pclass==2:
            return 29
        else:
            return 24
    else:
        return Age

df['Age'] = df[['Age', 'Pclass']].apply(imputeage,axis=1) # All the Age are sorted
df.drop('Cabin',axis=1, inplace=True)
df.dropna(inplace=True)

# Now For Dummy Variables

sex = pd.get_dummies(df['Sex'],drop_first=True)
embarked = pd.get_dummies(df['Embarked'],drop_first=True)
df = pd.concat([df,sex,embarked],axis=1)

df.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
df.drop('PassengerId',axis=1,inplace=True)

# Logistic Regression

y = df.iloc[:, 0:1].values
X = df.iloc[:, 1:].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)
print(cm)
print(cr)

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=classifier, X = X_train, y= y_train, cv=10, n_jobs=-1)
print(accuracies.mean())
print(accuracies.std())
