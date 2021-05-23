import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords 

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
import pandas as pd
import sys

#####################################################################

data_path = "D:/VIT/SEM-6/G2 - Information Security Management/Project/"
df = pd.read_csv(data_path + "sqli.csv",encoding='utf-16')
df.tail()

vectorizer = CountVectorizer( min_df=2, max_df=0.7, stop_words=stopwords.words('english'))
posts = vectorizer.fit_transform(df['Sentence'].values.astype('U')).toarray()

transformed_posts = pd.DataFrame(posts)
transformed_posts.tail()

df=pd.concat([df,transformed_posts],axis=1)

X=df[df.columns[2:]]
y=df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

df2 = pd.DataFrame( {"Sentence":["Number A","Number B"], "Label":[0,0]} )
X_test = X_test.append(df2['Sentence'], ignore_index = True)
print(X_test.tail())
y_test = y_test.append(df2['Label'], ignore_index = True)
print(y_test.tail())
print(len(X_test),len(y_test))

##################################################################

input_dim = X_train.shape[1]  # Number of features

model = Sequential()
model.add(layers.Dense(20, input_dim=input_dim, activation='relu'))
model.add(layers.Dense(10,  activation='tanh'))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy', 
              optimizer='adam', 
              metrics=['accuracy'])

nn_history = model.fit(X_train,y_train,
                    epochs=10,
                    verbose=True,
                    validation_data=(X_test, y_test),
                    batch_size=15)

nn_pred = model.predict(X_test[-2:])
for i in range(len(nn_pred)):
    if nn_pred[i]>0.5:
        nn_pred[i]=1
    elif nn_pred[i]<=0.5:
        nn_pred[i]=0

print(nn_pred)

"""
acc = nn_history.history['accuracy']
val_acc = nn_history.history['val_accuracy']
epochs = range(1, len(acc)+1)

plt.plot(epochs, acc, 'b', label = "training accuracy")
plt.plot(epochs, val_acc, 'r', label = "validation accuracy")
plt.title('Training and validation accuracy')
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
#plt.axis([0, 50, 0.65, 1.10])
plt.legend()
plt.show()
model.save('./ml/model_NN.h5')
print(classification_report(y_test, nn_pred))
"""
