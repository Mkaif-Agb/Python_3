import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("ClassifiedData.csv",index_col=0)
sns.heatmap(df.isnull(),cbar=False,cmap='viridis',yticklabels=False)
plt.show()

sns.pairplot(df,hue='TARGET CLASS')
plt.tight_layout()
plt.show()

scaler = StandardScaler()
scaler.fit(df.drop(['TARGET CLASS'],axis=1))
scaled_features = scaler.transform(df.drop(['TARGET CLASS'],axis=1))
df_feat = pd.DataFrame(scaled_features,columns=df.columns[:-1],)


X = df_feat
y = df.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_test,y_pred)
print(cm)
cr = classification_report(y_test,y_pred)
print(cr)

error_rate=[]
for i in range(1,50):
    classifier = KNeighborsClassifier(n_neighbors=i)
    classifier.fit(X_train, y_train)
    y_pred_i = classifier.predict(X_test)
    error_rate.append(np.mean(y_pred_i!=y_test))

plt.plot(range(1,50),error_rate,color='red',linestyle='--',marker='o',markersize=10,markerfacecolor='blue')
plt.title("Elbow Method")
plt.xlabel("Range")
plt.ylabel("Error Rate")
plt.show()

# 40 is the lowest

classifier = KNeighborsClassifier(n_neighbors=40)
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_test,y_pred)
print(cm)
cr = classification_report(y_test,y_pred)
print(cr)