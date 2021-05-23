import tensorflow as tf
tf.autograph.set_verbosity(1)
import time
import pickle
from keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer

print('Loading Model')


###########################################

start = time.time()
feature_path = './ml/features.pkl'
vectorizer = CountVectorizer(vocabulary=pickle.load(open(feature_path, "rb")))
#posts = vectorizer.fit_transform(df['Sentence'].values.astype('U')).toarray()
#print(len(posts[0]))

model = load_model("./ml/model_NN.h5")
model.compile(loss='binary_crossentropy', 
              optimizer='adam', 
              metrics=['accuracy'])
end = time.time()
print("Time taken: ", round(end-start,3), "seconds")

