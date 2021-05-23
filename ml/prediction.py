from preload import model, vectorizer

import sys
import time
import pandas as pd


df = pd.DataFrame({"Sentence":[sys.argv[1],sys.argv[2]]})
posts = vectorizer.fit_transform(df['Sentence'].values.astype('U')).toarray()

#start = time.time()
nn_pred = model.predict(pd.DataFrame(posts))
for i in range(len(nn_pred)):
    if nn_pred[i]>0.5:
        nn_pred[i]=1
    elif nn_pred[i]<=0.5:
        nn_pred[i]=0
#end = time.time()
#print("Time: ", round(end-start,3), "seconds")
print(nn_pred[0][0])

