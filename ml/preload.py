import pandas as pd
import pickle
from keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer

print('Loading Model')


###########################################


feature_path = './ml/features.pkl'
vectorizer = CountVectorizer(vocabulary=pickle.load(open(feature_path, "rb")))
#posts = vectorizer.fit_transform(df['Sentence'].values.astype('U')).toarray()
#print(len(posts[0]))

model = load_model("./ml/model_NN.h5")
model.compile(loss='binary_crossentropy', 
              optimizer='adam', 
              metrics=['accuracy'])


