import pickle
import pandas
from sklearn import model_selection
# load the model from disk
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
# print(result)

#live data prediction
print(loaded_model.predict([[10,20,30,4,5,6,7,8]])[0])
a = loaded_model.predict([[10,20,30,4,5,6,7,8]])[0]

if int(a) ==1:
    print('diabitic')
else:
    print('not diabtic')