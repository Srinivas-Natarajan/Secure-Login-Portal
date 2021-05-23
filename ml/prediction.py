from preload import model, vectorizer

import sys
import pandas as pd

print('First param:'+sys.argv[1]+'#')
print('Second param:'+sys.argv[2]+'#\n')


df = pd.DataFrame({"Sentence":[sys.argv[1],sys.argv[2]]})
posts = vectorizer.fit_transform(df['Sentence'].values.astype('U')).toarray()
print(len(posts[0]))


nn_pred = model.predict(pd.DataFrame(posts))

print("Before: ",nn_pred)
for i in range(len(nn_pred)):
    if nn_pred[i]>0.5:
        nn_pred[i]=1
    elif nn_pred[i]<=0.5:
        nn_pred[i]=0

print("After: ",nn_pred)


