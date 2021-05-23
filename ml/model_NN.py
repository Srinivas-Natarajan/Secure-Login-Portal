import numpy as np
import pandas as pd
import sys
import pickle

from keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer

import nltk
from nltk.corpus import stopwords 
nltk.download('stopwords')

print('#Hello from python#')
print('First param:'+sys.argv[1]+'#')
print('Second param:'+sys.argv[2]+'#\n')

###########################################

df = pd.DataFrame({"Sentence":[sys.argv[1],sys.argv[2]]})
#df = pd.DataFrame({"Sentence":['sample@gmail.com',"admin' or 1 = 1#"]})


feature_path = './ml/features.pkl'
vectorizer= CountVectorizer(vocabulary=pickle.load(open(feature_path, "rb")))
posts = vectorizer.fit_transform(df['Sentence'].values.astype('U')).toarray()
print(len(posts[0]))

model = load_model("./ml/model_NN.h5")
model.compile(loss='binary_crossentropy', 
              optimizer='adam', 
              metrics=['accuracy'])

nn_pred = model.predict(pd.DataFrame(posts))

print("Before: ",nn_pred)
for i in range(len(nn_pred)):
    if nn_pred[i]>0.5:
        nn_pred[i]=1
    elif nn_pred[i]<=0.5:
        nn_pred[i]=0

print("After: ",nn_pred)
